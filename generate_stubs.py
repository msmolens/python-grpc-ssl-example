#!/usr/bin/env python
"""Run protoc to generate messages and gRPC stubs from .proto definitions."""

from grpc_tools import protoc

args = [
    '',
    '-I./protos',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/shopping_list.proto',
    ]
protoc.main(args)
