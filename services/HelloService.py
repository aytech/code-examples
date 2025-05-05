from proto.hello_pb2_grpc import HelloServicer
from proto.hello_pb2 import HelloRequest
from proto.hello_pb2 import HelloResponse


class HelloService(HelloServicer):

    def SayHello(self, request: HelloRequest, context):
        return HelloResponse(name="Oleg", age=32)