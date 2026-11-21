from logging import Logger
from typing import ClassVar, Final, Literal

from authlib.oauth2.rfc6749 import BaseGrant, TokenEndpointMixin
from authlib.oauth2.rfc6750.token import _Token

log: Logger

DEVICE_CODE_GRANT_TYPE: Final[str]

class DeviceCodeGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE: ClassVar[str]
    TOKEN_ENDPOINT_AUTH_METHODS: ClassVar[list[str]]

    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> tuple[Literal[200], _Token, list[tuple[str, str]]]: ...
    def validate_device_credential(self, credential): ...
    def query_device_credential(self, device_code): ...
    def query_user_grant(self, user_code): ...
    def should_slow_down(self, credential): ...
