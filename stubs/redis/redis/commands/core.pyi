import builtins
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from datetime import datetime, timedelta
from typing import Any, Generic, TypeVar, Union, overload
from typing_extensions import Literal

from ..client import _Key, _Value

_ScoreCastFuncReturn = TypeVar("_ScoreCastFuncReturn")
_StrType = TypeVar("_StrType", bound=Union[str, bytes])

class ACLCommands(Generic[_StrType]):
    def acl_cat(self, category: str | None = ..., **kwargs) -> list[str]: ...
    def acl_deluser(self, *username: str, **kwargs) -> int: ...
    def acl_genpass(self, bits: int | None = ..., **kwargs) -> str: ...
    def acl_getuser(self, username: str, **kwargs) -> Any | None: ...
    def acl_help(self, **kwargs): ...
    def acl_list(self, **kwargs) -> list[str]: ...
    def acl_log(self, count: int | None = ..., **kwargs): ...
    def acl_log_reset(self, **kwargs): ...
    def acl_load(self, **kwargs) -> bool: ...
    def acl_save(self, **kwargs): ...
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
        **kwargs,
    ) -> bool: ...
    def acl_users(self, **kwargs) -> list[str]: ...
    def acl_whoami(self, **kwargs) -> str: ...

class ManagementCommands:
    def bgrewriteaof(self, **kwargs): ...
    def bgsave(self, schedule: bool = ..., **kwargs): ...
    def role(self): ...
    def client_kill(self, address: str, **kwargs) -> bool: ...
    def client_kill_filter(
        self,
        _id: Any | None = ...,
        _type: Any | None = ...,
        addr: Any | None = ...,
        skipme: Any | None = ...,
        laddr: Any | None = ...,
        user: Any | None = ...,
        **kwargs,
    ): ...
    def client_info(self, **kwargs): ...
    def client_list(self, _type: str | None = ..., client_id: list[str] = ..., **kwargs) -> list[dict[str, str]]: ...
    def client_getname(self, **kwargs) -> str | None: ...
    def client_getredir(self, **kwargs): ...
    def client_reply(self, reply, **kwargs): ...
    def client_id(self, **kwargs) -> int: ...
    def client_tracking_on(
        self, clientid: Any | None = ..., prefix=..., bcast: bool = ..., optin: bool = ..., optout: bool = ..., noloop: bool = ...
    ): ...
    def client_tracking_off(
        self, clientid: Any | None = ..., prefix=..., bcast: bool = ..., optin: bool = ..., optout: bool = ..., noloop: bool = ...
    ): ...
    def client_tracking(
        self,
        on: bool = ...,
        clientid: Any | None = ...,
        prefix=...,
        bcast: bool = ...,
        optin: bool = ...,
        optout: bool = ...,
        noloop: bool = ...,
        **kwargs,
    ): ...
    def client_trackinginfo(self, **kwargs): ...
    def client_setname(self, name: str, **kwargs) -> bool: ...
    def client_unblock(self, client_id, error: bool = ..., **kwargs): ...
    def client_pause(self, timeout, all: bool = ..., **kwargs): ...
    def client_unpause(self, **kwargs): ...
    def command(self, **kwargs): ...
    def command_info(self, **kwargs): ...
    def command_count(self, **kwargs): ...
    def config_get(self, pattern: str = ..., **kwargs): ...
    def config_set(self, name, value, **kwargs): ...
    def config_resetstat(self, **kwargs): ...
    def config_rewrite(self, **kwargs): ...
    def dbsize(self, **kwargs) -> int: ...
    def debug_object(self, key, **kwargs): ...
    def debug_segfault(self, **kwargs): ...
    def echo(self, value: _Value, **kwargs) -> bytes: ...
    def flushall(self, asynchronous: bool = ..., **kwargs) -> bool: ...
    def flushdb(self, asynchronous: bool = ..., **kwargs) -> bool: ...
    def sync(self): ...
    def psync(self, replicationid, offset): ...
    def swapdb(self, first, second, **kwargs): ...
    def select(self, index, **kwargs): ...
    def info(self, section: _Key | None = ..., **kwargs) -> Mapping[str, Any]: ...
    def lastsave(self, **kwargs): ...
    def lolwut(self, *version_numbers, **kwargs): ...
    def reset(self) -> None: ...
    def migrate(
        self, host, port, keys, destination_db, timeout, copy: bool = ..., replace: bool = ..., auth: Any | None = ..., **kwargs
    ): ...
    def object(self, infotype, key, **kwargs): ...
    def memory_doctor(self, **kwargs): ...
    def memory_help(self, **kwargs): ...
    def memory_stats(self, **kwargs) -> dict[str, Any]: ...
    def memory_malloc_stats(self, **kwargs): ...
    def memory_usage(self, key, samples: Any | None = ..., **kwargs): ...
    def memory_purge(self, **kwargs): ...
    def ping(self, **kwargs): ...
    def quit(self, **kwargs): ...
    def replicaof(self, *args, **kwargs): ...
    def save(self, **kwargs): ...
    def shutdown(self, save: bool = ..., nosave: bool = ..., **kwargs) -> None: ...
    def slaveof(self, host: Any | None = ..., port: Any | None = ..., **kwargs): ...
    def slowlog_get(self, num: Any | None = ..., **kwargs): ...
    def slowlog_len(self, **kwargs): ...
    def slowlog_reset(self, **kwargs): ...
    def time(self, **kwargs): ...
    def wait(self, num_replicas, timeout, **kwargs): ...

class BasicKeyCommands(Generic[_StrType]):
    def append(self, key, value): ...
    def bitcount(self, key: _Key, start: int | None = ..., end: int | None = ...) -> int: ...
    def bitfield(self, key, default_overflow: Any | None = ...): ...
    def bitop(self, operation, dest, *keys): ...
    def bitpos(self, key, bit, start=..., end=...): ...
    def copy(self, source, destination, destination_db: Any | None = ..., replace: bool = ...): ...
    def decr(self, name, amount: int = ...) -> int: ...
    def decrby(self, name, amount: int = ...) -> int: ...
    def delete(self, *names: _Key) -> int: ...
    def __delitem__(self, name: _Key) -> None: ...
    def dump(self, name): ...
    def exists(self, *names: _Key) -> int: ...
    __contains__ = exists
    def expire(self, name: _Key, time: int | timedelta) -> bool: ...
    def expireat(self, name, when): ...
    def get(self, name: _Key) -> _StrType | None: ...
    def getdel(self, name): ...
    def getex(
        self,
        name,
        ex: Any | None = ...,
        px: Any | None = ...,
        exat: Any | None = ...,
        pxat: Any | None = ...,
        persist: bool = ...,
    ): ...
    def __getitem__(self, name: str): ...
    def getbit(self, name: _Key, offset: int) -> int: ...
    def getrange(self, key, start, end): ...
    def getset(self, name, value) -> _StrType | None: ...
    def incr(self, name: _Key, amount: int = ...) -> int: ...
    def incrby(self, name: _Key, amount: int = ...) -> int: ...
    def incrbyfloat(self, name: _Key, amount: float = ...) -> float: ...
    def keys(self, pattern: _Key = ..., **kwargs) -> list[_StrType]: ...
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
    def mget(self, keys: _Key | Iterable[_Key], *args: _Key) -> list[_StrType | None]: ...
    def mset(self, mapping: Mapping[_Key, _Value]) -> Literal[True]: ...
    def msetnx(self, mapping: Mapping[_Key, _Value]) -> bool: ...
    def move(self, name: _Key, db: int) -> bool: ...
    def persist(self, name: _Key) -> bool: ...
    def pexpire(self, name: _Key, time: int | timedelta) -> Literal[1, 0]: ...
    def pexpireat(self, name: _Key, when: int | datetime) -> Literal[1, 0]: ...
    def psetex(self, name, time_ms, value): ...
    def pttl(self, name): ...
    def hrandfield(self, key, count: Any | None = ..., withvalues: bool = ...): ...
    def randomkey(self, **kwargs): ...
    def rename(self, src, dst): ...
    def renamenx(self, src, dst): ...
    def restore(
        self, name, ttl, value, replace: bool = ..., absttl: bool = ..., idletime: Any | None = ..., frequency: Any | None = ...
    ): ...
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
    def __setitem__(self, name, value) -> None: ...
    def setbit(self, name: _Key, offset: int, value: int) -> int: ...
    def setex(self, name: _Key, time: int | timedelta, value: _Value) -> bool: ...
    def setnx(self, name: _Key, value: _Value) -> bool: ...
    def setrange(self, name, offset, value): ...
    def stralgo(
        self,
        algo,
        value1,
        value2,
        specific_argument: str = ...,
        len: bool = ...,
        idx: bool = ...,
        minmatchlen: Any | None = ...,
        withmatchlen: bool = ...,
        **kwargs,
    ): ...
    def strlen(self, name): ...
    def substr(self, name, start, end: int = ...): ...
    def touch(self, *args): ...
    def ttl(self, name: _Key) -> int: ...
    def type(self, name): ...
    def watch(self, *names): ...
    def unwatch(self): ...
    def unlink(self, *names: _Key) -> int: ...

class ListCommands(Generic[_StrType]):
    @overload
    def blpop(self, keys: _Value | Iterable[_Value], timeout: Literal[0] | None = ...) -> tuple[_StrType, _StrType]: ...
    @overload
    def blpop(self, keys: _Value | Iterable[_Value], timeout: float) -> tuple[_StrType, _StrType] | None: ...
    @overload
    def brpop(self, keys: _Value | Iterable[_Value], timeout: Literal[0] | None = ...) -> tuple[_StrType, _StrType]: ...
    @overload
    def brpop(self, keys: _Value | Iterable[_Value], timeout: float) -> tuple[_StrType, _StrType] | None: ...
    def brpoplpush(self, src, dst, timeout: int | None = ...): ...
    def lindex(self, name: _Key, index: int) -> _StrType | None: ...
    def linsert(
        self, name: _Key, where: Literal["BEFORE", "AFTER", "before", "after"], refvalue: _Value, value: _Value
    ) -> int: ...
    def llen(self, name: _Key) -> int: ...
    def lpop(self, name, count: int | None = ...): ...
    def lpush(self, name: _Value, *values: _Value) -> int: ...
    def lpushx(self, name, value): ...
    def lrange(self, name: _Key, start: int, end: int) -> list[_StrType]: ...
    def lrem(self, name: _Key, count: int, value: _Value) -> int: ...
    def lset(self, name: _Key, index: int, value: _Value) -> bool: ...
    def ltrim(self, name: _Key, start: int, end: int) -> bool: ...
    def rpop(self, name, count: int | None = ...): ...
    def rpoplpush(self, src, dst): ...
    def rpush(self, name: _Value, *values: _Value) -> int: ...
    def rpushx(self, name, value): ...
    def lpos(self, name, value, rank: Any | None = ..., count: Any | None = ..., maxlen: Any | None = ...): ...
    @overload
    def sort(
        self,
        name: _Key,
        start: int | None = ...,
        num: int | None = ...,
        by: _Key | None = ...,
        get: _Key | Sequence[_Key] | None = ...,
        desc: bool = ...,
        alpha: bool = ...,
        store: None = ...,
        groups: bool = ...,
    ) -> list[_StrType]: ...
    @overload
    def sort(
        self,
        name: _Key,
        start: int | None = ...,
        num: int | None = ...,
        by: _Key | None = ...,
        get: _Key | Sequence[_Key] | None = ...,
        desc: bool = ...,
        alpha: bool = ...,
        *,
        store: _Key,
        groups: bool = ...,
    ) -> int: ...
    @overload
    def sort(
        self,
        name: _Key,
        start: int | None,
        num: int | None,
        by: _Key | None,
        get: _Key | Sequence[_Key] | None,
        desc: bool,
        alpha: bool,
        store: _Key,
        groups: bool = ...,
    ) -> int: ...

class ScanCommands(Generic[_StrType]):
    def scan(
        self, cursor: int = ..., match: _Key | None = ..., count: int | None = ..., _type: str | None = ..., **kwargs
    ) -> tuple[int, list[_StrType]]: ...
    def scan_iter(
        self, match: str | None = ..., count: int | None = ..., _type: str | None = ..., **kwargs
    ) -> Iterator[_StrType]: ...
    def sscan(
        self, name: _Key, cursor: int = ..., match: str | None = ..., count: int | None = ...
    ) -> tuple[int, list[_StrType]]: ...
    def sscan_iter(self, name: _Key, match: str | None = ..., count: int | None = ...): ...
    def hscan(
        self, name: _Key, cursor: int = ..., match: str | None = ..., count: int | None = ...
    ) -> tuple[int, dict[_StrType, _StrType]]: ...
    def hscan_iter(self, name: _Key, match: str | None = ..., count: int | None = ...): ...
    def zscan(self, name, cursor: int = ..., match: Any | None = ..., count: Any | None = ..., score_cast_func=...): ...
    def zscan_iter(self, name, match: Any | None = ..., count: Any | None = ..., score_cast_func=...): ...

class SetCommands(Generic[_StrType]):
    def sadd(self, name: _Key, *values: _Value) -> int: ...
    def scard(self, name: _Key) -> int: ...
    def sdiff(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]: ...
    def sdiffstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int: ...
    def sinter(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]: ...
    def sinterstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int: ...
    def sismember(self, name: _Key, value: _Value) -> bool: ...
    def smembers(self, name: _Key) -> builtins.set[_StrType]: ...
    def smismember(self, name, values, *args): ...
    def smove(self, src: _Key, dst: _Key, value: _Value) -> bool: ...
    @overload
    def spop(self, name: _Key, count: None = ...) -> _Value | None: ...
    @overload
    def spop(self, name: _Key, count: int) -> list[_Value]: ...
    @overload
    def srandmember(self, name: _Key, number: None = ...) -> _Value | None: ...
    @overload
    def srandmember(self, name: _Key, number: int) -> list[_Value]: ...
    def srem(self, name: _Key, *values: _Value) -> int: ...
    def sunion(self, keys: _Key | Iterable[_Key], *args: _Key) -> builtins.set[_Value]: ...
    def sunionstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> int: ...

class StreamCommands:
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
    def xautoclaim(
        self, name, groupname, consumername, min_idle_time, start_id: int = ..., count: Any | None = ..., justid: bool = ...
    ): ...
    def xclaim(
        self, name, groupname, consumername, min_idle_time, message_ids, idle=..., time=..., retrycount=..., force=..., justid=...
    ): ...
    def xdel(self, name, *ids): ...
    def xgroup_create(self, name, groupname, id: str = ..., mkstream: bool = ...): ...
    def xgroup_delconsumer(self, name, groupname, consumername): ...
    def xgroup_destroy(self, name, groupname): ...
    def xgroup_createconsumer(self, name, groupname, consumername): ...
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
    def xrange(self, name, min: str = ..., max: str = ..., count: Any | None = ...): ...
    def xread(self, streams, count: Any | None = ..., block: Any | None = ...): ...
    def xreadgroup(
        self, groupname, consumername, streams, count: Any | None = ..., block: Any | None = ..., noack: bool = ...
    ): ...
    def xrevrange(self, name, max: str = ..., min: str = ..., count: Any | None = ...): ...
    def xtrim(
        self, name, maxlen: Any | None = ..., approximate: bool = ..., minid: Any | None = ..., limit: Any | None = ...
    ): ...

class SortedSetCommands(Generic[_StrType]):
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
    def zdiff(self, keys, withscores: bool = ...): ...
    def zdiffstore(self, dest, keys): ...
    def zincrby(self, name: _Key, amount: float, value: _Value) -> float: ...
    def zinter(self, keys, aggregate: Any | None = ..., withscores: bool = ...): ...
    def zinterstore(self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = ...) -> int: ...
    def zlexcount(self, name: _Key, min: _Value, max: _Value) -> int: ...
    def zpopmax(self, name: _Key, count: int | None = ...) -> list[tuple[_StrType, float]]: ...
    def zpopmin(self, name: _Key, count: int | None = ...) -> list[tuple[_StrType, float]]: ...
    def zrandmember(self, key, count: Any | None = ..., withscores: bool = ...): ...
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
        desc: bool,
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
    @overload
    def zrevrange(
        self,
        name: _Key,
        start: int,
        end: int,
        withscores: Literal[True],
        score_cast_func: Callable[[float], _ScoreCastFuncReturn] = ...,
    ) -> list[tuple[_StrType, _ScoreCastFuncReturn]]: ...
    @overload
    def zrevrange(
        self, name: _Key, start: int, end: int, withscores: bool = ..., score_cast_func: Callable[[Any], Any] = ...
    ) -> list[_StrType]: ...
    def zrangestore(
        self,
        dest,
        name,
        start,
        end,
        byscore: bool = ...,
        bylex: bool = ...,
        desc: bool = ...,
        offset: Any | None = ...,
        num: Any | None = ...,
    ): ...
    def zrangebylex(
        self, name: _Key, min: _Value, max: _Value, start: int | None = ..., num: int | None = ...
    ) -> list[_StrType]: ...
    def zrevrangebylex(
        self, name: _Key, max: _Value, min: _Value, start: int | None = ..., num: int | None = ...
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
    def zrank(self, name: _Key, value: _Value) -> int | None: ...
    def zrem(self, name: _Key, *values: _Value) -> int: ...
    def zremrangebylex(self, name: _Key, min: _Value, max: _Value) -> int: ...
    def zremrangebyrank(self, name: _Key, min: int, max: int) -> int: ...
    def zremrangebyscore(self, name: _Key, min: _Value, max: _Value) -> int: ...
    def zrevrank(self, name: _Key, value: _Value) -> int | None: ...
    def zscore(self, name: _Key, value: _Value) -> float | None: ...
    def zunion(self, keys, aggregate: Any | None = ..., withscores: bool = ...): ...
    def zunionstore(self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = ...) -> int: ...
    def zmscore(self, key, members): ...

class HyperlogCommands:
    def pfadd(self, name: _Key, *values: _Value) -> int: ...
    def pfcount(self, name: _Key) -> int: ...
    def pfmerge(self, dest: _Key, *sources: _Key) -> bool: ...

class HashCommands(Generic[_StrType]):
    def hdel(self, name: _Key, *keys: _Key) -> int: ...
    def hexists(self, name: _Key, key: _Key) -> bool: ...
    def hget(self, name: _Key, key: _Key) -> _StrType | None: ...
    def hgetall(self, name: _Key) -> dict[_StrType, _StrType]: ...
    def hincrby(self, name: _Key, key: _Key, amount: int = ...) -> int: ...
    def hincrbyfloat(self, name: _Key, key: _Key, amount: float = ...) -> float: ...
    def hkeys(self, name: _Key) -> list[_StrType]: ...
    def hlen(self, name: _Key) -> int: ...
    @overload
    def hset(self, name: _Key, key: _Key, value: _Value, mapping: Mapping[_Key, _Value] | None = ...) -> int: ...
    @overload
    def hset(self, name: _Key, key: None, value: None, mapping: Mapping[_Key, _Value]) -> int: ...
    @overload
    def hset(self, name: _Key, *, mapping: Mapping[_Key, _Value]) -> int: ...
    def hsetnx(self, name: _Key, key: _Key, value: _Value) -> int: ...
    def hmset(self, name: _Key, mapping: Mapping[_Key, _Value]) -> bool: ...
    def hmget(self, name: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> list[_StrType | None]: ...
    def hvals(self, name: _Key) -> list[_StrType]: ...
    def hstrlen(self, name, key): ...

class PubSubCommands:
    def publish(self, channel: _Key, message: _Key, **kwargs) -> int: ...
    def pubsub_channels(self, pattern: _Key = ..., **kwargs) -> list[str]: ...
    def pubsub_numpat(self, **kwargs) -> int: ...
    def pubsub_numsub(self, *args: _Key, **kwargs) -> list[tuple[str, int]]: ...

class ScriptCommands(Generic[_StrType]):
    def eval(self, script, numkeys, *keys_and_args): ...
    def evalsha(self, sha, numkeys, *keys_and_args): ...
    def script_exists(self, *args): ...
    def script_debug(self, *args): ...
    def script_flush(self, sync_type: Any | None = ...): ...
    def script_kill(self): ...
    def script_load(self, script): ...
    def register_script(self, script: str | _StrType) -> Script: ...

class GeoCommands:
    def geoadd(self, name, values, nx: bool = ..., xx: bool = ..., ch: bool = ...): ...
    def geodist(self, name, place1, place2, unit: Any | None = ...): ...
    def geohash(self, name, *values): ...
    def geopos(self, name, *values): ...
    def georadius(
        self,
        name,
        longitude,
        latitude,
        radius,
        unit: Any | None = ...,
        withdist: bool = ...,
        withcoord: bool = ...,
        withhash: bool = ...,
        count: Any | None = ...,
        sort: Any | None = ...,
        store: Any | None = ...,
        store_dist: Any | None = ...,
        any: bool = ...,
    ): ...
    def georadiusbymember(
        self,
        name,
        member,
        radius,
        unit: Any | None = ...,
        withdist: bool = ...,
        withcoord: bool = ...,
        withhash: bool = ...,
        count: Any | None = ...,
        sort: Any | None = ...,
        store: Any | None = ...,
        store_dist: Any | None = ...,
        any: bool = ...,
    ): ...
    def geosearch(
        self,
        name,
        member: Any | None = ...,
        longitude: Any | None = ...,
        latitude: Any | None = ...,
        unit: str = ...,
        radius: Any | None = ...,
        width: Any | None = ...,
        height: Any | None = ...,
        sort: Any | None = ...,
        count: Any | None = ...,
        any: bool = ...,
        withcoord: bool = ...,
        withdist: bool = ...,
        withhash: bool = ...,
    ): ...
    def geosearchstore(
        self,
        dest,
        name,
        member: Any | None = ...,
        longitude: Any | None = ...,
        latitude: Any | None = ...,
        unit: str = ...,
        radius: Any | None = ...,
        width: Any | None = ...,
        height: Any | None = ...,
        sort: Any | None = ...,
        count: Any | None = ...,
        any: bool = ...,
        storedist: bool = ...,
    ): ...

class ModuleCommands:
    def module_load(self, path, *args): ...
    def module_unload(self, name): ...
    def module_list(self): ...
    def command_info(self): ...
    def command_count(self): ...
    def command_getkeys(self, *args): ...
    def command(self): ...

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

class ClusterCommands:
    def readwrite(self, **kwargs) -> bool: ...
    def readonly(self, **kwargs) -> bool: ...

class DataAccessCommands(
    BasicKeyCommands[_StrType],
    HyperlogCommands,
    HashCommands[_StrType],
    GeoCommands,
    ListCommands[_StrType],
    ScanCommands[_StrType],
    SetCommands[_StrType],
    StreamCommands,
    SortedSetCommands[_StrType],
    Generic[_StrType],
): ...
class CoreCommands(
    ACLCommands[_StrType],
    ClusterCommands,
    DataAccessCommands[_StrType],
    ManagementCommands,
    ModuleCommands,
    PubSubCommands,
    ScriptCommands[_StrType],
    Generic[_StrType],
): ...
