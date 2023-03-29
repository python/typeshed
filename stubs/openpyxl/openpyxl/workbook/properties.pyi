from _typeshed import Incomplete

from openpyxl.descriptors.base import NoneSet
from openpyxl.descriptors.serialisable import Serialisable

class WorkbookProperties(Serialisable):
    tagname: str
    date1904: Incomplete
    dateCompatibility: Incomplete
    showObjects: NoneSet(values=(["all", "placeholders"]))
    showBorderUnselectedTables: Incomplete
    filterPrivacy: Incomplete
    promptedSolutions: Incomplete
    showInkAnnotation: Incomplete
    backupFile: Incomplete
    saveExternalLinkValues: Incomplete
    updateLinks: NoneSet(values=(["userSet", "never", "always"]))
    codeName: Incomplete
    hidePivotFieldList: Incomplete
    showPivotChartFilter: Incomplete
    allowRefreshQuery: Incomplete
    publishItems: Incomplete
    checkCompatibility: Incomplete
    autoCompressPictures: Incomplete
    refreshAllConnections: Incomplete
    defaultThemeVersion: Incomplete
    def __init__(
        self,
        date1904: Incomplete | None = None,
        dateCompatibility: Incomplete | None = None,
        showObjects: Incomplete | None = None,
        showBorderUnselectedTables: Incomplete | None = None,
        filterPrivacy: Incomplete | None = None,
        promptedSolutions: Incomplete | None = None,
        showInkAnnotation: Incomplete | None = None,
        backupFile: Incomplete | None = None,
        saveExternalLinkValues: Incomplete | None = None,
        updateLinks: Incomplete | None = None,
        codeName: Incomplete | None = None,
        hidePivotFieldList: Incomplete | None = None,
        showPivotChartFilter: Incomplete | None = None,
        allowRefreshQuery: Incomplete | None = None,
        publishItems: Incomplete | None = None,
        checkCompatibility: Incomplete | None = None,
        autoCompressPictures: Incomplete | None = None,
        refreshAllConnections: Incomplete | None = None,
        defaultThemeVersion: Incomplete | None = None,
    ) -> None: ...

class CalcProperties(Serialisable):
    tagname: str
    calcId: Incomplete
    calcMode: NoneSet(values=(["manual", "auto", "autoNoTable"]))
    fullCalcOnLoad: Incomplete
    refMode: NoneSet(values=(["A1", "R1C1"]))
    iterate: Incomplete
    iterateCount: Incomplete
    iterateDelta: Incomplete
    fullPrecision: Incomplete
    calcCompleted: Incomplete
    calcOnSave: Incomplete
    concurrentCalc: Incomplete
    concurrentManualCount: Incomplete
    forceFullCalc: Incomplete
    def __init__(
        self,
        calcId: int = 124519,
        calcMode: Incomplete | None = None,
        fullCalcOnLoad: bool = True,
        refMode: Incomplete | None = None,
        iterate: Incomplete | None = None,
        iterateCount: Incomplete | None = None,
        iterateDelta: Incomplete | None = None,
        fullPrecision: Incomplete | None = None,
        calcCompleted: Incomplete | None = None,
        calcOnSave: Incomplete | None = None,
        concurrentCalc: Incomplete | None = None,
        concurrentManualCount: Incomplete | None = None,
        forceFullCalc: Incomplete | None = None,
    ) -> None: ...

class FileVersion(Serialisable):
    tagname: str
    appName: Incomplete
    lastEdited: Incomplete
    lowestEdited: Incomplete
    rupBuild: Incomplete
    codeName: Incomplete
    def __init__(
        self,
        appName: Incomplete | None = None,
        lastEdited: Incomplete | None = None,
        lowestEdited: Incomplete | None = None,
        rupBuild: Incomplete | None = None,
        codeName: Incomplete | None = None,
    ) -> None: ...
