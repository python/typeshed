from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.worksheet.ole import ObjectAnchor

class ControlProperty(Serialisable):
    tagname: str
    anchor: Typed[ObjectAnchor, Literal[False]]
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    recalcAlways: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    autoPict: Incomplete
    macro: Incomplete
    altText: Incomplete
    linkedCell: Incomplete
    listFillRange: Incomplete
    cf: Incomplete
    id: Incomplete
    __elements__: Incomplete
    def __init__(
        self,
        anchor: ObjectAnchor,
        locked: bool = True,
        defaultSize: bool = True,
        _print: bool = True,
        disabled: bool = False,
        recalcAlways: bool = False,
        uiObject: bool = False,
        autoFill: bool = True,
        autoLine: bool = True,
        autoPict: bool = True,
        macro: Incomplete | None = None,
        altText: Incomplete | None = None,
        linkedCell: Incomplete | None = None,
        listFillRange: Incomplete | None = None,
        cf: str = "pict",
        id: Incomplete | None = None,
    ) -> None: ...

class Control(Serialisable):
    tagname: str
    controlPr: Typed[ControlProperty, Literal[True]]
    shapeId: Incomplete
    name: Incomplete
    __elements__: Incomplete
    def __init__(
        self, controlPr: ControlProperty | None = None, shapeId: Incomplete | None = None, name: Incomplete | None = None
    ) -> None: ...

class Controls(Serialisable):
    tagname: str
    control: Incomplete
    __elements__: Incomplete
    def __init__(self, control=()) -> None: ...
