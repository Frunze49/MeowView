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

from concurrent import futures
import logging

from sqlalchemy.exc import SQLAlchemyError

import grpc
import posts_pb2
import posts_pb2_grpc

from db_connector.database import Session
from db_connector.model import Post

class Greeter(posts_pb2_grpc.GreeterServicer):

    def __init__(self):
        self.session = Session()

    def SayHello(self, request, context):
        return posts_pb2.HelloReply(message="Hello, %s!" % request.name)
    
    def GetPost(self, request, context):
        post = self.session.query(Post).filter_by(id=request.id).first()
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
            self.session.add(new_data)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            return posts_pb2.AddReply(success=False, message="Failed to add post: " + str(e))
        return posts_pb2.AddReply(success=True, message="Post added successfully")


    def DeletePost(self, request, context):
        post = self.session.query(Post).filter_by(id=request.id).first()
        if post and post.login == request.login:
            self.session.delete(post)
            self.session.commit()
            return posts_pb2.AddReply(success=True, message="Post deleted successfully")
        return posts_pb2.AddReply(success=False, message="No permissions")
    

    def UpdatePost(self, request, context):
        post = self.session.query(Post).filter_by(id=request.post.id).first()
        if post and post.login == request.post.login:
            post.image = request.post.image
            post.description = request.post.description
            self.session.commit()
            return posts_pb2.AddReply(success=True, message="Post updated successfully")
        return posts_pb2.AddReply(success=False, message="No permissions")

    def ListPost(self, request, context):
        posts = self.session.query(Post).all()
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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    posts_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
