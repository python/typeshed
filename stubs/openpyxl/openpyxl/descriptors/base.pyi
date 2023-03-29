from _typeshed import Incomplete, Unused
from collections.abc import Iterable
from datetime import datetime
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal

from openpyxl.descriptors.serialisable import Serialisable

_T = TypeVar("_T")
_N = TypeVar("_N", bound=bool)

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
        expected_type: type[_T] | tuple[type[_T], ...],
        allow_none: Literal[True],
        nested: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Typed[_T, Literal[False]],
        name: str | None = None,
        *,
        expected_type: type[_T] | tuple[type[_T], ...],
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

class Convertible(Typed):
    def __set__(self, instance: Serialisable, value) -> None: ...

class Max(Convertible):
    expected_type: Incomplete
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance: Serialisable, value) -> None: ...

class Min(Convertible):
    expected_type: Incomplete
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance: Serialisable, value) -> None: ...

class MinMax(Min, Max): ...

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

class Bool(Convertible):
    expected_type: Incomplete
    def __set__(self, instance: Serialisable, value) -> None: ...

class String(Typed):
    expected_type: type[str]

class Text(String, Convertible): ...

class ASCII(Typed):
    expected_type: type[bytes]

class Tuple(Typed):
    expected_type: type[tuple[Any, ...]]

class Length(Descriptor):
    def __init__(self, name: str | None = None, **kw) -> None: ...
    def __set__(self, instance: Serialisable, value) -> None: ...

class Default(Typed):
    def __init__(self, name: str | None = None, **kw) -> None: ...
    def __call__(self): ...

class Alias(Descriptor):
    alias: Incomplete
    def __init__(self, alias) -> None: ...
    def __set__(self, instance: Serialisable, value) -> None: ...
    def __get__(self, instance: Serialisable, cls: Unused): ...

class MatchPattern(Descriptor):
    allow_none: bool
    test_pattern: Incomplete
    def __init__(self, name: str | None = None, **kw) -> None: ...
    def __set__(self, instance: Serialisable, value) -> None: ...

class DateTime(Typed):
    expected_type: type[datetime]
    def __set__(self, instance: Serialisable, value) -> None: ...
