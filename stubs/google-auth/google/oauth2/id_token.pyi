from collections.abc import Mapping, Sequence
from typing import Any

from google.auth import credentials as _credentials, transport as transport

def verify_token(
    id_token: str | bytes,
    request: transport.Request,
    audience: str | Sequence[str] | None = None,
    certs_url: str = "https://www.googleapis.com/oauth2/v1/certs",
    clock_skew_in_seconds: int = 0,
) -> Mapping[str, Any]: ...
def verify_oauth2_token(
    id_token: str | bytes, request: transport.Request, audience: str | Sequence[str] | None = None, clock_skew_in_seconds: int = 0
) -> Mapping[str, Any]: ...
def verify_firebase_token(
    id_token: str | bytes, request: transport.Request, audience: str | Sequence[str] | None = None, clock_skew_in_seconds: int = 0
) -> Mapping[str, Any]: ...
def fetch_id_token_credentials(audience: str, request: transport.Request | None = None) -> _credentials.Credentials: ...
def fetch_id_token(request: transport.Request, audience: str) -> str: ...
