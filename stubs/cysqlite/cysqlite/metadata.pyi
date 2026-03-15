from typing import Any, NamedTuple
from typing_extensions import Buffer

class Index(NamedTuple):
    name: str
    sql: str
    columns: list[str]
    unique: bool
    table: str

class Column(NamedTuple):
    name: str
    data_type: str
    null: bool
    primary_key: bool
    table: str
    default: Any | None

class ForeignKey(NamedTuple):
    column: str
    dest_table: str
    dest_column: str
    table: str

class View(NamedTuple):
    name: str
    sql: str

class ColumnMetadata(NamedTuple):
    table: str | Buffer
    column: str | Buffer
    datatype: str
    collation: str
    not_null: bool
    primary_key: bool
    auto_increment: bool
