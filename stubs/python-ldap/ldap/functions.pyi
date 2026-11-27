from typing import Any

from ldap.dn import explode_dn as explode_dn, explode_rdn as explode_rdn

__all__ = [
    "open",
    "initialize",
    "init",
    "explode_dn",
    "explode_rdn",
    "get_option",
    "set_option",
    "escape_str",
    "strf_secs",
    "strp_secs",
]

def initialize(
    uri: Any,
    trace_level: int = 0,
    trace_file: Any = ...,
    trace_stack_limit: Any = ...,
    bytes_mode: Any = ...,
    fileno: Any = ...,
    **kwargs: Any,
) -> Any: ...
def get_option(option: Any) -> Any: ...
def set_option(option: Any, invalue: Any) -> None: ...
def escape_str(escape_func: Any, s: Any, *args: Any) -> Any: ...
def strf_secs(secs: Any) -> Any: ...
def strp_secs(dt_str: Any) -> Any: ...

# Names in __all__ with no definition:
open: Any
init: Any
