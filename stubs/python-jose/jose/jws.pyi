from typing import Any

def sign(
    payload: str | dict[str, Any], key: str | dict[str, Any], headers: dict[str, Any] | None = ..., algorithm: str = ...
) -> str: ...
def verify(token: str, key: str | dict[str, Any], algorithms: str | list[str], verify: bool = ...) -> str: ...
def get_unverified_header(token: str) -> dict[str, Any]: ...
def get_unverified_headers(token: str) -> dict[str, Any]: ...
def get_unverified_claims(token: str) -> dict[str, Any]: ...
