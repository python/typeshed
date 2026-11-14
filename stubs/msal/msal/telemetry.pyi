from _typeshed import Incomplete
from logging import Logger

logger: Logger
CLIENT_REQUEST_ID: str
CLIENT_CURRENT_TELEMETRY: str
CLIENT_LAST_TELEMETRY: str
NON_SILENT_CALL: int
FORCE_REFRESH: int
AT_ABSENT: int
AT_EXPIRED: int
AT_AGING: int
RESERVED: int

class _TelemetryContext:
    def __init__(self, buffer, lock, api_id, correlation_id=None, refresh_reason=None) -> None: ...
    def generate_headers(self) -> dict[str, str]: ...
    def hit_an_access_token(self) -> None: ...
    def update_telemetry(self, auth_result: Incomplete | None) -> None: ...
