from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, Integer, Set, String, Typed, _ConvertibleToBool, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker

_OleObjectDvAspect: TypeAlias = Literal["DVASPECT_CONTENT", "DVASPECT_ICON"]
_OleObjectOleUpdate: TypeAlias = Literal["OLEUPDATE_ALWAYS", "OLEUPDATE_ONCALL"]

class ObjectAnchor(Serialisable):
    tagname: str
    _from: Typed[AnchorMarker, Literal[False]]  # Not private. Avoids name clash
    to: Typed[AnchorMarker, Literal[False]]
    moveWithCells: Bool[Literal[True]]
    sizeWithCells: Bool[Literal[True]]
    z_order: Integer[Literal[True]]
    def __init__(
        self,
        _from: AnchorMarker,
        to: AnchorMarker,
        moveWithCells: _ConvertibleToBool | None = False,
        sizeWithCells: _ConvertibleToBool | None = False,
        z_order: _ConvertibleToInt | None = None,
    ) -> None: ...

class ObjectPr(Serialisable):
    tagname: str
    anchor: Typed[ObjectAnchor, Literal[False]]
    locked: Bool[Literal[True]]
    defaultSize: Bool[Literal[True]]
    _print: Bool[Literal[True]]  # Not private. Avoids name clash
    disabled: Bool[Literal[True]]
    uiObject: Bool[Literal[True]]
    autoFill: Bool[Literal[True]]
    autoLine: Bool[Literal[True]]
    autoPict: Bool[Literal[True]]
    macro: String[Literal[False]]
    altText: String[Literal[True]]
    dde: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        anchor: ObjectAnchor,
        locked: _ConvertibleToBool | None,
        defaultSize: _ConvertibleToBool | None,
        _print: _ConvertibleToBool | None,
        disabled: _ConvertibleToBool | None,
        uiObject: _ConvertibleToBool | None,
        autoFill: _ConvertibleToBool | None,
        autoLine: _ConvertibleToBool | None,
        autoPict: _ConvertibleToBool | None,
        macro: str,
        altText: str | None = None,
        dde: _ConvertibleToBool | None = False,
    ) -> None: ...

class OleObject(Serialisable):
    tagname: str
    objectPr: Typed[ObjectPr, Literal[True]]
    progId: String[Literal[True]]
    dvAspect: Set[_OleObjectDvAspect]
    link: String[Literal[True]]
    oleUpdate: Set[_OleObjectOleUpdate]
    autoLoad: Bool[Literal[True]]
    shapeId: Integer[Literal[False]]
    __elements__: Incomplete
    def __init__(
        self,
        objectPr: ObjectPr | None,
        progId: str | None,
        dvAspect: _OleObjectDvAspect,
        link: str | None,
        oleUpdate: _OleObjectOleUpdate,
        autoLoad: _ConvertibleToBool | None,
        shapeId: _ConvertibleToInt,
    ) -> None: ...

class OleObjects(Serialisable):
    tagname: str
    oleObject: Incomplete
    __elements__: Incomplete
    def __init__(self, oleObject=()) -> None: ...
