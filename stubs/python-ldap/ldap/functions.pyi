from collections.abc import Callable
from typing import Any, BinaryIO, TextIO

from ldap.dn import explode_dn as explode_dn, explode_rdn as explode_rdn
from ldap.ldapobject import LDAPObject

__all__ = ["initialize", "explode_dn", "explode_rdn", "get_option", "set_option", "escape_str", "strf_secs", "strp_secs"]

def initialize(
    uri: str,
    trace_level: int = 0,
    trace_file: TextIO = ...,
    trace_stack_limit: int | None = None,
    bytes_mode: Any | None = None,
    fileno: int | BinaryIO | None = None,
    **kwargs: Any,
) -> LDAPObject: ...
def get_option(option: int) -> Any: ...
def set_option(option: int, invalue: Any) -> int: ...
def escape_str(escape_func: Callable[[str], str], s: str, *args: str) -> str: ...
def strf_secs(secs: float) -> str: ...
def strp_secs(dt_str: str) -> int: ...
