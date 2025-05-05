import grpc

from proto.hello_pb2_grpc import HelloStub
from proto.hello_pb2 import HelloRequest, HelloResponse


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = HelloStub(channel)
        response: HelloResponse = stub.SayHello(HelloRequest(name="Oleg"))
        print("Client received: Name: " + response.name + ", Age: " + str(response.age))

if __name__ == '__main__':
    run()