from _typeshed import Incomplete
from collections.abc import Iterator, MutableMapping
from typing import TypeAlias

__all__ = [
    "SEARCH_SCOPE",
    "SEARCH_SCOPE_STR",
    "LDAP_SCOPE_BASE",
    "LDAP_SCOPE_ONELEVEL",
    "LDAP_SCOPE_SUBTREE",
    "isLDAPUrl",
    "LDAPUrlExtension",
    "LDAPUrlExtensions",
    "LDAPUrl",
]

LDAP_SCOPE_BASE: int
LDAP_SCOPE_ONELEVEL: int
LDAP_SCOPE_SUBTREE: int
SEARCH_SCOPE_STR: Incomplete
SEARCH_SCOPE: Incomplete

def isLDAPUrl(s: str) -> bool: ...

class LDAPUrlExtension:
    critical: Incomplete
    extype: Incomplete
    exvalue: Incomplete
    def __init__(
        self, extensionStr: str | None = None, critical: int = 0, extype: str | None = None, exvalue: str | None = None
    ) -> None: ...
    def unparse(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

LDAPUrlExtensionsBase: TypeAlias = MutableMapping[str, LDAPUrlExtension]

class LDAPUrlExtensions(LDAPUrlExtensionsBase):
    def __init__(self, default: dict[str, LDAPUrlExtension] | None = None) -> None: ...
    def __setitem__(self, name: str, value: LDAPUrlExtension) -> None: ...
    def __getitem__(self, name: str) -> LDAPUrlExtension: ...
    def __delitem__(self, name: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def parse(self, extListStr: str) -> None: ...
    def unparse(self) -> str: ...

class LDAPUrl:
    attr2extype: Incomplete
    urlscheme: Incomplete
    hostport: Incomplete
    dn: Incomplete
    attrs: Incomplete
    scope: Incomplete
    filterstr: Incomplete
    extensions: LDAPUrlExtensions | None
    who: Incomplete
    cred: Incomplete
    def __init__(
        self,
        ldapUrl: str | None = None,
        urlscheme: str = "ldap",
        hostport: str = "",
        dn: str = "",
        attrs: list[str] | None = None,
        scope: int | None = None,
        filterstr: str | None = None,
        extensions: LDAPUrlExtensions | None = None,
        who: str | None = None,
        cred: str | None = None,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def applyDefaults(self, defaults: dict[str, str]) -> None: ...
    def initializeUrl(self) -> str: ...
    def unparse(self) -> str: ...
    def htmlHREF(self, urlPrefix: str = "", hrefText: str | None = None, hrefTarget: str | None = None) -> str: ...
    def __getattr__(self, name: str) -> str | None: ...
    def __setattr__(self, name: str, value: str) -> None: ...
    def __delattr__(self, name: str) -> None: ...
