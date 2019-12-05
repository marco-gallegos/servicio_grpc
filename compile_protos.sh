#!/bin/bash

python -m grpc_tools.protoc -Igrpc --python_out=. --grpc_python_out=. grpc/ventacedis.proto