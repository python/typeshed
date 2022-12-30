from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Iterable, NamedTuple, Union

from influxdb_client import Point, WritePrecision
from influxdb_client.client._base import _BaseWriteApi
from influxdb_client.client.write_api import PointSettings

logger: Incomplete

class WriteApiAsync(_BaseWriteApi):
    def __init__(self, influxdb_client, point_settings: PointSettings = ...) -> None: ...
    async def write(
        self,
        bucket: str,
        org: str = ...,
        record: Union[
            str,
            Iterable["str"],
            Point,
            Iterable["Point"],
            dict,
            Iterable["dict"],
            bytes,
            Iterable["bytes"],
            NamedTuple,
            Iterable["NamedTuple"],
            "dataclass",
            Iterable["dataclass"],
        ] = ...,
        write_precision: WritePrecision = ...,
        **kwargs,
    ) -> bool: ...
