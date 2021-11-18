from redis.exceptions import DataError as DataError
from typing import Any

ADD_CMD: str
ALTER_CMD: str
CREATERULE_CMD: str
CREATE_CMD: str
DECRBY_CMD: str
DELETERULE_CMD: str
DEL_CMD: str
GET_CMD: str
INCRBY_CMD: str
INFO_CMD: str
MADD_CMD: str
MGET_CMD: str
MRANGE_CMD: str
MREVRANGE_CMD: str
QUERYINDEX_CMD: str
RANGE_CMD: str
REVRANGE_CMD: str

class TimeSeriesCommands:
    def create(self, key, **kwargs): ...
    def alter(self, key, **kwargs): ...
    def add(self, key, timestamp, value, **kwargs): ...
    def madd(self, ktv_tuples): ...
    def incrby(self, key, value, **kwargs): ...
    def decrby(self, key, value, **kwargs): ...
    def delete(self, key, from_time, to_time): ...
    def createrule(self, source_key, dest_key, aggregation_type, bucket_size_msec): ...
    def deleterule(self, source_key, dest_key): ...
    def range(
        self,
        key,
        from_time,
        to_time,
        count: Any | None = ...,
        aggregation_type: Any | None = ...,
        bucket_size_msec: int = ...,
        filter_by_ts: Any | None = ...,
        filter_by_min_value: Any | None = ...,
        filter_by_max_value: Any | None = ...,
        align: Any | None = ...,
    ): ...
    def revrange(
        self,
        key,
        from_time,
        to_time,
        count: Any | None = ...,
        aggregation_type: Any | None = ...,
        bucket_size_msec: int = ...,
        filter_by_ts: Any | None = ...,
        filter_by_min_value: Any | None = ...,
        filter_by_max_value: Any | None = ...,
        align: Any | None = ...,
    ): ...
    def mrange(
        self,
        from_time,
        to_time,
        filters,
        count: Any | None = ...,
        aggregation_type: Any | None = ...,
        bucket_size_msec: int = ...,
        with_labels: bool = ...,
        filter_by_ts: Any | None = ...,
        filter_by_min_value: Any | None = ...,
        filter_by_max_value: Any | None = ...,
        groupby: Any | None = ...,
        reduce: Any | None = ...,
        select_labels: Any | None = ...,
        align: Any | None = ...,
    ): ...
    def mrevrange(
        self,
        from_time,
        to_time,
        filters,
        count: Any | None = ...,
        aggregation_type: Any | None = ...,
        bucket_size_msec: int = ...,
        with_labels: bool = ...,
        filter_by_ts: Any | None = ...,
        filter_by_min_value: Any | None = ...,
        filter_by_max_value: Any | None = ...,
        groupby: Any | None = ...,
        reduce: Any | None = ...,
        select_labels: Any | None = ...,
        align: Any | None = ...,
    ): ...
    def get(self, key): ...
    def mget(self, filters, with_labels: bool = ...): ...
    def info(self, key): ...
    def queryindex(self, filters): ...
