from typing import Any

__version__: str
__author__: str
__license__: str

LIBLDAP_API_INFO: Any
OPT_NAMES_DICT: dict[Any, Any]
OPT_ERROR_STRING: int
OPT_DIAGNOSTIC_MESSAGE: int

class LDAPLock:
    def __init__(self, lock_class: Any = ..., desc: str = ...) -> None: ...
    def acquire(self) -> None: ...
    def release(self) -> None: ...

_ldap_module_lock: LDAPLock

def initialize(
    uri: str,
    trace_level: int = ...,
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

class NO_UNIQUE_ENTRY(Exception): ...
class LDAPBytesWarning(Warning): ...

from ldap.dn import explode_dn as explode_dn, explode_rdn as explode_rdn
