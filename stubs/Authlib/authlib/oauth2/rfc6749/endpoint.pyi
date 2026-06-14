from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any

from .requests import OAuth2Request

@dataclass
class EndpointRequest:
    request: OAuth2Request
    client: Any = None

class Endpoint:
    ENDPOINT_NAME: str | None
    server: Incomplete
    def __init__(self, server=None) -> None: ...
    def create_endpoint_request(self, request): ...
    def validate_request(self, request: OAuth2Request) -> EndpointRequest: ...
    def create_response(self, validated_request: EndpointRequest) -> tuple[int, Any, list[Incomplete]] | None: ...
    def create_endpoint_response(self, request: OAuth2Request) -> tuple[int, Any, list[Incomplete]] | None: ...
    def __call__(self, request: OAuth2Request) -> tuple[int, Any, list[Incomplete]] | None: ...
