from typing import Any

def create_client_assertion_jwt(
    domain: str, client_id: str, client_assertion_signing_key: str, client_assertion_signing_alg: str | None
) -> str: ...
def add_client_authentication(
    payload: dict[str, Any],
    domain: str,
    client_id: str,
    client_secret: str | None,
    client_assertion_signing_key: str | None,
    client_assertion_signing_alg: str | None,
) -> dict[str, Any]: ...
