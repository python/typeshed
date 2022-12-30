from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any, NamedTuple
from typing_extensions import TypeAlias

from influxdb_client.client._base import _BaseWriteApi
from influxdb_client.client.write.point import Point
from influxdb_client.client.write_api import PointSettings
from influxdb_client.domain.write_precision import _WritePrecision

_DataClass: TypeAlias = Any  # any dataclass

logger: Incomplete

class WriteApiAsync(_BaseWriteApi):
    def __init__(self, influxdb_client, point_settings: PointSettings = ...) -> None: ...
    async def write(
        self,
        bucket: str,
        org: str | None = ...,
        record: str
        | Iterable[str]
        | Point
        | Iterable[Point]
        | dict[Incomplete, Incomplete]
        | Iterable[dict[Incomplete, Incomplete]]
        | bytes
        | Iterable[bytes]
        | NamedTuple
        | Iterable[NamedTuple]
        | _DataClass
        | Iterable[_DataClass] = ...,
        write_precision: _WritePrecision = ...,
        **kwargs,
    ) -> bool: ...
