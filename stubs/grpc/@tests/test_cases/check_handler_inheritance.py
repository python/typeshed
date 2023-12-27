from __future__ import annotations

import typing
from typing_extensions import assert_type

import grpc


class Request:
    pass


class Response:
    pass


def unary_unary_call(rq: Request, ctx: grpc.ServicerContext) -> Response:
    assert_type(rq, Request)
    return Response()


class ServiceHandler(grpc.ServiceRpcHandler[Request, Response]):
    def service(self, handler_call_details: grpc.HandlerCallDetails) -> typing.Optional[grpc.RpcMethodHandler[Request, Response]]:
        rpc = grpc.RpcMethodHandler[Request, Response]()
        rpc.unary_unary = unary_unary_call
        return rpc


h = ServiceHandler()
ctx = grpc.ServicerContext()
svc = h.service(grpc.HandlerCallDetails())
if svc is not None and svc.unary_unary is not None:
    svc.unary_unary(Request(), ctx)
