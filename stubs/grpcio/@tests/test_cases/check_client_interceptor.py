from __future__ import annotations

from collections.abc import Callable
from typing import AsyncIterable, AsyncIterator, Awaitable, Iterable, Iterator, TypeVar

import grpc
import grpc.aio

RequestT = TypeVar("RequestT")
ResponseT = TypeVar("ResponseT")


class NoopUnaryUnaryInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(
        self,
        continuation: Callable[[grpc.ClientCallDetails, RequestT], grpc._CallFuture[ResponseT]],
        client_call_details: grpc.ClientCallDetails,
        request: RequestT,
    ) -> grpc._CallFuture[ResponseT]:
        return continuation(client_call_details, request)


class NoopUnaryStreamInterceptor(grpc.UnaryStreamClientInterceptor):
    def intercept_unary_stream(
        self,
        continuation: Callable[[grpc.ClientCallDetails, RequestT], grpc._CallIterator[ResponseT]],
        client_call_details: grpc.ClientCallDetails,
        request: RequestT,
    ) -> grpc._CallIterator[ResponseT]:
        return continuation(client_call_details, request)


class NoopStreamUnaryInterceptor(grpc.StreamUnaryClientInterceptor):
    def intercept_stream_unary(
        self,
        continuation: Callable[[grpc.ClientCallDetails, Iterator[RequestT]], grpc._CallFuture[ResponseT]],
        client_call_details: grpc.ClientCallDetails,
        request_iterator: Iterator[RequestT],
    ) -> grpc._CallFuture[ResponseT]:
        return continuation(client_call_details, request_iterator)


class NoopStreamStreamInterceptor(grpc.StreamStreamClientInterceptor):
    def intercept_stream_stream(
        self,
        continuation: Callable[[grpc.ClientCallDetails, Iterator[RequestT]], grpc._CallIterator[ResponseT]],
        client_call_details: grpc.ClientCallDetails,
        request_iterator: Iterator[RequestT],
    ) -> grpc._CallIterator[ResponseT]:
        return continuation(client_call_details, request_iterator)


channel = grpc.insecure_channel("target")
channel = grpc.intercept_channel(
    channel,
    NoopUnaryUnaryInterceptor(),
    NoopUnaryStreamInterceptor(),
    NoopStreamUnaryInterceptor(),
    NoopStreamStreamInterceptor(),
)


class NoopAioUnaryUnaryInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self,
        continuation: Callable[[grpc.aio.ClientCallDetails, RequestT], Awaitable[grpc.aio.UnaryUnaryCall[RequestT, ResponseT]]],
        client_call_details: grpc.aio.ClientCallDetails,
        request: RequestT,
    ) -> ResponseT | grpc.aio.UnaryUnaryCall[RequestT, ResponseT]:
        return await continuation(client_call_details, request)


class NoopAioUnaryStreamInterceptor(grpc.aio.UnaryStreamClientInterceptor):
    async def intercept_unary_stream(
        self,
        continuation: Callable[[grpc.aio.ClientCallDetails, RequestT], Awaitable[grpc.aio.UnaryStreamCall[RequestT, ResponseT]]],
        client_call_details: grpc.aio.ClientCallDetails,
        request: RequestT,
    ) -> AsyncIterator[ResponseT] | grpc.aio.UnaryStreamCall[RequestT, ResponseT]:
        return await continuation(client_call_details, request)


class NoopAioStreamUnaryInterceptor(grpc.aio.StreamUnaryClientInterceptor):
    async def intercept_stream_unary(
        self,
        continuation: Callable[
            [grpc.aio.ClientCallDetails, AsyncIterable[RequestT] | Iterable[RequestT]],
            Awaitable[grpc.aio.StreamUnaryCall[RequestT, ResponseT]],
        ],
        client_call_details: grpc.aio.ClientCallDetails,
        request_iterator: AsyncIterable[RequestT] | Iterable[RequestT],
    ) -> ResponseT | grpc.aio.StreamUnaryCall[RequestT, ResponseT]:
        return await continuation(client_call_details, request_iterator)


class NoopAioStreamStreamInterceptor(grpc.aio.StreamStreamClientInterceptor):
    async def intercept_stream_stream(
        self,
        continuation: Callable[
            [grpc.aio.ClientCallDetails, AsyncIterable[RequestT] | Iterable[RequestT]],
            Awaitable[grpc.aio.StreamStreamCall[RequestT, ResponseT]],
        ],
        client_call_details: grpc.aio.ClientCallDetails,
        request_iterator: AsyncIterable[RequestT] | Iterable[RequestT],
    ) -> AsyncIterator[ResponseT] | grpc.aio.StreamStreamCall[RequestT, ResponseT]:
        return await continuation(client_call_details, request_iterator)


grpc.aio.insecure_channel(
    "target",
    interceptors=[
        NoopAioUnaryUnaryInterceptor(),
        NoopAioUnaryStreamInterceptor(),
        NoopAioStreamUnaryInterceptor(),
        NoopAioStreamStreamInterceptor(),
    ],
)
