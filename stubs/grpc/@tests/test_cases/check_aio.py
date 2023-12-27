from __future__ import annotations

import typing
from typing_extensions import assert_type

import grpc.aio

assert_type(grpc.aio.Channel(), grpc.aio.Channel)
assert_type(grpc.aio.Server(), grpc.aio.Server)

# Interceptor casts
client_interceptors = [typing.cast(grpc.aio.ClientInterceptor, "interceptor")]
grpc.aio.insecure_channel("target", interceptors=client_interceptors)

server_interceptors = [typing.cast(grpc.aio.ServerInterceptor[typing.Any, typing.Any], "interceptor")]
grpc.aio.server(interceptors=server_interceptors)
