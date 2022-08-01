from _typeshed import Self

from re import Pattern

from sqlalchemy import Table
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Query

def should_set_tablename(cls: type) -> bool: ...

camelcase_re: Pattern[str]

def camel_to_snake_case(name: str) -> str: ...

class NameMetaMixin(type):
    def __init__(cls, name: str, bases: tuple[type, ...], d: dict[str, Any]) -> None: ...
    def __table_cls__(cls, *args, **kwargs) -> Table | None: ...

class BindMetaMixin(type):
    def __init__(cls, name: str, bases: tuple[type, ...], d: dict[str, Any]) -> None: ...

class DefaultMeta(NameMetaMixin, BindMetaMixin, DeclarativeMeta): ...

class Model:
    # These aren't actually properties at runtime, but we treat them as such so we can use `self` types
    # without using typing.Self
    @property
    def query_class(self: Self) -> type[Query[Self]] | None: ...
    @query_class.setter
    def query_class(self: Self, value: type[Query[Self]] | None) -> None: ...
    @property
    def query(self: Self) -> Query[Self] | None: ...
    @query.setter
    def query(self: Self, value: Query[Self] | None) -> None: ...
