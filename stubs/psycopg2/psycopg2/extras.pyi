from collections import OrderedDict
from typing import Any, Iterator, NamedTuple

from psycopg2._ipaddress import register_ipaddress as register_ipaddress
from psycopg2._json import (
    Json as Json,
    register_default_json as register_default_json,
    register_default_jsonb as register_default_jsonb,
    register_json as register_json,
)
from psycopg2._psycopg import (
    REPLICATION_LOGICAL as REPLICATION_LOGICAL,
    REPLICATION_PHYSICAL as REPLICATION_PHYSICAL,
    ReplicationConnection as _replicationConnection,
    ReplicationCursor as _replicationCursor,
    ReplicationMessage as ReplicationMessage,
)
from psycopg2._range import (
    DateRange as DateRange,
    DateTimeRange as DateTimeRange,
    DateTimeTZRange as DateTimeTZRange,
    NumericRange as NumericRange,
    Range as Range,
    RangeAdapter as RangeAdapter,
    RangeCaster as RangeCaster,
    register_range as register_range,
)

from .extensions import connection as _connection, cursor as _cursor, quote_ident as quote_ident

class DictCursorBase(_cursor):
    row_factory: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def fetchone(self) -> tuple[Any, ...] | None: ...
    def fetchmany(self, size: int | None = ...) -> list[tuple[Any, ...]]: ...
    def fetchall(self) -> list[tuple[Any, ...]]: ...
    def __iter__(self) -> Iterator[tuple[Any, ...]]: ...

class DictConnection(_connection):
    def cursor(self, *args, **kwargs) -> DictCursor: ...

class DictCursor(DictCursorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    index: Any
    def execute(self, query, vars: Any | None = ...): ...
    def callproc(self, procname, vars: Any | None = ...): ...
    def fetchone(self) -> DictRow | None: ...
    def fetchmany(self, size: int | None = ...) -> list[DictRow]: ...
    def fetchall(self) -> list[DictRow]: ...
    def __iter__(self) -> Iterator[DictRow]: ...

class DictRow(list[Any]):
    def __init__(self, cursor) -> None: ...
    def __getitem__(self, x): ...
    def __setitem__(self, x, v) -> None: ...
    def items(self): ...
    def keys(self): ...
    def values(self): ...
    def get(self, x, default: Any | None = ...): ...
    def copy(self): ...
    def __contains__(self, x): ...
    def __reduce__(self): ...

class RealDictConnection(_connection):
    def cursor(self, *args, **kwargs) -> RealDictCursor: ...

class RealDictCursor(DictCursorBase):
    def __init__(self, *args, **kwargs) -> None: ...
    column_mapping: Any
    def execute(self, query, vars: Any | None = ...): ...
    def callproc(self, procname, vars: Any | None = ...): ...
    def fetchone(self) -> RealDictRow | None: ...
    def fetchmany(self, size: int | None = ...) -> list[RealDictRow]: ...
    def fetchall(self) -> list[RealDictRow]: ...
    def __iter__(self) -> Iterator[RealDictRow]: ...

class RealDictRow(OrderedDict[Any, Any]):
    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...

class NamedTupleConnection(_connection):
    def cursor(self, *args, **kwargs) -> NamedTupleCursor: ...

class NamedTupleCursor(_cursor):
    Record: Any
    MAX_CACHE: int
    def execute(self, query, vars: Any | None = ...): ...
    def executemany(self, query, vars): ...
    def callproc(self, procname, vars: Any | None = ...): ...
    def fetchone(self) -> NamedTuple | None: ...
    def fetchmany(self, size: int | None = ...) -> list[NamedTuple]: ...
    def fetchall(self) -> list[NamedTuple]: ...
    def __iter__(self) -> Iterator[NamedTuple]: ...

class LoggingConnection(_connection):
    log: Any
    def initialize(self, logobj) -> None: ...
    def filter(self, msg, curs): ...
    def cursor(self, *args, **kwargs): ...

class LoggingCursor(_cursor):
    def execute(self, query, vars: Any | None = ...): ...
    def callproc(self, procname, vars: Any | None = ...): ...

class MinTimeLoggingConnection(LoggingConnection):
    def initialize(self, logobj, mintime: int = ...) -> None: ...
    def filter(self, msg, curs): ...
    def cursor(self, *args, **kwargs): ...

class MinTimeLoggingCursor(LoggingCursor):
    timestamp: Any
    def execute(self, query, vars: Any | None = ...): ...
    def callproc(self, procname, vars: Any | None = ...): ...

class LogicalReplicationConnection(_replicationConnection):
    def __init__(self, *args, **kwargs) -> None: ...

class PhysicalReplicationConnection(_replicationConnection):
    def __init__(self, *args, **kwargs) -> None: ...

class StopReplication(Exception): ...

class ReplicationCursor(_replicationCursor):
    def create_replication_slot(self, slot_name, slot_type: Any | None = ..., output_plugin: Any | None = ...) -> None: ...
    def drop_replication_slot(self, slot_name) -> None: ...
    def start_replication(
        self,
        slot_name: Any | None = ...,
        slot_type: Any | None = ...,
        start_lsn: int = ...,
        timeline: int = ...,
        options: Any | None = ...,
        decode: bool = ...,
        status_interval: int = ...,
    ) -> None: ...
    def fileno(self): ...

class UUID_adapter:
    def __init__(self, uuid) -> None: ...
    def __conform__(self, proto): ...
    def getquoted(self): ...

def register_uuid(oids: Any | None = ..., conn_or_curs: Any | None = ...): ...

class Inet:
    addr: Any
    def __init__(self, addr) -> None: ...
    def prepare(self, conn) -> None: ...
    def getquoted(self): ...
    def __conform__(self, proto): ...

def register_inet(oid: Any | None = ..., conn_or_curs: Any | None = ...): ...
def wait_select(conn) -> None: ...

class HstoreAdapter:
    wrapped: Any
    def __init__(self, wrapped) -> None: ...
    conn: Any
    getquoted: Any
    def prepare(self, conn) -> None: ...
    @classmethod
    def parse(cls, s, cur, _bsdec=...): ...
    @classmethod
    def parse_unicode(cls, s, cur): ...
    @classmethod
    def get_oids(cls, conn_or_curs): ...

def register_hstore(
    conn_or_curs, globally: bool = ..., unicode: bool = ..., oid: Any | None = ..., array_oid: Any | None = ...
) -> None: ...

class CompositeCaster:
    name: Any
    schema: Any
    oid: Any
    array_oid: Any
    attnames: Any
    atttypes: Any
    typecaster: Any
    array_typecaster: Any
    def __init__(self, name, oid, attrs, array_oid: Any | None = ..., schema: Any | None = ...) -> None: ...
    def parse(self, s, curs): ...
    def make(self, values): ...
    @classmethod
    def tokenize(cls, s): ...

def register_composite(name, conn_or_curs, globally: bool = ..., factory: Any | None = ...): ...
def execute_batch(cur, sql, argslist, page_size: int = ...) -> None: ...
def execute_values(cur, sql, argslist, template: Any | None = ..., page_size: int = ..., fetch: bool = ...): ...
