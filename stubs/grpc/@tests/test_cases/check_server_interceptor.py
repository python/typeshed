from __future__ import annotations

import typing

import grpc


class Request:
    pass


class Response:
    pass


class NoopInterceptor(grpc.ServerInterceptor[Request, Response]):
    def intercept_service(
        self,
        continuation: typing.Callable[[grpc.HandlerCallDetails], grpc.RpcMethodHandler[Request, Response] | None],
        handler_call_details: grpc.HandlerCallDetails,
    ) -> grpc.RpcMethodHandler[Request, Response] | None:
        return continuation(handler_call_details)
