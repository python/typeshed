from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Bool, String, Typed, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.ole import ObjectAnchor

class ControlProperty(Serialisable):
    tagname: str
    anchor: Typed[ObjectAnchor, Literal[False]]
    locked: Bool[Literal[True]]
    defaultSize: Bool[Literal[True]]
    _print: Bool[Literal[True]]  # Not private. Avoids name clash
    disabled: Bool[Literal[True]]
    recalcAlways: Bool[Literal[True]]
    uiObject: Bool[Literal[True]]
    autoFill: Bool[Literal[True]]
    autoLine: Bool[Literal[True]]
    autoPict: Bool[Literal[True]]
    macro: String[Literal[True]]
    altText: String[Literal[True]]
    linkedCell: String[Literal[True]]
    listFillRange: String[Literal[True]]
    cf: String[Literal[True]]
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        anchor: ObjectAnchor,
        locked: _ConvertibleToBool | None = True,
        defaultSize: _ConvertibleToBool | None = True,
        _print: _ConvertibleToBool | None = True,
        disabled: _ConvertibleToBool | None = False,
        recalcAlways: _ConvertibleToBool | None = False,
        uiObject: _ConvertibleToBool | None = False,
        autoFill: _ConvertibleToBool | None = True,
        autoLine: _ConvertibleToBool | None = True,
        autoPict: _ConvertibleToBool | None = True,
        macro: str | None = None,
        altText: str | None = None,
        linkedCell: str | None = None,
        listFillRange: str | None = None,
        cf: str | None = "pict",
        id: Incomplete | None = None,
    ) -> None: ...

class Control(Serialisable):
    tagname: str
    controlPr: Typed[ControlProperty, Literal[True]]
    shapeId: Incomplete
    name: String[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self, controlPr: ControlProperty | None = None, shapeId: Incomplete | None = None, name: str | None = None
    ) -> None: ...

class Controls(Serialisable):
    tagname: str
    control: Incomplete
    __elements__: Incomplete
    def __init__(self, control=()) -> None: ...
