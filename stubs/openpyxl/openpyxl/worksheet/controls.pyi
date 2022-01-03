from typing import Any

from openpyxl.descriptors import Bool as Bool, Integer as Integer, Sequence as Sequence, String as String, Typed as Typed
from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

from .ole import ObjectAnchor as ObjectAnchor

class ControlProperty(Serialisable):
    tagname: str
    anchor: Any
    locked: Any
    defaultSize: Any
    disabled: Any
    recalcAlways: Any
    uiObject: Any
    autoFill: Any
    autoLine: Any
    autoPict: Any
    macro: Any
    altText: Any
    linkedCell: Any
    listFillRange: Any
    cf: Any
    id: Any
    __elements__: Any
    def __init__(
        self,
        anchor: Any | None = ...,
        locked: bool = ...,
        defaultSize: bool = ...,
        _print: bool = ...,
        disabled: bool = ...,
        recalcAlways: bool = ...,
        uiObject: bool = ...,
        autoFill: bool = ...,
        autoLine: bool = ...,
        autoPict: bool = ...,
        macro: Any | None = ...,
        altText: Any | None = ...,
        linkedCell: Any | None = ...,
        listFillRange: Any | None = ...,
        cf: str = ...,
        id: Any | None = ...,
    ) -> None: ...

class Control(Serialisable):
    tagname: str
    controlPr: Any
    shapeId: Any
    name: Any
    __elements__: Any
    def __init__(self, controlPr: Any | None = ..., shapeId: Any | None = ..., name: Any | None = ...) -> None: ...

class Controls(Serialisable):
    tagname: str
    control: Any
    __elements__: Any
    def __init__(self, control=...) -> None: ...
