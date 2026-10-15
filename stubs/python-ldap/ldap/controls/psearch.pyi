from _typeshed import Incomplete

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["CHANGE_TYPES_INT", "CHANGE_TYPES_STR", "EntryChangeNotificationControl", "PersistentSearchControl"]

CHANGE_TYPES_INT: Incomplete
CHANGE_TYPES_STR: Incomplete

class PersistentSearchControl(RequestControl):
    class PersistentSearchControlValue(univ.Sequence):
        componentType: Incomplete

    controlType: str
    changeTypes: Incomplete
    def __init__(
        self,
        criticality: bool = True,
        changeTypes: list[int | str] | int | None = None,
        changesOnly: bool = False,
        returnECs: bool = True,
    ) -> None: ...
    def encodeControlValue(self) -> bytes: ...

class ChangeType(univ.Enumerated):
    namedValues: Incomplete
    subtypeSpec: Incomplete

class EntryChangeNotificationValue(univ.Sequence):
    componentType: Incomplete

class EntryChangeNotificationControl(ResponseControl):
    controlType: str
    changeType: Incomplete
    previousDN: str | None
    changeNumber: int | None
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
