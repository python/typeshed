import typing_extensions
from _typeshed import Incomplete
from collections.abc import Iterable

import grpc
from google.protobuf import descriptor_pool
from grpc import aio
from grpc_reflection.v1alpha import reflection_pb2 as _reflection_pb2
from grpc_reflection.v1alpha._base import BaseReflectionServicer

SERVICE_NAME: str

_AnyServer: typing_extensions.TypeAlias = grpc.Server | aio.Server
_AnyServicerContext: typing_extensions.TypeAlias = grpc.ServicerContext | aio.ServicerContext[Incomplete, Incomplete]

class ReflectionServicer(BaseReflectionServicer):
    def ServerReflectionInfo(
        self, request_iterator: Iterable[_reflection_pb2.ServerReflectionRequest], context: _AnyServicerContext
    ) -> None: ...

def enable_server_reflection(
    service_names: Iterable[str], server: _AnyServer, pool: descriptor_pool.DescriptorPool | None = ...
) -> None: ...
