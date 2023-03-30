from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import Set, Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker

_OleObjectDvAspect: TypeAlias = Literal["DVASPECT_CONTENT", "DVASPECT_ICON"]
_OleObjectOleUpdate: TypeAlias = Literal["OLEUPDATE_ALWAYS", "OLEUPDATE_ONCALL"]

class ObjectAnchor(Serialisable):
    tagname: str
    to: Typed[AnchorMarker, Literal[False]]
    moveWithCells: Incomplete
    sizeWithCells: Incomplete
    z_order: Incomplete
    def __init__(
        self,
        _from: AnchorMarker,
        to: AnchorMarker,
        moveWithCells: bool = False,
        sizeWithCells: bool = False,
        z_order: Incomplete | None = None,
    ) -> None: ...

class ObjectPr(Serialisable):
    tagname: str
    anchor: Typed[ObjectAnchor, Literal[False]]
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    autoPict: Incomplete
    macro: Incomplete
    altText: Incomplete
    dde: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        anchor: ObjectAnchor,
        locked: bool = True,
        defaultSize: bool = True,
        _print: bool = True,
        disabled: bool = False,
        uiObject: bool = False,
        autoFill: bool = True,
        autoLine: bool = True,
        autoPict: bool = True,
        macro: Incomplete | None = None,
        altText: Incomplete | None = None,
        dde: bool = False,
    ) -> None: ...

class OleObject(Serialisable):
    tagname: str
    objectPr: Typed[ObjectPr, Literal[True]]
    progId: Incomplete
    dvAspect: Set[_OleObjectDvAspect]
    link: Incomplete
    oleUpdate: Set[_OleObjectOleUpdate]
    autoLoad: Incomplete
    shapeId: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        objectPr: ObjectPr | None,
        progId: Incomplete | None,
        dvAspect: _OleObjectDvAspect,
        link: Incomplete | None,
        oleUpdate: _OleObjectOleUpdate,
        autoLoad: bool = False,
        shapeId: Incomplete | None = None,
    ) -> None: ...

class OleObjects(Serialisable):
    tagname: str
    oleObject: Incomplete
    __elements__: Incomplete
    def __init__(self, oleObject=()) -> None: ...
