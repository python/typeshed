import _typeshed
import sys
import types
from _typeshed import SupportsKeysAndGetItem, Unused
from abc import ABCMeta
from builtins import property as _builtins_property
from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal, Self, TypeAlias

__all__ = ["EnumMeta", "Enum", "IntEnum", "Flag", "IntFlag", "auto", "unique"]

if sys.version_info >= (3, 11):
    __all__ += [
        "CONFORM",
        "CONTINUOUS",
        "EJECT",
        "EnumCheck",
        "EnumType",
        "FlagBoundary",
        "KEEP",
        "NAMED_FLAGS",
        "ReprEnum",
        "STRICT",
        "StrEnum",
        "UNIQUE",
        "global_enum",
        "global_enum_repr",
        "global_flag_repr",
        "global_str",
        "member",
        "nonmember",
        "property",
        "verify",
    ]

if sys.version_info >= (3, 12):
    __all__ += ["pickle_by_enum_name", "pickle_by_global_name"]

_EnumMemberT = TypeVar("_EnumMemberT")
_EnumerationT = TypeVar("_EnumerationT", bound=type[Enum])

# The following all work:
# >>> from enum import Enum
# >>> from string import ascii_lowercase
# >>> Enum('Foo', names='RED YELLOW GREEN')
# <enum 'Foo'>
# >>> Enum('Foo', names=[('RED', 1), ('YELLOW, 2)])
# <enum 'Foo'>
# >>> Enum('Foo', names=((x for x in (ascii_lowercase[i], i)) for i in range(5)))
# <enum 'Foo'>
# >>> Enum('Foo', names={'RED': 1, 'YELLOW': 2})
# <enum 'Foo'>
_EnumNames: TypeAlias = str | Iterable[str] | Iterable[Iterable[str | Any]] | Mapping[str, Any]

if sys.version_info >= (3, 11):
    class nonmember(Generic[_EnumMemberT]):
        value: _EnumMemberT
        def __init__(self, value: _EnumMemberT) -> None: ...

    class member(Generic[_EnumMemberT]):
        value: _EnumMemberT
        def __init__(self, value: _EnumMemberT) -> None: ...

class _EnumDict(dict[str, Any]):
    def __init__(self) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    if sys.version_info >= (3, 11):
        # See comment above `typing.MutableMapping.update`
        # for why overloads are preferable to a Union here
        #
        # Unlike with MutableMapping.update(), the first argument is required,
        # hence the type: ignore
        @overload  # type: ignore[override]
        def update(self, members: SupportsKeysAndGetItem[str, Any], **more_members: Any) -> None: ...
        @overload
        def update(self, members: Iterable[tuple[str, Any]], **more_members: Any) -> None: ...

# Note: EnumMeta actually subclasses type directly, not ABCMeta.
# This is a temporary workaround to allow multiple creation of enums with builtins
# such as str as mixins, which due to the handling of ABCs of builtin types, cause
# spurious inconsistent metaclass structure. See #1595.
# Structurally: Iterable[T], Reversible[T], Container[T] where T is the enum itself
class EnumMeta(ABCMeta):
    if sys.version_info >= (3, 11):
        def __new__(
            metacls: type[_typeshed.Self],
            cls: str,
            bases: tuple[type, ...],
            classdict: _EnumDict,
            *,
            boundary: FlagBoundary | None = None,
            _simple: bool = False,
            **kwds: Any,
        ) -> _typeshed.Self: ...
    elif sys.version_info >= (3, 9):
        def __new__(
            metacls: type[_typeshed.Self], cls: str, bases: tuple[type, ...], classdict: _EnumDict, **kwds: Any
        ) -> _typeshed.Self: ...
    else:
        def __new__(metacls: type[_typeshed.Self], cls: str, bases: tuple[type, ...], classdict: _EnumDict) -> _typeshed.Self: ...

    if sys.version_info >= (3, 9):
        @classmethod
        def __prepare__(metacls, cls: str, bases: tuple[type, ...], **kwds: Any) -> _EnumDict: ...  # type: ignore[override]
    else:
        @classmethod
        def __prepare__(metacls, cls: str, bases: tuple[type, ...]) -> _EnumDict: ...  # type: ignore[override]

    def __iter__(self: type[_EnumMemberT]) -> Iterator[_EnumMemberT]: ...
    def __reversed__(self: type[_EnumMemberT]) -> Iterator[_EnumMemberT]: ...
    if sys.version_info >= (3, 12):
        def __contains__(self: type[Any], value: object) -> bool: ...
    elif sys.version_info >= (3, 11):
        def __contains__(self: type[Any], member: object) -> bool: ...
    elif sys.version_info >= (3, 10):
        def __contains__(self: type[Any], obj: object) -> bool: ...
    else:
        def __contains__(self: type[Any], member: object) -> bool: ...

    def __getitem__(self: type[_EnumMemberT], name: str) -> _EnumMemberT: ...
    @_builtins_property
    def __members__(self: type[_EnumMemberT]) -> types.MappingProxyType[str, _EnumMemberT]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> Literal[True]: ...
    def __dir__(self) -> list[str]: ...
    # Simple value lookup
    @overload
    def __call__(cls: type[_EnumMemberT], value: Any, names: None = None) -> _EnumMemberT: ...
    # Functional Enum API
    if sys.version_info >= (3, 11):
        @overload
        def __call__(
            cls,
            value: str,
            names: _EnumNames,
            *,
            module: str | None = None,
            qualname: str | None = None,
            type: type | None = None,
            start: int = 1,
            boundary: FlagBoundary | None = None,
        ) -> type[Enum]: ...
    else:
        @overload
        def __call__(
            cls,
            value: str,
            names: _EnumNames,
            *,
            module: str | None = None,
            qualname: str | None = None,
            type: type | None = None,
            start: int = 1,
        ) -> type[Enum]: ...
    _member_names_: list[str]  # undocumented
    _member_map_: dict[str, Enum]  # undocumented
    _value2member_map_: dict[Any, Enum]  # undocumented

if sys.version_info >= (3, 11):
    # In 3.11 `EnumMeta` metaclass is renamed to `EnumType`, but old name also exists.
    EnumType = EnumMeta

    class property(types.DynamicClassAttribute):
        def __set_name__(self, ownerclass: type[Enum], name: str) -> None: ...
        name: str
        clsname: str
    _magic_enum_attr = property
else:
    _magic_enum_attr = types.DynamicClassAttribute

class Enum(metaclass=EnumMeta):
    @_magic_enum_attr
    def name(self) -> str: ...
    @_magic_enum_attr
    def value(self) -> Any: ...
    _name_: str
    _value_: Any
    _ignore_: str | list[str]
    _order_: str
    __order__: str
    @classmethod
    def _missing_(cls, value: object) -> Any: ...
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any: ...
    # It's not true that `__new__` will accept any argument type,
    # so ideally we'd use `Any` to indicate that the argument type is inexpressible.
    # However, using `Any` causes too many false-positives for those using mypy's `--disallow-any-expr`
    # (see #7752, #2539, mypy/#5788),
    # and in practice using `object` here has the same effect as using `Any`.
    def __new__(cls, value: object) -> Self: ...
    def __dir__(self) -> list[str]: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __reduce_ex__(self, proto: Unused) -> tuple[Any, ...]: ...
    if sys.version_info >= (3, 12):
        def __copy__(self) -> Self: ...
        def __deepcopy(self, memo: Any) -> Self: ...

if sys.version_info >= (3, 11):
    class ReprEnum(Enum): ...

if sys.version_info >= (3, 11):
    _IntEnumBase = ReprEnum
else:
    _IntEnumBase = Enum

class IntEnum(int, _IntEnumBase):
    _value_: int
    @_magic_enum_attr
    def value(self) -> int: ...
    def __new__(cls, value: int) -> Self: ...

def unique(enumeration: _EnumerationT) -> _EnumerationT: ...

_auto_null: Any

class Flag(Enum):
    _name_: str | None  # type: ignore[assignment]
    _value_: int
    @_magic_enum_attr
    def name(self) -> str | None: ...  # type: ignore[override]
    @_magic_enum_attr
    def value(self) -> int: ...
    def __contains__(self, other: Self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __or__(self, other: Self) -> Self: ...
    def __and__(self, other: Self) -> Self: ...
    def __xor__(self, other: Self) -> Self: ...
    def __invert__(self) -> Self: ...
    if sys.version_info >= (3, 11):
        def __iter__(self) -> Iterator[Self]: ...
        def __len__(self) -> int: ...
        __ror__ = __or__
        __rand__ = __and__
        __rxor__ = __xor__

if sys.version_info >= (3, 11):
    class StrEnum(str, ReprEnum):
        def __new__(cls, value: str) -> Self: ...
        _value_: str
        @_magic_enum_attr
        def value(self) -> str: ...
        @staticmethod
        def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str: ...

    class EnumCheck(StrEnum):
        CONTINUOUS: str
        NAMED_FLAGS: str
        UNIQUE: str
    CONTINUOUS = EnumCheck.CONTINUOUS
    NAMED_FLAGS = EnumCheck.NAMED_FLAGS
    UNIQUE = EnumCheck.UNIQUE

    class verify:
        def __init__(self, *checks: EnumCheck) -> None: ...
        def __call__(self, enumeration: _EnumerationT) -> _EnumerationT: ...

    class FlagBoundary(StrEnum):
        STRICT: str
        CONFORM: str
        EJECT: str
        KEEP: str
    STRICT = FlagBoundary.STRICT
    CONFORM = FlagBoundary.CONFORM
    EJECT = FlagBoundary.EJECT
    KEEP = FlagBoundary.KEEP

    def global_str(self: Enum) -> str: ...
    def global_enum(cls: _EnumerationT, update_str: bool = False) -> _EnumerationT: ...
    def global_enum_repr(self: Enum) -> str: ...
    def global_flag_repr(self: Flag) -> str: ...

if sys.version_info >= (3, 11):
    # The body of the class is the same, but the base classes are different.
    class IntFlag(int, ReprEnum, Flag, boundary=KEEP):  # type: ignore[misc]  # complaints about incompatible bases
        def __new__(cls, value: int) -> Self: ...
        def __or__(self, other: int) -> Self: ...
        def __and__(self, other: int) -> Self: ...
        def __xor__(self, other: int) -> Self: ...
        __ror__ = __or__
        __rand__ = __and__
        __rxor__ = __xor__

else:
    class IntFlag(int, Flag):  # type: ignore[misc]  # complaints about incompatible bases
        def __new__(cls, value: int) -> Self: ...
        def __or__(self, other: int) -> Self: ...
        def __and__(self, other: int) -> Self: ...
        def __xor__(self, other: int) -> Self: ...
        __ror__ = __or__
        __rand__ = __and__
        __rxor__ = __xor__

# subclassing IntFlag so it picks up all implemented base functions, best modeling behavior of enum.auto()
class auto(IntFlag):
    _value_: Any
    @_magic_enum_attr
    def value(self) -> Any: ...
    def __new__(cls) -> Self: ...

if sys.version_info >= (3, 12):
    def pickle_by_global_name(self: Enum, proto: int) -> str: ...
    def pickle_by_enum_name(self: _EnumMemberT, proto: int) -> tuple[Callable[..., Any], tuple[type[_EnumMemberT], str]]: ...
