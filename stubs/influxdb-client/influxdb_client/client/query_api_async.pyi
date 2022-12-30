from _typeshed import Incomplete
from typing import AsyncGenerator

from influxdb_client.client._base import _BaseQueryApi
from influxdb_client.client.flux_table import FluxRecord, TableList

class QueryApiAsync(_BaseQueryApi):
    def __init__(self, influxdb_client, query_options=...) -> None: ...
    async def query(self, query: str, org: Incomplete | None = ..., params: dict[Incomplete, Incomplete] = ...) -> TableList: ...
    async def query_stream(
        self, query: str, org: Incomplete | None = ..., params: dict[Incomplete, Incomplete] = ...
    ) -> AsyncGenerator["FluxRecord", None]: ...
    async def query_data_frame(
        self,
        query: str,
        org: Incomplete | None = ...,
        data_frame_index: list[str] = ...,
        params: dict[Incomplete, Incomplete] = ...,
    ): ...
    async def query_data_frame_stream(
        self,
        query: str,
        org: Incomplete | None = ...,
        data_frame_index: list[str] = ...,
        params: dict[Incomplete, Incomplete] = ...,
    ): ...
    async def query_raw(
        self, query: str, org: Incomplete | None = ..., dialect=..., params: dict[Incomplete, Incomplete] = ...
    ): ...
