import typing

import grpc
from grpc import aio
from google.protobuf import descriptor_pool
from grpc_reflection.v1alpha import reflection_pb2 as _reflection_pb2
from grpc_reflection.v1alpha._base import BaseReflectionServicer

SERVICE_NAME: str

AnyServer = typing.Union[grpc.Server, aio.Server]
AnyServicerContext = typing.Union[grpc.ServicerContext, aio.ServicerContext]

class ReflectionServicer(BaseReflectionServicer):
    def ServerReflectionInfo(
        self,
        request_iterator: typing.Iterable[_reflection_pb2.ServerReflectionRequest],
        context: AnyServicerContext,
    ) -> None:
        ...

def enable_server_reflection(
    service_names: typing.Iterable[str],
    server: AnyServer,
    pool: typing.Optional[descriptor_pool.DescriptorPool] = ...,
) -> None:
    ...
