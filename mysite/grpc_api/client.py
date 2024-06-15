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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import posts_pb2
import posts_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")

    # with grpc.insecure_channel("localhost:50051") as channel:
    #     stub = posts_pb2_grpc.GreeterStub(channel)
    #     response = stub.GetPost(posts_pb2.GetRequest(id=1, login='Adil'))

    # with grpc.insecure_channel("localhost:50051") as channel:
    #     stub = posts_pb2_grpc.GreeterStub(channel)
    #     post = posts_pb2.Post(
    #         login='Adil',
    #         description='Hello',
    #         image=b"example_image_data"
    #     )
    #     response = stub.AddPost(posts_pb2.AddRequest(post=post))

    # with grpc.insecure_channel("localhost:50051") as channel:
    #     stub = posts_pb2_grpc.GreeterStub(channel)
    #     response = stub.DeletePost(posts_pb2.DeleteRequest(id=1, login='Adil'))

    # with grpc.insecure_channel("localhost:50051") as channel:
    #     stub = posts_pb2_grpc.GreeterStub(channel)
    #     post = posts_pb2.Post(
    #         id=2
    #         login='Adil',
    #         description='Hello123',
    #         image=b"example_image_data"
    #     )
    #     response = stub.UpdatePost(posts_pb2.UpdateRequest(post=post, description_flag=True, image_flag=False))

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = posts_pb2_grpc.GreeterStub(channel)
        response = stub.ListPost(posts_pb2.ListRequest(login='Adil'))

    print("Greeter client received: " + response.message)
    print(response.list)

if __name__ == "__main__":
    logging.basicConfig()
    run()
