from typing import Any, Iterable

def encode(
    claims: dict[str, Any],
    key: str,
    algorithm: str = ...,
    headers: dict[str, Any] | None = ...,
    access_token: str | None = ...,
) -> str: ...
def decode(
    token: str,
    key: str | dict[str, Any],
    algorithms: str | list[str] | None = ...,
    options: dict[str, Any] | None = ...,
    audience: str | None = ...,
    issuer: str | Iterable[str] | None = ...,
    subject: str | None = ...,
    access_token: str | None = ...,
) -> dict[str, Any]: ...
def get_unverified_header(token: str) -> dict[str, Any]: ...
def get_unverified_headers(token: str) -> dict[str, Any]: ...
def get_unverified_claims(token: str) -> dict[str, Any]: ...
