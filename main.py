"""
@autor Marco A. Gallegos
@date 2019/12/05
@descripcion importa los modulos/endpoints para levangtar el servidcio de grpc
"""

import ventacedis_pb2
import ventacedis_pb2_grpc

from concurrent import futures
import logging

import grpc

import db_service as dbs


class Greeter(ventacedis_pb2_grpc.dbServicer):
    """Esta clase engloba las funciones que se pueden llamar la funcion debe tener el mismo nombre que la funcion
    en el archivo rpoto"""
    def dbData(self, request, context):
        #return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
        response = ventacedis_pb2.Response(value=False)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ventacedis_pb2_grpc.add_dbServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()