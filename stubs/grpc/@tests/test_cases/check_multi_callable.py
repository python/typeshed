from __future__ import annotations

import typing
from typing_extensions import assert_type

import grpc


class DummyRequest:
    pass


class DummyReply:
    pass


class DummyServiceStub(typing.Protocol):
    UnaryUnary: grpc.UnaryUnaryMultiCallable[DummyRequest, DummyReply]
    UnaryStream: grpc.UnaryStreamMultiCallable[DummyRequest, DummyReply]
    StreamUnary: grpc.StreamUnaryMultiCallable[DummyRequest, DummyReply]
    StreamStream: grpc.StreamStreamMultiCallable[DummyRequest, DummyReply]


stub: DummyServiceStub = typing.cast(typing.Any, None)
req = DummyRequest()

assert_type(stub.UnaryUnary(req), DummyReply)

for resp in stub.UnaryStream(req):
    assert_type(resp, DummyReply)

assert_type(stub.StreamUnary(iter([req])), DummyReply)

for resp in stub.StreamStream(iter([req])):
    assert_type(resp, DummyReply)
