from __future__ import annotations

from collections.abc import AsyncIterator, Callable
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Awaitable, TypeVar, cast

import grpc
import grpc.aio

RequestT = TypeVar("RequestT")
ResponseT = TypeVar("ResponseT")


class NoopInterceptor(grpc.ServerInterceptor):
    def intercept_service(
        self,
        continuation: Callable[[grpc.HandlerCallDetails], grpc.RpcMethodHandler[RequestT, ResponseT] | None],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler[RequestT, ResponseT] | None:
        return continuation(handler_call_details)


grpc.server(interceptors=[NoopInterceptor()], thread_pool=ThreadPoolExecutor())


class NoopAioInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(
        self,
        continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.aio.RpcMethodHandler[RequestT, ResponseT]]],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.aio.RpcMethodHandler[RequestT, ResponseT]:
        return await continuation(handler_call_details)


grpc.aio.server(interceptors=[NoopAioInterceptor()])

aio_handler = grpc.aio.RpcMethodHandler[RequestT, ResponseT]()
aio_handler.unary_unary = cast(Callable[[RequestT, grpc.aio.ServicerContext[RequestT, ResponseT]], Awaitable[ResponseT]], None)
aio_handler.unary_stream = cast(
    Callable[[RequestT, grpc.aio.ServicerContext[RequestT, ResponseT]], AsyncIterator[ResponseT]], None
)
aio_handler.stream_unary = cast(
    Callable[[AsyncIterator[RequestT], grpc.aio.ServicerContext[RequestT, ResponseT]], Awaitable[ResponseT]], None
)
aio_handler.stream_stream = cast(
    Callable[[AsyncIterator[RequestT], grpc.aio.ServicerContext[RequestT, ResponseT]], AsyncIterator[ResponseT]], None
)
