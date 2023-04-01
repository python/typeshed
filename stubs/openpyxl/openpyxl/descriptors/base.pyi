from _typeshed import Incomplete, ReadableBuffer, SupportsTrunc, Unused
from collections.abc import Iterable, Sized
from datetime import datetime
from re import Pattern
from typing import Any, Generic, SupportsFloat, SupportsInt, TypeVar, overload
from typing_extensions import Literal, SupportsIndex, TypeAlias

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.fill import Blip
from openpyxl.worksheet.cell_range import CellRange, MultiCellRange

_T = TypeVar("_T")
_P = TypeVar("_P", str, ReadableBuffer)
_N = TypeVar("_N", bound=bool)
_L = TypeVar("_L", bound=Sized)
_M = TypeVar("_M", int, float)

_ExpectedTypeParam: TypeAlias = type[_T] | tuple[type[_T], ...]
_ConvertibleToMultiCellRange: TypeAlias = MultiCellRange | str | Iterable[CellRange]
_ConvertibleToInt: TypeAlias = int | str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc
_ConvertibleToFloat: TypeAlias = float | SupportsFloat | SupportsIndex | str | ReadableBuffer
# Since everything is convertible to a bool, this restricts to only intended expected types, allowing None restrictions
_ConvertibleToBool: TypeAlias = bool | str | int

class Descriptor(Generic[_T]):
    name: str | None
    def __init__(self, name: str | None = None, **kw: object) -> None: ...
    def __get__(self, instance: Serialisable, cls: type | None) -> _T: ...
    def __set__(self, instance: Serialisable, value: _T) -> None: ...

class Typed(Descriptor[_T], Generic[_T, _N]):
    expected_type: type[_T]
    allow_none: _N
    nested: bool
    __doc__: Incomplete

    @overload
    def __init__(
        self: Typed[_T, Literal[True]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        allow_none: Literal[True],
        nested: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Typed[_T, Literal[False]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        allow_none: Literal[False] = False,
        nested: bool = False,
    ) -> None: ...
    @overload
    def __get__(self: Typed[_T, Literal[True]], instance: Serialisable, objtype: type | None = None) -> _T | None: ...
    @overload
    def __get__(self: Typed[_T, Literal[False]], instance: Serialisable, objtype: type | None = None) -> _T: ...
    @overload
    def __set__(self: Typed[_T, Literal[True]], instance: Serialisable, value: _T | None) -> None: ...
    @overload
    def __set__(self: Typed[_T, Literal[False]], instance: Serialisable, value: _T) -> None: ...

class Convertible(Typed[_T, _N]):
    @overload
    def __init__(
        self: Convertible[_T, Literal[True]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        allow_none: Literal[True],
        nested: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Convertible[_T, Literal[False]],
        name: str | None = None,
        *,
        expected_type: _ExpectedTypeParam[_T],
        allow_none: Literal[False] = False,
        nested: bool = False,
    ) -> None: ...
    # NOTE: It is currently impossible to make a generic based on the parameter type of another generic
    # So we implement explicitely the types used internally
    # MultiCellRange
    @overload
    def __set__(
        self: Convertible[MultiCellRange, Literal[True]], instance: Serialisable, value: _ConvertibleToMultiCellRange | None
    ) -> None: ...
    @overload
    def __set__(
        self: Convertible[MultiCellRange, Literal[False]], instance: Serialisable, value: _ConvertibleToMultiCellRange
    ) -> None: ...
    # str | Blip
    @overload
    def __set__(
        self: Convertible[str, bool] | Convertible[Blip, bool], instance: Serialisable, value: object  # Not[None] when _N = False
    ) -> None: ...
    # bool
    @overload
    def __set__(self: Convertible[bool, Literal[True]], instance: Serialisable, value: _ConvertibleToBool | None) -> None: ...
    # int
    @overload
    def __set__(self: Convertible[int, Literal[True]], instance: Serialisable, value: _ConvertibleToInt | None) -> None: ...
    @overload
    def __set__(self: Convertible[int, Literal[False]], instance: Serialisable, value: _ConvertibleToInt) -> None: ...
    # float
    @overload
    def __set__(self: Convertible[float, Literal[True]], instance: Serialisable, value: _ConvertibleToFloat | None) -> None: ...
    @overload
    def __set__(self: Convertible[float, Literal[False]], instance: Serialisable, value: _ConvertibleToFloat) -> None: ...
    # Anything else
    @overload
    def __set__(self: Convertible[_T, Literal[True]], instance: Serialisable, value: _T | int | Any | None) -> None: ...

class Max(Convertible[_M, _N], Generic[_M, _N]):
    expected_type: type[_M]
    allow_none: _N
    @overload
    def __init__(
        self: Max[int, Literal[True]], *, expected_type: _ExpectedTypeParam[int], allow_none: Literal[True], max: float
    ) -> None: ...
    @overload
    def __init__(
        self: Max[int, Literal[False]], *, expected_type: _ExpectedTypeParam[int], allow_none: Literal[False] = False, max: float
    ) -> None: ...
    # mypy can't infer type from `expected_type = float` (pyright can), so we have to add extra overloads
    @overload
    def __init__(
        self: Max[float, Literal[True]], *, expected_type: _ExpectedTypeParam[float] = ..., allow_none: Literal[True], max: float
    ) -> None: ...
    @overload
    def __init__(
        self: Max[float, Literal[False]],
        *,
        expected_type: _ExpectedTypeParam[float] = ...,
        allow_none: Literal[False] = False,
        max: float,
    ) -> None: ...
    @overload  # type:ignore[override]  # Different restrictions
    def __set__(self: Max[int, Literal[True]], instance: Serialisable, value: _ConvertibleToInt | None) -> None: ...
    @overload
    def __set__(self: Max[int, Literal[False]], instance: Serialisable, value: _ConvertibleToInt) -> None: ...
    @overload
    def __set__(self: Max[float, Literal[True]], instance: Serialisable, value: _ConvertibleToFloat | None) -> None: ...
    @overload
    def __set__(self: Max[float, Literal[False]], instance: Serialisable, value: _ConvertibleToFloat) -> None: ...

class Min(Convertible[_M, _N], Generic[_M, _N]):
    expected_type: type[_M]
    allow_none: _N
    @overload
    def __init__(
        self: Min[int, Literal[True]], *, expected_type: _ExpectedTypeParam[int], allow_none: Literal[True], max: float
    ) -> None: ...
    @overload
    def __init__(
        self: Min[int, Literal[False]], *, expected_type: _ExpectedTypeParam[int], allow_none: Literal[False] = False, max: float
    ) -> None: ...
    # mypy can't infer type from `expected_type = float` (pyright can), so we have to add extra overloads
    @overload
    def __init__(
        self: Min[float, Literal[True]], *, expected_type: _ExpectedTypeParam[float] = ..., allow_none: Literal[True], max: float
    ) -> None: ...
    @overload
    def __init__(
        self: Min[float, Literal[False]],
        *,
        expected_type: _ExpectedTypeParam[float] = ...,
        allow_none: Literal[False] = False,
        max: float,
    ) -> None: ...
    @overload  # type:ignore[override]  # Different restrictions
    def __set__(self: Min[int, Literal[True]], instance: Serialisable, value: _ConvertibleToInt | None) -> None: ...
    @overload
    def __set__(self: Min[int, Literal[False]], instance: Serialisable, value: _ConvertibleToInt) -> None: ...
    @overload
    def __set__(self: Min[float, Literal[True]], instance: Serialisable, value: _ConvertibleToFloat | None) -> None: ...
    @overload
    def __set__(self: Min[float, Literal[False]], instance: Serialisable, value: _ConvertibleToFloat) -> None: ...

class MinMax(Min[_M, _N], Max[_M, _N], Generic[_M, _N]):
    expected_type: type[_M]
    allow_none: _N
    @overload
    def __init__(
        self: MinMax[int, Literal[True]],
        *,
        expected_type: _ExpectedTypeParam[int],
        allow_none: Literal[True],
        min: float,
        max: float,
    ) -> None: ...
    @overload
    def __init__(
        self: MinMax[int, Literal[False]],
        *,
        expected_type: _ExpectedTypeParam[int],
        allow_none: Literal[False] = False,
        min: float,
        max: float,
    ) -> None: ...
    # mypy can't infer type from `expected_type = float` (pyright can), so we have to add extra overloads
    @overload
    def __init__(
        self: MinMax[float, Literal[True]],
        *,
        expected_type: _ExpectedTypeParam[float] = ...,
        allow_none: Literal[True],
        min: float,
        max: float,
    ) -> None: ...
    @overload
    def __init__(
        self: MinMax[float, Literal[False]],
        *,
        expected_type: _ExpectedTypeParam[float] = ...,
        allow_none: Literal[False] = False,
        min: float,
        max: float,
    ) -> None: ...

class Set(Descriptor[_T]):
    __doc__: str
    def __init__(self, name: str | None = None, *, values: Iterable[_T]) -> None: ...
    def __set__(self, instance: Serialisable, value: _T) -> None: ...

class NoneSet(Set[_T | None]):
    def __init__(self, name: str | None = None, *, values: Iterable[_T | None]) -> None: ...
    def __set__(self, instance: Serialisable, value: _T | Literal["none"] | None) -> None: ...

class Integer(Convertible):
    expected_type: Incomplete

class Float(Convertible):
    expected_type: Incomplete

class Bool(Convertible[bool, _N]):
    expected_type: type[bool]
    allow_none: _N
    @overload
    def __init__(self: Bool[Literal[True]], name: str | None = None, *, allow_none: Literal[True]) -> None: ...
    @overload
    def __init__(self: Bool[Literal[False]], name: str | None = None, *, allow_none: Literal[False] = False) -> None: ...
    @overload  # type:ignore[override]  # Different restrictions
    def __set__(self: Bool[Literal[True]], instance: Serialisable, value: _ConvertibleToBool | None) -> None: ...
    @overload
    def __set__(self: Bool[Literal[False]], instance: Serialisable, value: _ConvertibleToBool) -> None: ...

class String(Typed):
    expected_type: type[str]

class Text(String, Convertible): ...

class ASCII(Typed):
    expected_type: type[bytes]

class Tuple(Typed):
    expected_type: type[tuple[Any, ...]]

class Length(Descriptor[_L]):
    def __init__(self, name: Unused = None, *, length: int) -> None: ...
    def __set__(self, instance: Serialisable, value: _L) -> None: ...

class Default(Typed):
    def __init__(self, name: str | None = None, **kw) -> None: ...
    def __call__(self): ...

# Note: Aliases types can't be infered. Anyway an alias means there's another option
# incomplete: Make it generic with explicit getter/setter type arguments ?
class Alias(Descriptor[Incomplete]):
    alias: str
    def __init__(self, alias: str) -> None: ...
    def __set__(self, instance: Serialisable, value: Incomplete) -> None: ...
    def __get__(self, instance: Serialisable, cls: Unused): ...

class MatchPattern(Descriptor[_P], Generic[_P, _N]):
    allow_none: _N
    test_pattern: Pattern[bytes] | Pattern[str]

    @overload  # str
    def __init__(
        self: MatchPattern[str, Literal[True]], name: str | None = None, *, pattern: str | Pattern[str], allow_none: Literal[True]
    ) -> None: ...
    @overload  # str | None
    def __init__(
        self: MatchPattern[str, Literal[False]],
        name: str | None = None,
        *,
        pattern: str | Pattern[str],
        allow_none: Literal[False] = False,
    ) -> None: ...
    @overload  # bytes
    def __init__(
        self: MatchPattern[ReadableBuffer, Literal[True]],
        name: str | None = None,
        *,
        pattern: bytes | Pattern[bytes],
        allow_none: Literal[True],
    ) -> None: ...
    @overload  # bytes | None
    def __init__(
        self: MatchPattern[ReadableBuffer, Literal[False]],
        name: str | None = None,
        *,
        pattern: bytes | Pattern[bytes],
        allow_none: Literal[False] = False,
    ) -> None: ...
    @overload
    def __get__(self: MatchPattern[_P, Literal[True]], instance: Serialisable, objtype: type | None = None) -> _P | None: ...
    @overload
    def __get__(self: MatchPattern[_P, Literal[False]], instance: Serialisable, objtype: type | None = None) -> _P: ...
    @overload
    def __set__(self: MatchPattern[_P, Literal[True]], instance: Serialisable, value: _P | None) -> None: ...
    @overload
    def __set__(self: MatchPattern[_P, Literal[False]], instance: Serialisable, value: _P) -> None: ...

class DateTime(Typed[datetime, _N], Generic[_N]):
    allow_none: _N
    expected_type: type[datetime]
    @overload
    def __init__(self: DateTime[Literal[True]], name: str | None = None, *, allow_none: Literal[True]) -> None: ...
    @overload
    def __init__(self: DateTime[Literal[False]], name: str | None = None, *, allow_none: Literal[False] = False) -> None: ...
    @overload
    def __set__(self: DateTime[Literal[True]], instance: Serialisable, value: datetime | str | None) -> None: ...
    @overload
    def __set__(self: DateTime[Literal[False]], instance: Serialisable, value: datetime | str) -> None: ...
