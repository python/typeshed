from __future__ import annotations

import inspect
from collections.abc import Awaitable, Callable
from concurrent.futures.thread import ThreadPoolExecutor
from typing import TYPE_CHECKING, TypeVar
from typing_extensions import TypeGuard

import grpc
import grpc.aio

if TYPE_CHECKING:
    from grpc.aio import _AsyncRpcMethodHandler

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
        continuation: Callable[
            [grpc.HandlerCallDetails],
            Awaitable[grpc.RpcMethodHandler[RequestT, ResponseT] | _AsyncRpcMethodHandler[RequestT, ResponseT] | None],
        ],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler[RequestT, ResponseT] | _AsyncRpcMethodHandler[RequestT, ResponseT] | None:
        return await continuation(handler_call_details)


grpc.aio.server(interceptors=[NoopAioInterceptor()])


def is_async_unary_handler(
    handler: grpc.RpcMethodHandler[RequestT, ResponseT] | _AsyncRpcMethodHandler[RequestT, ResponseT],
) -> TypeGuard[_AsyncRpcMethodHandler[RequestT, ResponseT]]:
    return inspect.iscoroutinefunction(handler.unary_unary)


class WrappingAioInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(
        self,
        continuation: Callable[
            [grpc.HandlerCallDetails],
            Awaitable[grpc.RpcMethodHandler[RequestT, ResponseT] | _AsyncRpcMethodHandler[RequestT, ResponseT] | None],
        ],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler[RequestT, ResponseT] | _AsyncRpcMethodHandler[RequestT, ResponseT] | None:
        handler = await continuation(handler_call_details)
        if handler is None or not is_async_unary_handler(handler) or handler.unary_unary is None:
            return handler
        inner = handler.unary_unary

        async def behavior(request: RequestT, context: grpc.aio.ServicerContext[RequestT, ResponseT]) -> ResponseT:
            return await inner(request, context)

        return grpc.unary_unary_rpc_method_handler(behavior, handler.request_deserializer, handler.response_serializer)
