from collections.abc import Callable, Iterable, Mapping, Sequence
from datetime import timedelta
from typing import Any, Generic, TypeVar, Union, overload
from typing_extensions import Literal

from ..client import _Key, _Value

_ScoreCastFuncReturn = TypeVar("_ScoreCastFuncReturn")
_StrType = TypeVar("_StrType", bound=Union[str, bytes])

class CoreCommands(Generic[_StrType]):
    def acl_cat(self, category: str | None = ...) -> list[str]: ...
    def acl_deluser(self, username: str) -> int: ...
    def acl_genpass(self, bits: int | None = ...) -> str: ...
    def acl_getuser(self, username: str) -> Any | None: ...
    def acl_list(self) -> list[str]: ...
    def acl_load(self) -> bool: ...
    def acl_setuser(
        self,
        username: str,
        enabled: bool = ...,
        nopass: bool = ...,
        passwords: Sequence[str] | None = ...,
        hashed_passwords: Sequence[str] | None = ...,
        categories: Sequence[str] | None = ...,
        commands: Sequence[str] | None = ...,
        keys: Sequence[str] | None = ...,
        reset: bool = ...,
        reset_keys: bool = ...,
        reset_passwords: bool = ...,
    ) -> bool: ...
    def acl_users(self) -> list[str]: ...
    def acl_whoami(self) -> str: ...
    def append(self, key, value): ...
    def bitcount(self, key: _Key, start: int | None = ..., end: int | None = ...) -> int: ...
    def bitop(self, operation, dest, *keys): ...
    def bitpos(self, key, bit, start=..., end=...): ...
    def bgrewriteaof(self): ...
    def bgsave(self, schedule: bool = ...): ...
    def client_id(self) -> int: ...
    def client_kill(self, address: str) -> bool: ...
    def client_list(self, _type: str | None = ..., client_id: list[str] = ...) -> list[dict[str, str]]: ...
    def client_getname(self) -> str | None: ...
    def client_setname(self, name: str) -> bool: ...
    def flushall(self, asynchronous: bool = ...) -> bool: ...
    def flushdb(self, asynchronous: bool = ...) -> bool: ...
    def lindex(self, name: _Key, index: int) -> _StrType | None: ...
    def linsert(
        self, name: _Key, where: Literal["BEFORE", "AFTER", "before", "after"], refvalue: _Value, value: _Value
    ) -> int: ...
    def llen(self, name: _Key) -> int: ...
    def lmove(
        self, first_list: _Key, second_list: _Key, src: Literal["LEFT", "RIGHT"] = ..., dest: Literal["LEFT", "RIGHT"] = ...
    ) -> _Value: ...
    def blmove(
        self,
        first_list: _Key,
        second_list: _Key,
        timeout: float,
        src: Literal["LEFT", "RIGHT"] = ...,
        dest: Literal["LEFT", "RIGHT"] = ...,
    ) -> _Value | None: ...
    def lpop(self, name, count: int | None = ...): ...
    def lpush(self, name: _Value, *values: _Value) -> int: ...
    def lpushx(self, name, value): ...
    def lrange(self, name: _Key, start: int, end: int) -> list[_StrType]: ...
    def lrem(self, name: _Key, count: int, value: _Value) -> int: ...
    def lset(self, name: _Key, index: int, value: _Value) -> bool: ...
    def ltrim(self, name: _Key, start: int, end: int) -> bool: ...
    def randomkey(self): ...
    def rename(self, src, dst): ...
    def renamenx(self, src, dst): ...
    def restore(
        self, name, ttl, value, replace: bool = ..., absttl: bool = ..., idletime: Any | None = ..., frequency: Any | None = ...
    ): ...
    def rpop(self, name, count: int | None = ...): ...
    def rpoplpush(self, src, dst): ...
    def rpush(self, name: _Value, *values: _Value) -> int: ...
    def rpushx(self, name, value): ...
    def set(
        self,
        name: _Key,
        value: _Value,
        ex: None | int | timedelta = ...,
        px: None | int | timedelta = ...,
        nx: bool = ...,
        xx: bool = ...,
        keepttl: bool = ...,
        get: bool = ...,
        exat: Any | None = ...,
        pxat: Any | None = ...,
    ) -> bool | None: ...
    def xack(self, name, groupname, *ids): ...
    def xadd(
        self,
        name,
        fields,
        id: str = ...,
        maxlen=...,
        approximate: bool = ...,
        nomkstream: bool = ...,
        minid: Any | None = ...,
        limit: Any | None = ...,
    ): ...
    def xclaim(
        self, name, groupname, consumername, min_idle_time, message_ids, idle=..., time=..., retrycount=..., force=..., justid=...
    ): ...
    def xdel(self, name, *ids): ...
    def xgroup_create(self, name, groupname, id=..., mkstream=...): ...
    def xgroup_delconsumer(self, name, groupname, consumername): ...
    def xgroup_destroy(self, name, groupname): ...
    def xgroup_setid(self, name, groupname, id): ...
    def xinfo_consumers(self, name, groupname): ...
    def xinfo_groups(self, name): ...
    def xinfo_stream(self, name, full: bool = ...): ...
    def xlen(self, name: _Key) -> int: ...
    def xpending(self, name, groupname): ...
    def xpending_range(
        self,
        name,
        groupname,
        idle: Any | None = ...,
        min: Any | None = ...,
        max: Any | None = ...,
        count: int | None = ...,
        consumername: Any | None = ...,
    ): ...
    def xrange(self, name, min=..., max=..., count=...): ...
    def xread(self, streams, count=..., block=...): ...
    def xreadgroup(self, groupname, consumername, streams, count=..., block=..., noack=...): ...
    def xrevrange(self, name, max=..., min=..., count=...): ...
    def xtrim(
        self, name, maxlen: Any | None = ..., approximate: bool = ..., minid: Any | None = ..., limit: Any | None = ...
    ): ...
    def zadd(
        self,
        name: _Key,
        mapping: Mapping[_Key, _Value],
        nx: bool = ...,
        xx: bool = ...,
        ch: bool = ...,
        incr: bool = ...,
        gt: Any | None = ...,
        lt: Any | None = ...,
    ) -> int: ...
    def zcard(self, name: _Key) -> int: ...
    def zcount(self, name: _Key, min: _Value, max: _Value) -> int: ...
    def zincrby(self, name: _Key, amount: float, value: _Value) -> float: ...
    def zinterstore(self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = ...) -> int: ...
    def zlexcount(self, name: _Key, min: _Value, max: _Value) -> int: ...
    def zpopmax(self, name: _Key, count: int | None = ...) -> list[_StrType]: ...
    def zpopmin(self, name: _Key, count: int | None = ...) -> list[_StrType]: ...
    @overload
    def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: Literal[0] = ...) -> tuple[_StrType, _StrType, float]: ...
    @overload
    def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: float) -> tuple[_StrType, _StrType, float] | None: ...
    @overload
    def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: Literal[0] = ...) -> tuple[_StrType, _StrType, float]: ...
    @overload
    def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: float) -> tuple[_StrType, _StrType, float] | None: ...
    @overload
    def zrange(
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = ...,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[float], _ScoreCastFuncReturn] = ...,
        byscore: bool = ...,
        bylex: bool = ...,
        offset: int | None = ...,
        num: int | None = ...,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]: ...
    @overload
    def zrange(
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = ...,
        withscores: bool = ...,
        score_cast_func: Callable[[Any], Any] = ...,
        byscore: bool = ...,
        bylex: bool = ...,
        offset: int | None = ...,
        num: int | None = ...,
    ) -> list[_StrType]: ...
    def zrangebylex(
        self, name: _Key, min: _Value, max: _Value, start: int | None = ..., num: int | None = ...
    ) -> list[_StrType]: ...
    @overload
    def zrangebyscore(
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = ...,
        num: int | None = ...,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[float], _ScoreCastFuncReturn] = ...,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]: ...
    @overload
    def zrangebyscore(
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = ...,
        num: int | None = ...,
        withscores: bool = ...,
        score_cast_func: Callable[[Any], Any] = ...,
    ) -> list[_StrType]: ...
    def zrank(self, name: _Key, value: _Value) -> int | None: ...
    def zrem(self, name: _Key, *values: _Value) -> int: ...
    def zremrangebylex(self, name: _Key, min: _Value, max: _Value) -> int: ...
    def zremrangebyrank(self, name: _Key, min: int, max: int) -> int: ...
    def zremrangebyscore(self, name: _Key, min: _Value, max: _Value) -> int: ...
    @overload
    def zrevrange(
        self,
        name: _Key,
        start: int,
        end: int,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[float], _ScoreCastFuncReturn] = ...,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]: ...
    @overload
    def zrevrange(
        self, name: _Key, start: int, end: int, withscores: bool = ..., score_cast_func: Callable[[Any], Any] = ...
    ) -> list[_StrType]: ...
    @overload
    def zrevrangebyscore(
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = ...,
        num: int | None = ...,
        *,
        withscores: Literal[True],
        score_cast_func: Callable[[float], _ScoreCastFuncReturn] = ...,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]: ...
    @overload
    def zrevrangebyscore(
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = ...,
        num: int | None = ...,
        withscores: bool = ...,
        score_cast_func: Callable[[Any], Any] = ...,
    ) -> list[_StrType]: ...
    def zrevrangebylex(
        self, name: _Key, max: _Value, min: _Value, start: int | None = ..., num: int | None = ...
    ) -> list[_StrType]: ...
    def zrevrank(self, name: _Key, value: _Value) -> int | None: ...
    def zscore(self, name: _Key, value: _Value) -> float | None: ...
    def zunionstore(self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = ...) -> int: ...
    def script_exists(self, *args): ...
    def script_flush(self, sync_type: Any | None = ...): ...
    def script_kill(self): ...
    def script_load(self, script): ...
    def register_script(self, script: str | _StrType) -> Script: ...

class Script:
    def __init__(self, registered_client, script) -> None: ...
    def __call__(self, keys=..., args=..., client: Any | None = ...): ...

class BitFieldOperation:
    def __init__(self, client, key, default_overflow: Any | None = ...): ...
    def reset(self) -> None: ...
    def overflow(self, overflow): ...
    def incrby(self, fmt, offset, increment, overflow: Any | None = ...): ...
    def get(self, fmt, offset): ...
    def set(self, fmt, offset, value): ...
    @property
    def command(self): ...
    def execute(self): ...
