from collections.abc import Sequence

from google.auth.credentials import Credentials as Credentials
from google.auth.transport import Request as _Request

def load_credentials_from_file(
    filename: str, scopes: Sequence[str] | None = None, quota_project_id: str | None = None
) -> tuple[Credentials, str | None]: ...
def default_async(
    scopes: Sequence[str] | None = None, request: _Request | None = None, quota_project_id: str | None = None
) -> tuple[Credentials, str | None]: ...
