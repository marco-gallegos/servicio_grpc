#!/bin/bash

# compilar el archivo proto de ventas cedis y guardarlos en la raiz
python -m grpc_tools.protoc -Igrpc --python_out=. --grpc_python_out=. grpc/ventacedis.proto