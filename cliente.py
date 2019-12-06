"""
@autor Marco A. Gallegos
@date 2019/12/05
@descripcion ejemplo de como consumir el servicio grpc
"""

from __future__ import print_function
import logging

import grpc

import ventacedis_pb2
import ventacedis_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = ventacedis_pb2_grpc.dbStub(channel)
      response = stub.dbData(ventacedis_pb2.Params(value=True))
      print("client received: " + str(response.value))



if __name__ == '__main__':
    logging.basicConfig()
    run()