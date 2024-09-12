from _typeshed import MaybeNone
from collections.abc import Callable, Iterator
from typing import Any

__all__ = [
    "LUA_VERSION",
    "LUA_MAXINTEGER",
    "LUA_MININTEGER",
    "LuaRuntime",
    "LuaError",
    "LuaSyntaxError",
    "LuaMemoryError",
    "as_itemgetter",
    "as_attrgetter",
    "lua_type",
    "unpacks_lua_table",
    "unpacks_lua_table_method",
]

LUA_MAXINTEGER: int
LUA_MININTEGER: int
LUA_VERSION: tuple[int, int]

# cyfunction object
as_attrgetter: Callable[[object], object]
as_itemgetter: Callable[[object], object]

# cyfunction object
lua_type: Callable[[object], str | MaybeNone]

# cyfunction object as decorator
unpacks_lua_table: Callable[[Callable[..., Any]], Callable[..., Any]]
unpacks_lua_table_method: Callable[[Callable[..., Any]], Callable[..., Any]]

## classes

class FastRLock:
    @classmethod
    def __init__(self, /, *args: Any, **kwargs: Any) -> None: ...
    def acquire(self, blocking: bool = ...) -> Any: ...
    def release(self) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, t: object, v: object, tb: object) -> Any: ...

class LuaError(Exception): ...
class LuaSyntaxError(LuaError): ...
class LuaMemoryError(LuaError, MemoryError): ...

class LuaRuntime:
    lua_implementation: str
    lua_version: tuple[int, int]

    @classmethod
    def __cinit__(cls, unpack_return_tuples: bool) -> None: ...
    def add_pending_unref(self, ref: int) -> None: ...
    def clean_up_pending_unrefs(self) -> int: ...
    def get_max_memory(self, total: bool = False) -> int | MaybeNone: ...
    def get_memory_used(self, total: bool = False) -> int | MaybeNone: ...
    def reraise_on_exceptions(self) -> int: ...
    def store_raised_exception(self, L: object, lua_error_msg: str) -> None: ...  # unannotated
    def eval(self, lua_code: str, *args: Any, name: str | None = None, mode: str | None = None) -> Any: ...
    def execute(self, lua_code: str, *args: Any, name: str | None = None, mode: str | None = None) -> Any: ...
    def compile(self, lua_code: str, name: str | None = None, mode: str | None = None) -> Callable[..., Any]: ...
    def require(self, modulename: str) -> Any: ...
    def globals(self) -> _LuaTable: ...
    def table(self, *items: Any, **kwargs: Any) -> _LuaTable: ...
    def table_from(self, *args: Any, recursive: bool = ...) -> _LuaTable: ...
    def nogc(self) -> _LuaNoGC: ...
    def gccollect(self) -> None: ...
    def set_max_memory(self, max_memory: int, total: bool = False) -> None: ...
    def set_overflow_handler(self, overflow_handler: Callable[..., None]) -> None: ...
    def register_py_object(self, cname: str, pyname: str, obj: object) -> int: ...
    def init_python_lib(self, register_eval: bool, register_builtins: bool) -> int: ...

## inner classes

class _LuaIter:
    def __iter__(self) -> Iterator[object]: ...

class _LuaTable:
    def keys(self) -> _LuaIter: ...
    def values(self) -> _LuaIter: ...
    def items(self) -> _LuaIter: ...

class _LuaNoGC: ...
class _LuaObject: ...
