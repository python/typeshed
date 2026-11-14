from _typeshed import Incomplete
from datetime import datetime
from logging import Logger

logger: Logger

def send_request(
    username: str, password: str, cloud_audience_urn: str, endpoint_address: str, soap_action: str | None, http_client, **kwargs
) -> dict[str, Incomplete]: ...
def escape_xml(s: str) -> str: ...
def wsu_time_format(datetime_obj: datetime) -> str: ...
