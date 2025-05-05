#!/usr/bin/env bash

python -m grpc_tools.protoc \
    -Iproto=./protobuf \
    --python_out=. \
    --pyi_out=. \
    --grpc_python_out=. \
    ./protobuf/*.proto