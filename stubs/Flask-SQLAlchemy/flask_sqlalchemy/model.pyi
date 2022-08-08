from re import Pattern
from typing import Any

from sqlalchemy import Table
from sqlalchemy.ext.declarative import DeclarativeMeta

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
    query_class: Any | None
    query: Any | None
