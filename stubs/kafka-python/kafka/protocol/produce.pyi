import abc
from _typeshed import Incomplete

from kafka.protocol.api import Request, Response

class ProduceResponse_v0(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v1(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v2(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v3(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v4(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v5(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v6(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v7(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceResponse_v8(Response):
    API_KEY: int
    API_VERSION: int
    SCHEMA: Incomplete

class ProduceRequest(Request, metaclass=abc.ABCMeta):
    API_KEY: int
    def expect_response(self): ...

class ProduceRequest_v0(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v0
    SCHEMA: Incomplete

class ProduceRequest_v1(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v1
    SCHEMA: Incomplete

class ProduceRequest_v2(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v2
    SCHEMA: Incomplete

class ProduceRequest_v3(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v3
    SCHEMA: Incomplete

class ProduceRequest_v4(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v4
    SCHEMA: Incomplete

class ProduceRequest_v5(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v5
    SCHEMA: Incomplete

class ProduceRequest_v6(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v6
    SCHEMA: Incomplete

class ProduceRequest_v7(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v7
    SCHEMA: Incomplete

class ProduceRequest_v8(ProduceRequest):
    API_VERSION: int
    RESPONSE_TYPE = ProduceResponse_v8
    SCHEMA: Incomplete

ProduceResponse: Incomplete
