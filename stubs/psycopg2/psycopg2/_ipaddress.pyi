from psycopg2.extensions import (
    QuotedString as QuotedString,
    new_array_type as new_array_type,
    new_type as new_type,
    register_adapter as register_adapter,
    register_type as register_type,
)
from typing import Any

ipaddress: Any

def register_ipaddress(conn_or_curs: Any | None = ...) -> None: ...
def cast_interface(s, cur: Any | None = ...): ...
def cast_network(s, cur: Any | None = ...): ...
def adapt_ipaddress(obj): ...
