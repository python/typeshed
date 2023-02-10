from _typeshed import Self, SupportsItems, Unused
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, NamedTuple
from typing_extensions import TypeAlias

from ..util import immutabledict
from .interfaces import Dialect

# object that produces a password when called with str()
_PasswordObject: TypeAlias = object

# stub-only helper class
class _URLTuple(NamedTuple):
    drivername: str
    username: str | None
    password: str | _PasswordObject | None
    host: str | None
    port: int | None
    database: str | None
    query: immutabledict[str, str | tuple[str, ...]]

_Query: TypeAlias = Mapping[str, str | Sequence[str]] | Sequence[tuple[str, str | Sequence[str]]]

class URL(_URLTuple):
    @classmethod
    def create(
        cls,
        drivername: str,
        username: str | None = ...,
        password: str | _PasswordObject | None = None,
        host: str | None = ...,
        port: int | None = ...,
        database: str | None = ...,
        query: _Query | None = ...,
    ) -> URL: ...
    def set(
        self: Self,
        drivername: str | None = ...,
        username: str | None = ...,
        password: str | _PasswordObject | None = None,
        host: str | None = ...,
        port: int | None = ...,
        database: str | None = ...,
        query: _Query | None = ...,
    ) -> Self: ...
    def update_query_string(self: Self, query_string: str, append: bool = ...) -> Self: ...
    def update_query_pairs(self: Self, key_value_pairs: Iterable[tuple[str, str]], append: bool = ...) -> Self: ...
    def update_query_dict(self: Self, query_parameters: SupportsItems[str, str | Sequence[str]], append: bool = ...) -> Self: ...
    def difference_update_query(self, names: Iterable[str]) -> URL: ...
    @property
    def normalized_query(self) -> immutabledict[str, tuple[str, ...]]: ...
    def __to_string__(self, hide_password: bool = ...) -> str: ...
    def render_as_string(self, hide_password: bool = ...) -> str: ...
    def __copy__(self: Self) -> Self: ...
    def __deepcopy__(self: Self, memo: Unused) -> Self: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def get_backend_name(self) -> str: ...
    def get_driver_name(self) -> str: ...
    def get_dialect(self) -> type[Dialect]: ...
    def translate_connect_args(self, names: list[str] | None = ..., **kw: str) -> dict[str, Any]: ...

def make_url(name_or_url: str | URL) -> URL: ...
