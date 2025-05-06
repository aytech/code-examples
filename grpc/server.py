from concurrent import futures

import grpc

from proto.hello_pb2_grpc import add_HelloServicer_to_server
from services.HelloService import HelloService

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_HelloServicer_to_server(HelloService(), server=server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()