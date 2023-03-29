from _typeshed import Incomplete
from datetime import datetime
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal

_T = TypeVar("_T")
_N = TypeVar("_N", bound=bool)

class Descriptor(Generic[_T]):
    name: Incomplete | None
    def __init__(self, name: Incomplete | None = None, **kw) -> None: ...
    def __get__(self, obj: Any, objtype: type | None = None) -> _T: ...
    def __set__(self, obj: Any, value: _T) -> None: ...

class Typed(Descriptor[_T], Generic[_T, _N]):
    expected_type: type[_T]
    allow_none: _N
    nested: bool
    __doc__: Incomplete

    @overload
    def __init__(
        self: Typed[_T, Literal[True]],
        name: Incomplete | None = None,
        *,
        expected_type: type[_T] | tuple[type[_T], ...],
        allow_none: Literal[True],
        nested: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Typed[_T, Literal[False]],
        name: Incomplete | None = None,
        *,
        expected_type: type[_T] | tuple[type[_T], ...],
        allow_none: Literal[False] = False,
        nested: bool = False,
    ) -> None: ...
    @overload
    def __get__(self: Typed[_T, Literal[True]], obj: Any, objtype: type | None = None) -> _T | None: ...
    @overload
    def __get__(self: Typed[_T, Literal[False]], obj: Any, objtype: type | None = None) -> _T: ...
    @overload
    def __set__(self: Typed[_T, Literal[True]], obj: Any, value: _T | None) -> None: ...
    @overload
    def __set__(self: Typed[_T, Literal[False]], obj: Any, value: _T) -> None: ...

class Convertible(Typed):
    def __set__(self, instance, value) -> None: ...

class Max(Convertible):
    expected_type: Incomplete
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Min(Convertible):
    expected_type: Incomplete
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class MinMax(Min, Max): ...

class Set(Descriptor):
    __doc__: Incomplete
    def __init__(self, name: Incomplete | None = None, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class NoneSet(Set):
    def __init__(self, name: Incomplete | None = None, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Integer(Convertible):
    expected_type: Incomplete

class Float(Convertible):
    expected_type: Incomplete

class Bool(Convertible):
    expected_type: Incomplete
    def __set__(self, instance, value) -> None: ...

class String(Typed):
    expected_type: type[str]

class Text(String, Convertible): ...

class ASCII(Typed):
    expected_type: type[bytes]

class Tuple(Typed):
    expected_type: type[tuple[Any, ...]]

class Length(Descriptor):
    def __init__(self, name: Incomplete | None = None, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Default(Typed):
    def __init__(self, name: Incomplete | None = None, **kw) -> None: ...
    def __call__(self): ...

class Alias(Descriptor):
    alias: Incomplete
    def __init__(self, alias) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class MatchPattern(Descriptor):
    allow_none: bool
    test_pattern: Incomplete
    def __init__(self, name: Incomplete | None = None, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class DateTime(Typed):
    expected_type: type[datetime]
    def __set__(self, instance, value) -> None: ...
