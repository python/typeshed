from typing import Any

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["SyncreplConsumer"]

class SyncUUID(univ.OctetString):
    subtypeSpec: Any  # TODO: Precise type

class SyncCookie(univ.OctetString): ...

class SyncRequestMode(univ.Enumerated):
    namedValues: Any  # TODO: Precise type
    subtypeSpec: Any  # TODO: Precise type

class SyncRequestValue(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SyncRequestControl(RequestControl):
    controlType: str
    criticality: Any  # TODO: Precise type
    cookie: Any  # TODO: Precise type
    mode: Any  # TODO: Precise type
    reloadHint: Any  # TODO: Precise type
    def __init__(
        self, criticality: int = 1, cookie: Any | None = None, mode: str = "refreshOnly", reloadHint: bool = False
    ) -> None: ...
    def encodeControlValue(self): ...

class SyncStateOp(univ.Enumerated):
    namedValues: Any  # TODO: Precise type
    subtypeSpec: Any  # TODO: Precise type

class SyncStateValue(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SyncStateControl(ResponseControl):
    controlType: str
    opnames: Any  # TODO: Precise type
    cookie: Any  # TODO: Precise type
    state: Any  # TODO: Precise type
    entryUUID: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...

class SyncDoneValue(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SyncDoneControl(ResponseControl):
    controlType: str
    cookie: Any  # TODO: Precise type
    refreshDeletes: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...

class RefreshDelete(univ.Sequence):
    componentType: Any  # TODO: Precise type

class RefreshPresent(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SyncUUIDs(univ.SetOf):
    componentType: Any  # TODO: Precise type

class SyncIdSet(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SyncInfoValue(univ.Choice):
    componentType: Any  # TODO: Precise type

class SyncInfoMessage:
    responseName: str
    newcookie: Any  # TODO: Precise type
    refreshDelete: Any  # TODO: Precise type
    refreshPresent: Any  # TODO: Precise type
    syncIdSet: Any  # TODO: Precise type
    def __init__(self, encodedMessage) -> None: ...

class SyncreplConsumer:
    def syncrepl_search(self, base, scope, mode: str = "refreshOnly", cookie: Any | None = None, **search_args): ...
    def syncrepl_poll(self, msgid: int = -1, timeout: Any | None = None, all: int = 0): ...
    def syncrepl_set_cookie(self, cookie) -> None: ...
    def syncrepl_get_cookie(self) -> None: ...
    def syncrepl_present(self, uuids, refreshDeletes: bool = False) -> None: ...
    def syncrepl_delete(self, uuids) -> None: ...
    def syncrepl_entry(self, dn, attrs, uuid) -> None: ...
    def syncrepl_refreshdone(self) -> None: ...
