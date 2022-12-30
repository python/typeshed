from datetime import datetime
from typing import Union

from influxdb_client import Organization
from influxdb_client.client._base import _BaseDeleteApi

class DeleteApiAsync(_BaseDeleteApi):
    def __init__(self, influxdb_client) -> None: ...
    async def delete(
        self,
        start: Union[str, datetime],
        stop: Union[str, datetime],
        predicate: str,
        bucket: str,
        org: Union[str, Organization, None] = ...,
    ) -> bool: ...
