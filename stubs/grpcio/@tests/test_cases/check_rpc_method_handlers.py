from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping
from typing import TYPE_CHECKING, Any, TypeAlias
from typing_extensions import assert_type

import grpc


def sync_unary(request: str, context: grpc.ServicerContext) -> str:
    return request


async def async_unary(request: str, context: grpc.aio.ServicerContext[str, str]) -> str:
    return request


async def async_unary_stream(request: str, context: grpc.aio.ServicerContext[str, str]) -> AsyncIterator[str]:
    yield request


async def async_stream_unary(requests: AsyncIterator[str], context: grpc.aio.ServicerContext[str, str]) -> str:
    return await anext(requests)


async def async_stream_stream(requests: AsyncIterator[str], context: grpc.aio.ServicerContext[str, str]) -> AsyncIterator[str]:
    async for request in requests:
        yield request


async def async_write(request: str, context: grpc.aio.ServicerContext[str, str]) -> None:
    await context.write(request)


async def async_stream_write(requests: AsyncIterator[str], context: grpc.aio.ServicerContext[str, str]) -> None:
    async for request in requests:
        await context.write(request)


def sync_unary_stream(request: str, context: grpc.ServicerContext) -> Iterator[str]:
    yield request


def sync_stream_unary(requests: Iterator[str], context: grpc.ServicerContext) -> str:
    return next(requests)


def sync_stream(requests: Iterator[str], context: grpc.ServicerContext) -> Iterator[str]:
    return requests


assert_type(grpc.unary_stream_rpc_method_handler(sync_unary_stream, bytes.decode, str.encode), grpc.RpcMethodHandler[str, str])
assert_type(grpc.stream_unary_rpc_method_handler(sync_stream_unary, bytes.decode, str.encode), grpc.RpcMethodHandler[str, str])
assert_type(grpc.unary_unary_rpc_method_handler(sync_unary, bytes.decode, str.encode), grpc.RpcMethodHandler[str, str])
assert_type(grpc.stream_stream_rpc_method_handler(sync_stream, bytes.decode, str.encode), grpc.RpcMethodHandler[str, str])
assert_type(grpc.unary_unary_rpc_method_handler(async_unary), grpc.aio._AsyncRpcMethodHandler[str, str])
assert_type(grpc.unary_stream_rpc_method_handler(async_unary_stream), grpc.aio._AsyncRpcMethodHandler[str, str])
assert_type(grpc.stream_unary_rpc_method_handler(async_stream_unary), grpc.aio._AsyncRpcMethodHandler[str, str])
assert_type(grpc.stream_stream_rpc_method_handler(async_stream_stream), grpc.aio._AsyncRpcMethodHandler[str, str])
assert_type(grpc.unary_stream_rpc_method_handler(async_write), grpc.aio._AsyncRpcMethodHandler[str, str])
assert_type(grpc.stream_stream_rpc_method_handler(async_stream_write), grpc.aio._AsyncRpcMethodHandler[str, str])

sync_handlers = {"Check": grpc.unary_unary_rpc_method_handler(sync_unary, bytes.decode, str.encode)}
grpc.method_handlers_generic_handler("test.Sync", sync_handlers)
async_handlers = {"Check": grpc.unary_unary_rpc_method_handler(async_unary)}
grpc.method_handlers_generic_handler("test.Async", async_handlers)


# The synchronous fallback must still accept the callback-based streaming API.
def nonblocking_watch(request: str, context: grpc.ServicerContext, send_response_callback: object) -> None:
    pass


assert_type(grpc.unary_stream_rpc_method_handler(nonblocking_watch, bytes.decode, str.encode), grpc.RpcMethodHandler[str, str])


# These classes are generic only in the stubs.
if TYPE_CHECKING:
    _AsyncGenericHandlerBase: TypeAlias = grpc.GenericRpcHandler[grpc.aio._AsyncRpcMethodHandler[str, str]]
    _AsyncServiceHandlerBase: TypeAlias = grpc.ServiceRpcHandler[grpc.aio._AsyncRpcMethodHandler[str, str]]
else:
    _AsyncGenericHandlerBase = grpc.GenericRpcHandler
    _AsyncServiceHandlerBase = grpc.ServiceRpcHandler


# Custom handlers must accept async factory results without widening sync callers.
class AsyncGenericHandler(_AsyncGenericHandlerBase):
    def service(self, handler_call_details: grpc.HandlerCallDetails) -> grpc.aio._AsyncRpcMethodHandler[str, str] | None:
        if handler_call_details.method == "/test.Async/Check":
            return grpc.unary_unary_rpc_method_handler(async_unary)
        return None


class AsyncServiceHandler(_AsyncServiceHandlerBase):
    def service(self, handler_call_details: grpc.HandlerCallDetails) -> grpc.aio._AsyncRpcMethodHandler[str, str]:
        return grpc.unary_unary_rpc_method_handler(async_unary)

    def service_name(self) -> str:
        return "test.Async"


def check_generic_handlers(sync_handler: grpc.GenericRpcHandler, details: grpc.HandlerCallDetails) -> None:
    assert_type(sync_handler.service(details), grpc.RpcMethodHandler[Any, Any] | None)
    async_handler = grpc.method_handlers_generic_handler("test.Async", async_handlers)
    assert_type(async_handler.service(details), grpc.aio._AsyncRpcMethodHandler[str, str] | None)
    sync_generic = grpc.method_handlers_generic_handler("test.Sync", sync_handlers)
    assert_type(sync_generic.service(details), grpc.RpcMethodHandler[str, str] | None)
    server = grpc.aio.server(handlers=[AsyncGenericHandler(), AsyncServiceHandler(), async_handler, sync_handler])
    server.add_generic_rpc_handlers([AsyncGenericHandler(), AsyncServiceHandler(), async_handler, sync_handler])


# An aio server can register and resolve both kinds of handler together.
def check_mixed_registration(server: grpc.aio.Server, details: grpc.HandlerCallDetails) -> None:
    mixed: Mapping[str, grpc.RpcMethodHandler[str, str] | grpc.aio._AsyncRpcMethodHandler[str, str]] = {
        "Sync": grpc.unary_unary_rpc_method_handler(sync_unary, bytes.decode, str.encode),
        "Async": grpc.unary_unary_rpc_method_handler(async_unary),
    }
    generic = grpc.method_handlers_generic_handler("test.Mixed", mixed)
    assert_type(generic.service(details), grpc.RpcMethodHandler[str, str] | grpc.aio._AsyncRpcMethodHandler[str, str] | None)
    grpc.aio.server(handlers=[generic])
    server.add_generic_rpc_handlers([generic])
    server.add_registered_method_handlers("test.Mixed", mixed)


# Any-returning callbacks must remain usable by synchronous servers. Their
# response type is deliberately not asserted: checkers resolve Any differently.
def dynamic_unary(request: str, context: Any) -> Any:
    return request


def dynamic_stream(requests: Iterator[str], context: Any) -> Any:
    return next(requests)


async def partial_async_unary(request: str, context: Any) -> str:
    return request


async def partial_async_unary_stream(request: str, context: Any) -> AsyncIterator[str]:
    yield request


async def partial_async_stream_unary(requests: AsyncIterator[str], context: Any) -> str:
    return await anext(requests)


async def partial_async_stream_stream(requests: AsyncIterator[str], context: Any) -> AsyncIterator[str]:
    async for request in requests:
        yield request


def check_dynamic_callbacks(server: grpc.Server, aio_server: grpc.aio.Server) -> None:
    handlers: dict[str, grpc.RpcMethodHandler[str, str]] = {
        "UnaryUnary": grpc.unary_unary_rpc_method_handler(dynamic_unary, bytes.decode, str.encode),
        "UnaryStream": grpc.unary_stream_rpc_method_handler(dynamic_unary, bytes.decode, str.encode),
        "StreamUnary": grpc.stream_unary_rpc_method_handler(dynamic_stream, bytes.decode, str.encode),
        "StreamStream": grpc.stream_stream_rpc_method_handler(dynamic_stream, bytes.decode, str.encode),
        "KeywordUnaryUnary": grpc.unary_unary_rpc_method_handler(dynamic_unary, response_serializer=str.encode),
        "KeywordUnaryStream": grpc.unary_stream_rpc_method_handler(dynamic_unary, response_serializer=str.encode),
        "KeywordStreamUnary": grpc.stream_unary_rpc_method_handler(dynamic_stream, response_serializer=str.encode),
        "KeywordStreamStream": grpc.stream_stream_rpc_method_handler(dynamic_stream, response_serializer=str.encode),
        "RawUnaryUnary": grpc.unary_unary_rpc_method_handler(dynamic_unary),
        "RawUnaryStream": grpc.unary_stream_rpc_method_handler(dynamic_unary),
        "RawStreamUnary": grpc.stream_unary_rpc_method_handler(dynamic_stream),
        "RawStreamStream": grpc.stream_stream_rpc_method_handler(dynamic_stream),
    }
    server.add_registered_method_handlers("test.Dynamic", handlers)
    server.add_generic_rpc_handlers([grpc.method_handlers_generic_handler("test.Dynamic", handlers)])
    aio_server.add_registered_method_handlers("test.Dynamic", handlers)


# A broad context annotation must not cause a coroutine to be inferred as a
# synchronous behavior when the serializer supplies a concrete response type.
partial_async_handlers: dict[str, grpc.aio._AsyncRpcMethodHandler[str, str]] = {
    "UnaryUnary": grpc.unary_unary_rpc_method_handler(partial_async_unary, bytes.decode, str.encode),
    "UnaryStream": grpc.unary_stream_rpc_method_handler(partial_async_unary_stream, bytes.decode, str.encode),
    "StreamUnary": grpc.stream_unary_rpc_method_handler(partial_async_stream_unary, bytes.decode, str.encode),
    "StreamStream": grpc.stream_stream_rpc_method_handler(partial_async_stream_stream, bytes.decode, str.encode),
}
# Without enough annotations or a serializer, avoid claiming a specific kind.
assert_type(grpc.unary_unary_rpc_method_handler(partial_async_unary), Any)
assert_type(grpc.unary_stream_rpc_method_handler(partial_async_unary_stream), Any)
