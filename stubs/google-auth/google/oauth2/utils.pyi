import abc
import enum
from collections.abc import Mapping

class ClientAuthType(enum.Enum):
    basic = 1
    request_body = 2

class ClientAuthentication:
    client_auth_type: ClientAuthType
    client_id: str
    client_secret: str | None
    def __init__(self, client_auth_type: ClientAuthType, client_id: str, client_secret: str | None = None) -> None: ...

class OAuthClientAuthHandler(metaclass=abc.ABCMeta):
    def __init__(self, client_authentication: ClientAuthentication | None = None) -> None: ...
    def apply_client_authentication_options(
        self, headers: Mapping[str, str], request_body: Mapping[str, str] | None = None, bearer_token: str | None = None
    ) -> None: ...

def handle_error_response(response_body: str) -> None: ...
