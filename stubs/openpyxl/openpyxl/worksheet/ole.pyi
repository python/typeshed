from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Bool, Set, Typed, _ConvertibleToBool
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
    z_order: Incomplete
    def __init__(
        self,
        _from: AnchorMarker,
        to: AnchorMarker,
        moveWithCells: _ConvertibleToBool | None = False,
        sizeWithCells: _ConvertibleToBool | None = False,
        z_order: Incomplete | None = None,
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
    macro: Incomplete
    altText: Incomplete
    dde: Bool[Literal[True]]
    __elements__: Incomplete
    def __init__(
        self,
        anchor: ObjectAnchor,
        locked: _ConvertibleToBool | None = True,
        defaultSize: _ConvertibleToBool | None = True,
        _print: _ConvertibleToBool | None = True,
        disabled: _ConvertibleToBool | None = False,
        uiObject: _ConvertibleToBool | None = False,
        autoFill: _ConvertibleToBool | None = True,
        autoLine: _ConvertibleToBool | None = True,
        autoPict: _ConvertibleToBool | None = True,
        macro: Incomplete | None = None,
        altText: Incomplete | None = None,
        dde: _ConvertibleToBool | None = False,
    ) -> None: ...

class OleObject(Serialisable):
    tagname: str
    objectPr: Typed[ObjectPr, Literal[True]]
    progId: Incomplete
    dvAspect: Set[_OleObjectDvAspect]
    link: Incomplete
    oleUpdate: Set[_OleObjectOleUpdate]
    autoLoad: Bool[Literal[True]]
    shapeId: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        objectPr: ObjectPr | None,
        progId: Incomplete | None,
        dvAspect: _OleObjectDvAspect,
        link: Incomplete | None,
        oleUpdate: _OleObjectOleUpdate,
        autoLoad: _ConvertibleToBool | None = False,
        shapeId: Incomplete | None = None,
    ) -> None: ...

class OleObjects(Serialisable):
    tagname: str
    oleObject: Incomplete
    __elements__: Incomplete
    def __init__(self, oleObject=()) -> None: ...
