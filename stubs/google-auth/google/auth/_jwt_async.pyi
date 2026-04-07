from collections.abc import Mapping
from typing import Any

from google.auth import _credentials_async, jwt
from google.auth.credentials import Signing
from google.auth.crypt import Signer as _Signer
from google.auth.transport import Request as _Request

_DEFAULT_TOKEN_LIFETIME_SECS: int
_DEFAULT_MAX_CACHE_SIZE: int
_ALGORITHM_TO_VERIFIER_CLASS: dict[str, type]
_CRYPTOGRAPHY_BASED_ALGORITHMS: frozenset[str]

def encode(
    signer: _Signer, payload: Mapping[str, str], header: Mapping[str, str] | None = None, key_id: str | None = None
) -> bytes: ...
def _decode_jwt_segment(encoded_section: bytes) -> Mapping[str, Any]: ...
def _unverified_decode(token: str | bytes) -> tuple[Mapping[str, Any], Mapping[str, Any], bytes, bytes]: ...
def decode_header(token: str | bytes) -> Mapping[str, Any]: ...
def _verify_iat_and_exp(payload: Mapping[str, str], clock_skew_in_seconds: int = 0) -> None: ...
def decode(
    token: str,
    certs: str | bytes | Mapping[str, str | bytes] | None = None,
    verify: bool = True,
    audience: str | list[str] | None = None,
    clock_skew_in_seconds: int = 0,
) -> Mapping[str, Any]: ...

class Credentials(jwt.Credentials, _credentials_async.Credentials):
    expiry: Any

    def __init__(
        self,
        signer: _Signer,
        issuer: str,
        subject: str,
        audience: str,
        additional_claims: Mapping[str, str] | None = None,
        token_lifetime: int = ...,
        quota_project_id: str | None = None,
    ) -> None: ...
    @classmethod
    def _from_signer_and_info(cls, signer: _Signer, info: Mapping[str, str], **kwargs: Any) -> Credentials: ...
    @classmethod
    def from_service_account_info(cls, info: Mapping[str, str], **kwargs: Any) -> Credentials: ...
    @classmethod
    def from_service_account_file(cls, filename: str, **kwargs: Any) -> Credentials: ...
    @classmethod
    def from_signing_credentials(cls, credentials: Signing, audience: str, **kwargs: Any) -> Credentials: ...
    def with_claims(
        self,
        issuer: str | None = None,
        subject: str | None = None,
        audience: str | None = None,
        additional_claims: Mapping[str, str] | None = None,
    ) -> Credentials: ...
    def with_quota_project(self, quota_project_id: str | None) -> Credentials: ...
    def refresh(self, request: Any) -> None: ...
    def sign_bytes(self, message: bytes) -> bytes: ...
    @property
    def signer_email(self) -> str: ...
    @property
    def signer(self) -> _Signer: ...
    @property
    def additional_claims(self) -> Mapping[str, str]: ...

class OnDemandCredentials(jwt.OnDemandCredentials, _credentials_async.Credentials):
    async def before_request(self, request: _Request, method: str, url: str, headers: Mapping[str, str]) -> None: ...
