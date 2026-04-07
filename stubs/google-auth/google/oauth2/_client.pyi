import datetime
from collections.abc import Mapping, Sequence

from google.auth.transport import Request

def jwt_grant(
    request: Request, token_uri: str, assertion: str, can_retry: bool = True
) -> tuple[str, datetime.datetime | None, Mapping[str, str]]: ...
def call_iam_generate_id_token_endpoint(
    request: Request, iam_id_token_endpoint: str, signer_email: str, audience: str, access_token: str, universe_domain: str = ...
) -> tuple[str, datetime.datetime]: ...
def id_token_jwt_grant(
    request: Request, token_uri: str, assertion: str, can_retry: bool = True
) -> tuple[str, datetime.datetime | None, Mapping[str, str]]: ...
def refresh_grant(
    request: Request,
    token_uri: str,
    refresh_token: str,
    client_id: str,
    client_secret: str,
    scopes: Sequence[str] | None = None,
    rapt_token: str | None = None,
    can_retry: bool = True,
) -> tuple[str, str, datetime.datetime | None, Mapping[str, str]]: ...
