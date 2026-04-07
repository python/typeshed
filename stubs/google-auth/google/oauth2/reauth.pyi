import datetime
from collections.abc import Mapping, Sequence

from google.auth.transport import Request as _Request

RUN_CHALLENGE_RETRY_LIMIT: int

def is_interactive() -> bool: ...
def get_rapt_token(
    request: _Request, client_id: str, client_secret: str, refresh_token: str, token_uri: str, scopes: Sequence[str] | None = None
) -> str: ...
def refresh_grant(
    request: _Request,
    token_uri: str,
    refresh_token: str,
    client_id: str,
    client_secret: str,
    scopes: Sequence[str] | None = None,
    rapt_token: str | None = None,
    enable_reauth_refresh: bool = False,
) -> tuple[str, str | None, datetime.datetime | None, Mapping[str, str], str]: ...
