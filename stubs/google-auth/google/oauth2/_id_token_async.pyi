from collections.abc import Mapping, Sequence
from typing import Any

from google.auth.transport import Request as _Request

async def verify_token(
    id_token: str | bytes,
    request: _Request,
    audience: str | Sequence[str] | None = None,
    certs_url: str = "https://www.googleapis.com/oauth2/v1/certs",
    clock_skew_in_seconds: int = 0,
) -> Mapping[str, Any]: ...
async def verify_oauth2_token(
    id_token: str | bytes, request: _Request, audience: str | Sequence[str] | None = None, clock_skew_in_seconds: int = 0
) -> Mapping[str, Any]: ...
async def verify_firebase_token(
    id_token: str | bytes, request: _Request, audience: str | Sequence[str] | None = None, clock_skew_in_seconds: int = 0
) -> Mapping[str, Any]: ...
async def fetch_id_token(request: _Request, audience: str) -> str: ...
