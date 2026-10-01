from _typeshed import Incomplete
from typing import Any

from ldap._ldap import *
from ldap._types import *
from ldap.dn import dn2str as dn2str, explode_dn as explode_dn, explode_rdn as explode_rdn, str2dn as str2dn
from ldap.functions import (
    escape_str as escape_str,
    get_option as get_option,
    initialize as initialize,
    set_option as set_option,
    strf_secs as strf_secs,
    strp_secs as strp_secs,
)
from ldap.ldapobject import NO_UNIQUE_ENTRY as NO_UNIQUE_ENTRY, LDAPBytesWarning as LDAPBytesWarning
from ldap.pkginfo import __version__ as __version__

LIBLDAP_API_INFO: Incomplete
OPT_NAMES_DICT: Incomplete
LDAPLockBaseClass: Incomplete

class LDAPLock:
    def __init__(self, lock_class: type[Any] | None = None, desc: str = "") -> None: ...
    def acquire(self) -> bool: ...
    def release(self) -> None: ...

OPT_DIAGNOSTIC_MESSAGE = OPT_ERROR_STRING
