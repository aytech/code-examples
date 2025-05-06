import time
from datetime import datetime
from threading import Thread

from proto.hello_pb2_grpc import HelloServicer
from proto.hello_pb2 import HelloRequest
from proto.hello_pb2 import HelloResponse


class HelloService(HelloServicer):

    def SayHello(self, request: HelloRequest, context):
        print("\nSimple request received")
        return HelloResponse(name="Oleg", age=32)

    def SayHelloResponseStream(self, request: HelloResponse, context):
        print("\nServer streaming request received")
        for idx in range(3):
            yield HelloResponse(name="Oleg (server:%s)" % idx, age=32)
            time.sleep(1)

    def SayHelloRequestStream(self, request_iterator, context):
        print("\nClient streaming request received")
        response_names = []

        for idx, i in enumerate(request_iterator):
            print("\tReceived request for %s at %s" % (i.name, datetime.now().strftime("%H:%M:%S")))
            response_names.append("%s (server:%i)" % (i.name, idx))

        return HelloResponse(name="; ".join(response_names), age=32)

    def SayHelloBidirectionalStream(self, request_iterator, context):
        print("\nBidirectional streaming request received")
        received_requests = []

        # Open thread to parse data, although parsing
        # can be done in the same thread as well
        def parse_request():
            for request in request_iterator:
                print("\tReceived request for %s at %s" % (request.name, datetime.now().strftime("%H:%M:%S")))
                received_requests.append(request)

        t = Thread(target=parse_request())
        t.start()

        for idx, i in enumerate(received_requests):
            yield HelloResponse(name="%s (server:%s)" % (i.name, idx), age=32)
            time.sleep(1)

        t.join()
