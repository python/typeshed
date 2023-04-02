from _typeshed import Incomplete, Unused
from collections.abc import Callable, Iterator
from typing import ClassVar, Generic, TypeVar
from typing_extensions import Literal, Self

from openpyxl.descriptors import Strict
from openpyxl.descriptors.base import Alias, Bool, Float, Integer, String, _ConvertibleToBool
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles.styleable import StyleableObject
from openpyxl.utils.bound_dictionary import BoundDictionary
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.xml.functions import Element

_DimT = TypeVar("_DimT", bound=Dimension)

class Dimension(Strict, StyleableObject):
    __fields__: ClassVar[tuple[str, ...]]

    index: Integer
    hidden: Bool[Literal[False]]
    outlineLevel: Integer
    outline_level: Alias
    collapsed: Bool[Literal[False]]
    style: Alias

    def __init__(
        self,
        index: int,
        hidden: _ConvertibleToBool,
        outlineLevel: int | None,
        collapsed: _ConvertibleToBool,
        worksheet: Worksheet,
        visible: Unused = True,
        style: Incomplete | None = None,
    ) -> None: ...
    def __iter__(self) -> Iterator[tuple[str, str]]: ...
    def __copy__(self) -> Self: ...

class RowDimension(Dimension):
    r: Alias
    s: Alias
    ht: Float
    height: Alias
    thickBot: Bool[Literal[False]]
    thickTop: Bool[Literal[False]]

    def __init__(
        self,
        worksheet: Worksheet,
        index: int,
        ht: Incomplete | None,
        customHeight: Unused,
        s: Incomplete | None,
        customFormat: Unused,
        hidden: bool,
        outlineLevel: int,
        outline_level: Incomplete | None,
        collapsed: bool,
        visible: Incomplete | None,
        height: Incomplete | None,
        r: Incomplete | None,
        spans: Unused,
        thickBot: _ConvertibleToBool,
        thickTop: _ConvertibleToBool,
        **kw: Unused,
    ) -> None: ...
    @property
    def customFormat(self) -> bool: ...
    @property
    def customHeight(self) -> bool: ...

class ColumnDimension(Dimension):
    width: Float
    bestFit: Bool[Literal[False]]
    auto_size: Alias
    index: String[Literal[False]]  # type:ignore[assignment]
    min: Integer
    max: Integer
    collapsed: Bool[Literal[False]]

    def __init__(
        self,
        worksheet: Worksheet,
        index: str = "A",
        width: int = 13,
        bestFit: _ConvertibleToBool = False,
        hidden: bool = False,
        outlineLevel: int = 0,
        outline_level: int | None = None,
        collapsed: _ConvertibleToBool = False,
        style: Incomplete | None = None,
        min: int | None = None,
        max: int | None = None,
        customWidth: Unused = False,
        visible: bool | None = None,
        auto_size: _ConvertibleToBool | None = None,
    ) -> None: ...
    @property
    def customWidth(self) -> bool: ...
    def reindex(self) -> None: ...
    def to_tree(self) -> Element | None: ...

class DimensionHolder(BoundDictionary[str, _DimT], Generic[_DimT]):
    worksheet: Worksheet
    max_outline: int | None
    default_factory: Callable[[], _DimT] | None

    def __init__(
        self, worksheet: Worksheet, reference: str = "index", default_factory: Callable[[], _DimT] | None = None
    ) -> None: ...
    def group(self, start: str, end: str | None = None, outline_level: int = 1, hidden: bool = False) -> None: ...
    def to_tree(self) -> Element | None: ...

class SheetFormatProperties(Serialisable):
    tagname: str
    baseColWidth: Incomplete
    defaultColWidth: Incomplete
    defaultRowHeight: Incomplete
    customHeight: Bool[Literal[True]]
    zeroHeight: Bool[Literal[True]]
    thickTop: Bool[Literal[True]]
    thickBottom: Bool[Literal[True]]
    outlineLevelRow: Incomplete
    outlineLevelCol: Incomplete
    def __init__(
        self,
        baseColWidth: int = 8,
        defaultColWidth: Incomplete | None = None,
        defaultRowHeight: int = 15,
        customHeight: _ConvertibleToBool | None = None,
        zeroHeight: _ConvertibleToBool | None = None,
        thickTop: _ConvertibleToBool | None = None,
        thickBottom: _ConvertibleToBool | None = None,
        outlineLevelRow: Incomplete | None = None,
        outlineLevelCol: Incomplete | None = None,
    ) -> None: ...

class SheetDimension(Serialisable):
    tagname: str
    ref: String[Literal[False]]
    def __init__(self, ref: str) -> None: ...
    @property
    def boundaries(self): ...
