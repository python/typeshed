from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.text import RichText
from openpyxl.descriptors import Typed
from openpyxl.descriptors.base import Alias, Bool, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.geometry import ShapeStyle
from openpyxl.drawing.properties import NonVisualDrawingProps, NonVisualDrawingShapeProps

class Connection(Serialisable):
    id: Incomplete
    idx: Incomplete
    def __init__(self, id: Incomplete | None = None, idx: Incomplete | None = None) -> None: ...

class ConnectorLocking(Serialisable):
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(self, extLst: ExtensionList | None = None) -> None: ...

class NonVisualConnectorProperties(Serialisable):
    cxnSpLocks: Typed[ConnectorLocking, Literal[True]]
    stCxn: Typed[Connection, Literal[True]]
    endCxn: Typed[Connection, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    def __init__(
        self,
        cxnSpLocks: ConnectorLocking | None = None,
        stCxn: Connection | None = None,
        endCxn: Connection | None = None,
        extLst: ExtensionList | None = None,
    ) -> None: ...

class ConnectorNonVisual(Serialisable):
    cNvPr: Typed[NonVisualDrawingProps, Literal[False]]
    cNvCxnSpPr: Typed[NonVisualConnectorProperties, Literal[False]]
    __elements__: Incomplete
    def __init__(self, cNvPr: NonVisualDrawingProps, cNvCxnSpPr: NonVisualConnectorProperties) -> None: ...

class ConnectorShape(Serialisable):
    tagname: str
    nvCxnSpPr: Typed[ConnectorNonVisual, Literal[False]]
    spPr: Typed[GraphicalProperties, Literal[False]]
    style: Typed[ShapeStyle, Literal[True]]
    macro: Incomplete
    fPublished: Bool[Literal[True]]
    def __init__(
        self,
        nvCxnSpPr: ConnectorNonVisual,
        spPr: GraphicalProperties,
        style: ShapeStyle | None = None,
        macro: Incomplete | None = None,
        fPublished: _ConvertibleToBool | None = None,
    ) -> None: ...

class ShapeMeta(Serialisable):
    tagname: str
    cNvPr: Typed[NonVisualDrawingProps, Literal[False]]
    cNvSpPr: Typed[NonVisualDrawingShapeProps, Literal[False]]
    def __init__(self, cNvPr: NonVisualDrawingProps, cNvSpPr: NonVisualDrawingShapeProps) -> None: ...

class Shape(Serialisable):
    macro: Incomplete
    textlink: Incomplete
    fPublished: Bool[Literal[True]]
    fLocksText: Bool[Literal[True]]
    nvSpPr: Typed[ShapeMeta, Literal[True]]
    meta: Alias
    spPr: Typed[GraphicalProperties, Literal[False]]
    graphicalProperties: Alias
    style: Typed[ShapeStyle, Literal[True]]
    txBody: Typed[RichText, Literal[True]]
    def __init__(
        self,
        macro: Incomplete | None,
        textlink: Incomplete | None,
        fPublished: _ConvertibleToBool | None,
        fLocksText: _ConvertibleToBool | None,
        nvSpPr: ShapeMeta | None,
        spPr: GraphicalProperties,
        style: ShapeStyle | None = None,
        txBody: RichText | None = None,
    ) -> None: ...
