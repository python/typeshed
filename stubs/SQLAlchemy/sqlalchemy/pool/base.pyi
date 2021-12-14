from typing import Any

from .. import log

reset_rollback: Any
reset_commit: Any
reset_none: Any

class _ConnDialect:
    is_async: bool
    def do_rollback(self, dbapi_connection) -> None: ...
    def do_commit(self, dbapi_connection) -> None: ...
    def do_close(self, dbapi_connection) -> None: ...
    def do_ping(self, dbapi_connection) -> None: ...
    def get_driver_connection(self, connection): ...

class _AsyncConnDialect(_ConnDialect):
    is_async: bool

class Pool(log.Identified):
    logging_name: Any
    echo: Any
    def __init__(
        self,
        creator,
        recycle: int = ...,
        echo: Any | None = ...,
        logging_name: Any | None = ...,
        reset_on_return: bool = ...,
        events: Any | None = ...,
        dialect: Any | None = ...,
        pre_ping: bool = ...,
        _dispatch: Any | None = ...,
    ) -> None: ...
    def recreate(self) -> None: ...
    def dispose(self) -> None: ...
    def connect(self): ...
    def status(self) -> None: ...

class _ConnectionRecord:
    finalize_callback: Any
    def __init__(self, pool, connect: bool = ...) -> None: ...
    fresh: bool
    fairy_ref: Any
    starttime: Any
    dbapi_connection: Any
    @property
    def driver_connection(self): ...
    @property
    def connection(self): ...
    @connection.setter
    def connection(self, value) -> None: ...
    def info(self): ...
    def record_info(self): ...
    @classmethod
    def checkout(cls, pool): ...
    def checkin(self, _fairy_was_created: bool = ...) -> None: ...
    @property
    def in_use(self): ...
    @property
    def last_connect_time(self): ...
    def close(self) -> None: ...
    def invalidate(self, e: Any | None = ..., soft: bool = ...) -> None: ...
    def get_connection(self): ...

class _ConnectionFairy:
    dbapi_connection: Any
    def __init__(self, dbapi_connection, connection_record, echo) -> None: ...
    @property
    def driver_connection(self): ...
    @property
    def connection(self): ...
    @connection.setter
    def connection(self, value) -> None: ...
    @property
    def is_valid(self): ...
    def info(self): ...
    @property
    def record_info(self): ...
    def invalidate(self, e: Any | None = ..., soft: bool = ...) -> None: ...
    def cursor(self, *args, **kwargs): ...
    def __getattr__(self, key): ...
    def detach(self) -> None: ...
    def close(self) -> None: ...
