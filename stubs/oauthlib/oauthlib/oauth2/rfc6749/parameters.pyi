from _typeshed import Incomplete
from typing import Any

def prepare_grant_uri(
    uri,
    client_id,
    response_type,
    redirect_uri: Incomplete | None = ...,
    scope: Incomplete | None = ...,
    state: Incomplete | None = ...,
    code_challenge: str | None = ...,
    code_challenge_method: str | None = ...,
    **kwargs,
): ...
def prepare_token_request(
    grant_type, body: str = ..., include_client_id: bool = ..., code_verifier: str | None = ..., **kwargs
): ...
def prepare_token_revocation_request(
    url, token, token_type_hint: str = ..., callback: Incomplete | None = ..., body: str = ..., **kwargs
): ...
def parse_authorization_code_response(uri, state: Incomplete | None = ...): ...
def parse_implicit_response(uri, state: Incomplete | None = ..., scope: Incomplete | None = ...): ...
def parse_token_response(body, scope: Incomplete | None = ...): ...
def validate_token_parameters(params) -> None: ...