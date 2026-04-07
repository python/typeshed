from collections.abc import Mapping, Sequence
from typing import Any

from google.auth.api_key import Credentials as _ApiKeyCredentials
from google.auth.credentials import Credentials as Credentials
from google.auth.transport import Request as Request

def load_credentials_from_file(
    filename: str,
    scopes: Sequence[str] | None = None,
    default_scopes: Sequence[str] | None = None,
    quota_project_id: str | None = None,
    request: Request | None = None,
) -> tuple[Credentials, str | None]: ...
def load_credentials_from_dict(
    info: Mapping[str, Any],
    scopes: Sequence[str] | None = None,
    default_scopes: Sequence[str] | None = None,
    quota_project_id: str | None = None,
    request: Request | None = None,
) -> tuple[Credentials, str | None]: ...
def get_api_key_credentials(key: str) -> _ApiKeyCredentials: ...
def default(
    scopes: Sequence[str] | None = None,
    request: Request | None = None,
    quota_project_id: str | None = None,
    default_scopes: Sequence[str] | None = None,
) -> tuple[Credentials, str | None]: ...
