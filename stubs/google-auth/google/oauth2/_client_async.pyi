from collections.abc import Mapping, Sequence
from datetime import datetime

from google.auth.transport import Request

async def jwt_grant(
    request: Request, token_uri: str, assertion: str, can_retry: bool = True
) -> tuple[str, datetime | None, Mapping[str, str]]: ...
async def id_token_jwt_grant(
    request: Request, token_uri: str, assertion: str, can_retry: bool = True
) -> tuple[str, datetime | None, Mapping[str, str]]: ...
async def refresh_grant(
    request: Request,
    token_uri: str,
    refresh_token: str,
    client_id: str,
    client_secret: str,
    scopes: Sequence[str] | None = None,
    rapt_token: str | None = None,
    can_retry: bool = True,
) -> tuple[str, str | None, datetime | None, Mapping[str, str]]: ...
