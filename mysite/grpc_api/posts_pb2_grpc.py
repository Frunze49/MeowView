# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_api.posts_pb2 as posts__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/posts.Greeter/SayHello',
                request_serializer=posts__pb2.HelloRequest.SerializeToString,
                response_deserializer=posts__pb2.HelloReply.FromString,
                )
        self.GetPost = channel.unary_unary(
                '/posts.Greeter/GetPost',
                request_serializer=posts__pb2.GetRequest.SerializeToString,
                response_deserializer=posts__pb2.GetReply.FromString,
                )
        self.AddPost = channel.unary_unary(
                '/posts.Greeter/AddPost',
                request_serializer=posts__pb2.AddRequest.SerializeToString,
                response_deserializer=posts__pb2.AddReply.FromString,
                )
        self.DeletePost = channel.unary_unary(
                '/posts.Greeter/DeletePost',
                request_serializer=posts__pb2.DeleteRequest.SerializeToString,
                response_deserializer=posts__pb2.DeleteReply.FromString,
                )
        self.UpdatePost = channel.unary_unary(
                '/posts.Greeter/UpdatePost',
                request_serializer=posts__pb2.UpdateRequest.SerializeToString,
                response_deserializer=posts__pb2.UpdateReply.FromString,
                )
        self.ListPost = channel.unary_unary(
                '/posts.Greeter/ListPost',
                request_serializer=posts__pb2.ListRequest.SerializeToString,
                response_deserializer=posts__pb2.ListReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=posts__pb2.HelloRequest.FromString,
                    response_serializer=posts__pb2.HelloReply.SerializeToString,
            ),
            'GetPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPost,
                    request_deserializer=posts__pb2.GetRequest.FromString,
                    response_serializer=posts__pb2.GetReply.SerializeToString,
            ),
            'AddPost': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPost,
                    request_deserializer=posts__pb2.AddRequest.FromString,
                    response_serializer=posts__pb2.AddReply.SerializeToString,
            ),
            'DeletePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePost,
                    request_deserializer=posts__pb2.DeleteRequest.FromString,
                    response_serializer=posts__pb2.DeleteReply.SerializeToString,
            ),
            'UpdatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePost,
                    request_deserializer=posts__pb2.UpdateRequest.FromString,
                    response_serializer=posts__pb2.UpdateReply.SerializeToString,
            ),
            'ListPost': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPost,
                    request_deserializer=posts__pb2.ListRequest.FromString,
                    response_serializer=posts__pb2.ListReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'posts.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.Greeter/SayHello',
            posts__pb2.HelloRequest.SerializeToString,
            posts__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.Greeter/GetPost',
            posts__pb2.GetRequest.SerializeToString,
            posts__pb2.GetReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.Greeter/AddPost',
            posts__pb2.AddRequest.SerializeToString,
            posts__pb2.AddReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.Greeter/DeletePost',
            posts__pb2.DeleteRequest.SerializeToString,
            posts__pb2.DeleteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.Greeter/UpdatePost',
            posts__pb2.UpdateRequest.SerializeToString,
            posts__pb2.UpdateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/posts.Greeter/ListPost',
            posts__pb2.ListRequest.SerializeToString,
            posts__pb2.ListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)