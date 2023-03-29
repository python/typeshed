from _typeshed import Incomplete, Unused
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.workbook.defined_name import DefinedNameList
from openpyxl.workbook.function_group import FunctionGroupList
from openpyxl.workbook.properties import CalcProperties, FileVersion, WorkbookProperties
from openpyxl.workbook.protection import FileSharing, WorkbookProtection
from openpyxl.workbook.smart_tags import SmartTagList, SmartTagProperties
from openpyxl.workbook.web import WebPublishing, WebPublishObjectList

class FileRecoveryProperties(Serialisable):
    tagname: str
    autoRecover: Incomplete
    crashSave: Incomplete
    dataExtractLoad: Incomplete
    repairLoad: Incomplete
    def __init__(
        self,
        autoRecover: Incomplete | None = None,
        crashSave: Incomplete | None = None,
        dataExtractLoad: Incomplete | None = None,
        repairLoad: Incomplete | None = None,
    ) -> None: ...

class ChildSheet(Serialisable):
    tagname: str
    name: Incomplete
    sheetId: Incomplete
    state: Incomplete
    id: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        sheetId: Incomplete | None = None,
        state: str = "visible",
        id: Incomplete | None = None,
    ) -> None: ...

class PivotCache(Serialisable):
    tagname: str
    cacheId: Incomplete
    id: Incomplete
    def __init__(self, cacheId: Incomplete | None = None, id: Incomplete | None = None) -> None: ...

class WorkbookPackage(Serialisable):
    tagname: str
    conformance: Incomplete
    fileVersion: Typed[FileVersion, Literal[True]]
    fileSharing: Typed[FileSharing, Literal[True]]
    workbookPr: Typed[WorkbookProperties, Literal[True]]
    properties: Incomplete
    workbookProtection: Typed[WorkbookProtection, Literal[True]]
    bookViews: Incomplete
    sheets: Incomplete
    functionGroups: Typed[FunctionGroupList, Literal[True]]
    externalReferences: Incomplete
    definedNames: Typed[DefinedNameList, Literal[True]]
    calcPr: Typed[CalcProperties, Literal[True]]
    oleSize: Incomplete
    customWorkbookViews: Incomplete
    pivotCaches: Incomplete
    smartTagPr: Typed[SmartTagProperties, Literal[True]]
    smartTagTypes: Typed[SmartTagList, Literal[True]]
    webPublishing: Typed[WebPublishing, Literal[True]]
    fileRecoveryPr: Typed[FileRecoveryProperties, Literal[True]]
    webPublishObjects: Typed[WebPublishObjectList, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    Ignorable: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        conformance: Incomplete | None = None,
        fileVersion: FileVersion | None = None,
        fileSharing: FileSharing | None = None,
        workbookPr: WorkbookProperties | None = None,
        workbookProtection: WorkbookProtection | None = None,
        bookViews=(),
        sheets=(),
        functionGroups: FunctionGroupList | None = None,
        externalReferences=(),
        definedNames: DefinedNameList | None = None,
        calcPr: CalcProperties | None = None,
        oleSize: Incomplete | None = None,
        customWorkbookViews=(),
        pivotCaches=(),
        smartTagPr: SmartTagProperties | None = None,
        smartTagTypes: SmartTagList | None = None,
        webPublishing: WebPublishing | None = None,
        fileRecoveryPr: FileRecoveryProperties | None = None,
        webPublishObjects: WebPublishObjectList | None = None,
        extLst: Unused = None,
        Ignorable: Unused = None,
    ) -> None: ...
    def to_tree(self): ...
    @property
    def active(self): ...
