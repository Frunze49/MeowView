# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from concurrent import futures
import logging

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update, func, and_


import grpc
import posts_pb2
import posts_pb2_grpc

from statistics import statistics_pb2
from statistics import statistics_pb2_grpc

from db_connector.database import PostSession
from db_connector.model import Post

from statistics.model import Statistics
from statistics.database import StatisticsSession

from sqlalchemy import Integer


class StatisticGreeter(statistics_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.statistics_session = StatisticsSession()
        self.post_session = PostSession()

    def GetStatistics(self, request, context):
        likes = self.statistics_session.query(Statistics).filter_by(post_id=request.post_id, like=True).count()
        views = self.statistics_session.query(Statistics).filter_by(post_id=request.post_id, view=True).count()
        return statistics_pb2.StatisticResponse(likes=likes, views=views)

    def TopPosts(self, request, context):

        subquery = (
            self.statistics_session.query(
                Statistics.post_id,
                func.sum(Statistics.like.cast(Integer)).label('total_likes'),
                func.sum(Statistics.view.cast(Integer)).label('total_views'),
            )
            .group_by(Statistics.post_id)
            .subquery()
        )

        print(f"Subquery SQL: {str(subquery)}", file=sys.stderr)

        top_5_query = None
        if request.filter == 'like':
            top_5_query = self.statistics_session.query(subquery.c.post_id, subquery.c.total_likes, subquery.c.total_views)\
                                    .order_by(subquery.c.total_likes.desc())\
                                    .limit(5)\
                                    .all()
        elif request.filter == 'view':
            top_5_query = self.statistics_session.query(subquery.c.post_id, subquery.c.total_likes, subquery.c.total_views)\
                                    .order_by(subquery.c.total_views.desc())\
                                    .limit(5)\
                                    .all()

        out = []
        for result in top_5_query:
            post = self.post_session.query(Post).filter_by(id=result.post_id).first()
            found = statistics_pb2.Post(
                post_id=post.id,
                author=post.login,
                description=post.description,
                image=post.image,
                likes=result.total_likes,
                views=result.total_views,
            )
            out.append(found)
            
        return statistics_pb2.TopPostsResponse(posts=out)


    def TopUsers(self, request, context):

        subquery = (
            self.statistics_session.query(
                Statistics.author,
                func.sum(Statistics.like.cast(Integer)).label('total_likes'),
            )
            .group_by(Statistics.author)
            .subquery()
        )

        print(f"Subquery SQL: {str(subquery)}", file=sys.stderr)

        top_3_query = self.statistics_session.query(subquery.c.author, subquery.c.total_likes)\
                                             .order_by(subquery.c.total_likes.desc())\
                                             .limit(3)\
                                             .all()
        
        print(f"Top 3: {str(top_3_query)}", file=sys.stderr)

        out = []
        for inst in top_3_query:
            likes = self.statistics_session.query(Statistics).filter_by(author=inst.author, like=True).count()
            found = statistics_pb2.User(
                author=inst.author,
                likes=likes,
            )
            out.append(found)

        print(f"OUT: {out}", file=sys.stderr)
            
        return statistics_pb2.TopUsersResponse(users=out)

        

class Greeter(posts_pb2_grpc.GreeterServicer):

    def __init__(self):
        self.post_session = PostSession()

    def SayHello(self, request, context):
        return posts_pb2.HelloReply(message="Hello, %s!" % request.name)
    
    def GetPost(self, request, context):
        post = self.post_session.query(Post).filter_by(id=request.id).first()
        if post:
            found = posts_pb2.Post(
                id=post.id,
                login=post.login,
                description=post.description,
                image=post.image
            )
            return posts_pb2.GetReply(success=True, message='200 OK', post=found)

        return posts_pb2.GetReply(success=False, message='404 Not Found', post=None)
    
    def AddPost(self, request, context):
        try:
            new_data = Post(login=request.post.login, description=request.post.description,
                            image=request.post.image)
            self.post_session.add(new_data)
            self.post_session.commit()
        except Exception as e:
            self.post_session.rollback()
            return posts_pb2.AddReply(success=False, message="Failed to add post: " + str(e))
        return posts_pb2.AddReply(success=True, message="Post added successfully")


    def DeletePost(self, request, context):
        post = self.post_session.query(Post).filter_by(id=request.id).first()
        if post and post.login == request.login:
            self.post_session.delete(post)
            self.post_session.commit()
            return posts_pb2.AddReply(success=True, message="Post deleted successfully")
        return posts_pb2.AddReply(success=False, message="No permissions")
    

    def UpdatePost(self, request, context):
        post = self.post_session.query(Post).filter_by(id=request.post.id).first()
        if post and post.login == request.post.login:
            post.image = request.post.image
            post.description = request.post.description
            self.post_session.commit()
            return posts_pb2.AddReply(success=True, message="Post updated successfully")
        return posts_pb2.AddReply(success=False, message="No permissions")

    def ListPost(self, request, context):
        posts = self.post_session.query(Post).all()
        out = []
        if posts:
            for post in posts:
                found = posts_pb2.Post(
                    id=post.id,
                    login=post.login,
                    description=post.description,
                    image=post.image
                )
                out.append(found)
        return posts_pb2.ListReply(success=True, message='200 OK', list=out)


def serve():
    port = "50051"
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=[
            ('grpc.max_receive_message_length', 10 * 1024 * 1024)  # 10 MB
        ]
    )
    posts_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    statistics_pb2_grpc.add_GreeterServicer_to_server(StatisticGreeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
