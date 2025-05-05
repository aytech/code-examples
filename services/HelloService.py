from time import sleep
from typing import List

from proto.hello_pb2_grpc import HelloServicer
from proto.hello_pb2 import HelloRequest
from proto.hello_pb2 import HelloResponse


class HelloService(HelloServicer):

    def SayHello(self, request: HelloRequest, context):
        return HelloResponse(name="Oleg", age=32)

    def SayHelloResponseStream(self, request: HelloResponse, context):
        for name_idx in range(1, 5):
            sleep(1)
            yield HelloResponse(name="Oleg {name}".format(name=str(name_idx)), age=32)

    def SayHelloRequestStream(self, request_iterator, context):
        print(request_iterator)
        # request_count = 0
        # request_name = None
        #
        for name_req in request_iterator:
            print(name_req)
        #     request_count += 1
        #     request_name = name_req
        return HelloResponse(name="{name} {idx}".format(name="Foo", idx=1), age=32)

    def SayHelloBidirectionalStream(self, request_iterator: List[HelloResponse], context):
        prev_requests = []
        for name_req in request_iterator:
            for prev_request in prev_requests:
                if prev_request.name == name_req.name:
                    yield prev_request
            prev_requests.append(name_req)

