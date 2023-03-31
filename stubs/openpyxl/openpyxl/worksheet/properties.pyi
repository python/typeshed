from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, Typed, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable

class Outline(Serialisable):
    tagname: str
    applyStyles: Bool[Literal[True]]
    summaryBelow: Bool[Literal[True]]
    summaryRight: Bool[Literal[True]]
    showOutlineSymbols: Bool[Literal[True]]
    def __init__(
        self,
        applyStyles: _ConvertibleToBool | None = None,
        summaryBelow: _ConvertibleToBool | None = None,
        summaryRight: _ConvertibleToBool | None = None,
        showOutlineSymbols: _ConvertibleToBool | None = None,
    ) -> None: ...

class PageSetupProperties(Serialisable):
    tagname: str
    autoPageBreaks: Bool[Literal[True]]
    fitToPage: Bool[Literal[True]]
    def __init__(self, autoPageBreaks: _ConvertibleToBool | None = None, fitToPage: _ConvertibleToBool | None = None) -> None: ...

class WorksheetProperties(Serialisable):
    tagname: str
    codeName: Incomplete
    enableFormatConditionsCalculation: Bool[Literal[True]]
    filterMode: Bool[Literal[True]]
    published: Bool[Literal[True]]
    syncHorizontal: Bool[Literal[True]]
    syncRef: Incomplete
    syncVertical: Bool[Literal[True]]
    transitionEvaluation: Bool[Literal[True]]
    transitionEntry: Bool[Literal[True]]
    tabColor: Incomplete
    outlinePr: Typed[Outline, Literal[True]]
    pageSetUpPr: Typed[PageSetupProperties, Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        codeName: Incomplete | None = None,
        enableFormatConditionsCalculation: _ConvertibleToBool | None = None,
        filterMode: _ConvertibleToBool | None = None,
        published: _ConvertibleToBool | None = None,
        syncHorizontal: _ConvertibleToBool | None = None,
        syncRef: Incomplete | None = None,
        syncVertical: _ConvertibleToBool | None = None,
        transitionEvaluation: _ConvertibleToBool | None = None,
        transitionEntry: _ConvertibleToBool | None = None,
        tabColor: Incomplete | None = None,
        outlinePr: Outline | None = None,
        pageSetUpPr: PageSetupProperties | None = None,
    ) -> None: ...
