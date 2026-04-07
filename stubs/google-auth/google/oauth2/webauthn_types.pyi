from dataclasses import dataclass

@dataclass(frozen=True)
class PublicKeyCredentialDescriptor:
    id: str
    transports: list[str] | None = None

    def to_dict(self) -> dict[str, object]: ...

@dataclass
class AuthenticationExtensionsClientInputs:
    appid: str | None = None

    def to_dict(self) -> dict[str, object]: ...

@dataclass
class GetRequest:
    origin: str
    rpid: str
    challenge: str
    timeout_ms: int | None = None
    allow_credentials: list[PublicKeyCredentialDescriptor] | None = None
    user_verification: str | None = None
    extensions: AuthenticationExtensionsClientInputs | None = None

    def to_json(self) -> str: ...

@dataclass(frozen=True)
class AuthenticatorAssertionResponse:
    client_data_json: str
    authenticator_data: str
    signature: str
    user_handle: str | None = None

@dataclass(frozen=True)
class GetResponse:
    id: str
    response: AuthenticatorAssertionResponse
    authenticator_attachment: str | None = None
    client_extension_results: dict[str, object] | None = None

    @staticmethod
    def from_json(json_str: str) -> GetResponse: ...
