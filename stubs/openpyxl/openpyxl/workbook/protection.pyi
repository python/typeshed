from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Alias, Bool, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class WorkbookProtection(Serialisable):
    tagname: str
    workbook_password: Alias
    workbookPasswordCharacterSet: Incomplete
    revision_password: Alias
    revisionsPasswordCharacterSet: Incomplete
    lockStructure: Bool[Literal[True]]
    lock_structure: Alias
    lockWindows: Bool[Literal[True]]
    lock_windows: Alias
    lockRevision: Bool[Literal[True]]
    lock_revision: Alias
    revisionsAlgorithmName: Incomplete
    revisionsHashValue: Incomplete
    revisionsSaltValue: Incomplete
    revisionsSpinCount: Incomplete
    workbookAlgorithmName: Incomplete
    workbookHashValue: Incomplete
    workbookSaltValue: Incomplete
    workbookSpinCount: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        workbookPassword: Incomplete | None = None,
        workbookPasswordCharacterSet: Incomplete | None = None,
        revisionsPassword: Incomplete | None = None,
        revisionsPasswordCharacterSet: Incomplete | None = None,
        lockStructure: _ConvertibleToBool | None = None,
        lockWindows: _ConvertibleToBool | None = None,
        lockRevision: _ConvertibleToBool | None = None,
        revisionsAlgorithmName: Incomplete | None = None,
        revisionsHashValue: Incomplete | None = None,
        revisionsSaltValue: Incomplete | None = None,
        revisionsSpinCount: Incomplete | None = None,
        workbookAlgorithmName: Incomplete | None = None,
        workbookHashValue: Incomplete | None = None,
        workbookSaltValue: Incomplete | None = None,
        workbookSpinCount: Incomplete | None = None,
    ) -> None: ...
    def set_workbook_password(self, value: str = "", already_hashed: bool = False) -> None: ...
    @property
    def workbookPassword(self): ...
    @workbookPassword.setter
    def workbookPassword(self, value) -> None: ...
    def set_revisions_password(self, value: str = "", already_hashed: bool = False) -> None: ...
    @property
    def revisionsPassword(self): ...
    @revisionsPassword.setter
    def revisionsPassword(self, value) -> None: ...
    @classmethod
    def from_tree(cls, node): ...

DocumentSecurity = WorkbookProtection

class FileSharing(Serialisable):
    tagname: str
    readOnlyRecommended: Bool[Literal[True]]
    userName: Incomplete
    reservationPassword: Incomplete
    algorithmName: Incomplete
    hashValue: Incomplete
    saltValue: Incomplete
    spinCount: Incomplete
    def __init__(
        self,
        readOnlyRecommended: _ConvertibleToBool | None = None,
        userName: Incomplete | None = None,
        reservationPassword: Incomplete | None = None,
        algorithmName: Incomplete | None = None,
        hashValue: Incomplete | None = None,
        saltValue: Incomplete | None = None,
        spinCount: Incomplete | None = None,
    ) -> None: ...
