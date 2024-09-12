from collections.abc import Iterator
from contextlib import contextmanager as _contextmanager

from .lua54 import *
from .version import __version__ as version

__all__ = [
    "allow_lua_module_loading",
    "version",
    # from lua54 (newest lib)
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

@_contextmanager
def allow_lua_module_loading() -> Iterator[None]: ...
