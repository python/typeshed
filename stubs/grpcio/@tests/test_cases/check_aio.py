from __future__ import annotations

import typing
from typing_extensions import assert_type

import grpc.aio

assert_type(grpc.aio.Server(), grpc.aio.Server)  # type: ignore[abstract]

# Interceptor casts
client_interceptors = [typing.cast(grpc.aio.ClientInterceptor, "interceptor")]
grpc.aio.insecure_channel("target", interceptors=client_interceptors)

server_interceptors = [typing.cast(grpc.aio.ServerInterceptor[typing.Any, typing.Any], "interceptor")]
grpc.aio.server(interceptors=server_interceptors)


# Metadata
async def metadata() -> None:
    metadata = await typing.cast(grpc.aio.Call, None).initial_metadata()
    assert_type(metadata["foo"], grpc.aio._MetadataValue)
    for k in metadata:
        assert_type(k, str)

    for k, v in metadata.items():
        assert_type(k, str)
        assert_type(v, grpc.aio._MetadataValue)
