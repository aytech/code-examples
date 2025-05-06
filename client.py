import time
from datetime import datetime

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
        print("\nSimple RPC:")
        response: HelloResponse = stub.SayHello(HelloRequest(name="Oleg"))
        print("\tSimple RPC response: %s at %s" % (response.name, datetime.now().strftime("%H:%M:%S")))

        ### Add streaming response
        print("\nResponse streaming RPC: ")
        response_stream = stub.SayHelloResponseStream(HelloRequest(name="Oleg"))
        for r in response_stream:
            print("\tServer streaming response: %s, at %s" % (r.name, datetime.now().strftime("%H:%M:%S")))

        ### Add streaming request
        print("\nRequest streaming RPC: ")

        def server_requests():
            for i in range(5):
                if i not in (2, 4):
                    yield HelloRequest(name="Oleg (client:%s)" % i)
                time.sleep(1)

        response = stub.SayHelloRequestStream(server_requests())
        print("\tClient streaming response: %s, at %s" % (response.name, datetime.now().strftime("%H:%M:%S")))

        ### Add bidirectional RPC request
        print("\nBidirectional RPC: ")

        def server_requests():
            for i in range(5):
                if i not in (1, 3):
                    yield HelloRequest(name="Oleg (client:%s)" % i)
                time.sleep(1)

        response_iterator = stub.SayHelloBidirectionalStream(server_requests())
        for response in response_iterator:
            print("\tBidirectional response: %s, at %s" % (response.name, datetime.now().strftime("%H:%M:%S")))


if __name__ == '__main__':
    run()
