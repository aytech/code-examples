import grpc

from proto.hello_pb2_grpc import HelloStub
from proto.hello_pb2 import HelloRequest, HelloResponse

class RequestIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise Exception


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = HelloStub(channel)
        response: HelloResponse = stub.SayHello(HelloRequest(name="Oleg"))
        print("\nSimple RPC: Name: " + response.name + ", Age: " + str(response.age))
        ### Add streaming response
        # print("\nResponse streaming RPC: ")
        # for response in stub.SayHelloResponseStream(HelloRequest(name="Oleg")):
        #     print("\tName: " + response.name + ", Age: " + str(response.age))
        ### Add streaming request
        print("\nRequest streaming RPC: ")
        print(stub.SayHelloRequestStream([HelloRequest(name="Oleg")]))
        # Add bidirectional RPC request
        print("Bidirectional RPC: ")

if __name__ == '__main__':
    run()