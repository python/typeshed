import json as json
from typing import Any

from psycopg2._psycopg import (
    ISQLQuote as ISQLQuote,
    QuotedString as QuotedString,
    new_array_type as new_array_type,
    new_type as new_type,
    register_type as register_type,
)

JSON_OID: int
JSONARRAY_OID: int
JSONB_OID: int
JSONBARRAY_OID: int

class Json:
    adapted: Any
    def __init__(self, adapted, dumps: Any | None = ...) -> None: ...
    def __conform__(self, proto): ...
    def dumps(self, obj): ...
    def prepare(self, conn) -> None: ...
    def getquoted(self): ...

def register_json(
    conn_or_curs: Any | None = ...,
    globally: bool = ...,
    loads: Any | None = ...,
    oid: Any | None = ...,
    array_oid: Any | None = ...,
    name: str = ...,
): ...
def register_default_json(conn_or_curs: Any | None = ..., globally: bool = ..., loads: Any | None = ...): ...
def register_default_jsonb(conn_or_curs: Any | None = ..., globally: bool = ..., loads: Any | None = ...): ...
