from _typeshed import Incomplete
from typing import Any

from ldap._types import LDAPEntryDict
from ldap.controls import RequestControl, ResponseControl
from ldap.ldapobject import SimpleLDAPObject as _Base
from pyasn1.type import univ

__all__ = ["OpenLDAPSyncreplCookie", "SyncreplConsumer"]

class SyncUUID(univ.OctetString):
    subtypeSpec: Incomplete

class SyncCookie(univ.OctetString): ...

class SyncRequestMode(univ.Enumerated):
    namedValues: Incomplete
    subtypeSpec: Incomplete

class SyncRequestValue(univ.Sequence):
    componentType: Incomplete

class SyncRequestControl(RequestControl):
    controlType: str
    criticality: bool
    cookie: Incomplete
    mode: Incomplete
    reloadHint: Incomplete
    def __init__(
        self,
        criticality: int | bool = True,
        cookie: str | bytes | None = None,
        mode: str = "refreshOnly",
        reloadHint: bool = False,
    ) -> None: ...
    def encodeControlValue(self) -> bytes: ...

class SyncStateOp(univ.Enumerated):
    namedValues: Incomplete
    subtypeSpec: Incomplete

class SyncStateValue(univ.Sequence):
    componentType: Incomplete

class SyncStateControl(ResponseControl):
    controlType: str
    opnames: Incomplete
    cookie: str | None
    state: Incomplete
    entryUUID: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class SyncDoneValue(univ.Sequence):
    componentType: Incomplete

class SyncDoneControl(ResponseControl):
    controlType: str
    cookie: str | None
    refreshDeletes: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class RefreshDelete(univ.Sequence):
    componentType: Incomplete

class RefreshPresent(univ.Sequence):
    componentType: Incomplete

class SyncUUIDs(univ.SetOf):
    componentType: Incomplete

class SyncIdSet(univ.Sequence):
    componentType: Incomplete

class SyncInfoValue(univ.Choice):
    componentType: Incomplete

class SyncInfoMessage:
    responseName: str
    newcookie: Incomplete
    refreshDelete: Incomplete
    refreshPresent: Incomplete
    syncIdSet: Incomplete
    def __init__(self, encodedMessage: bytes) -> None: ...

class SyncreplConsumer(_Base):
    def __init__(self, *args, **kwargs) -> None: ...
    def syncrepl_search(
        self,
        base: str,
        scope: int,
        mode: str = "refreshOnly",
        cookie: str | bytes | None = None,
        reloadHint: bool = False,
        **search_args: Any,
    ) -> int: ...
    def syncrepl_poll(self, msgid: int = -1, timeout: int | None = None, all: int = 0) -> bool: ...
    def syncrepl_set_cookie(self, cookie: str) -> None: ...
    def syncrepl_get_cookie(self) -> str | bytes | None: ...
    def syncrepl_present(self, uuids: list[str] | None, refreshDeletes: bool = False) -> None: ...
    def syncrepl_delete(self, uuids: list[str]) -> None: ...
    def syncrepl_entry(self, dn: str, attrs: LDAPEntryDict, uuid: str) -> None: ...
    def syncrepl_refreshdone(self) -> None: ...

class OpenLDAPSyncreplCookie:
    rid: int
    sid: int
    def __init__(self, cookie: str | bytes = "") -> None: ...
    def update(self, cookie: str | bytes) -> OpenLDAPSyncreplCookie: ...
    def unparse(self) -> str: ...
