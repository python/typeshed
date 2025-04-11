# Internals used by some type checkers.
#
# Don't use this module directly. It is only for type checkers to use.

import sys
import typing_extensions
from _collections_abc import dict_items, dict_keys, dict_values
from abc import ABCMeta
from collections.abc import Awaitable, Generator, Mapping
from types import CellType, CodeType
from typing import Any, ClassVar, Generic, TypeVar, final, overload
from typing_extensions import Never, ParamSpec, TypeVarTuple

_T = TypeVar("_T")

# Used for an undocumented mypy feature. Does not exist at runtime.
_promote = object()

# Internal mypy fallback type for all typed dicts.
# N.B. Keep this mostly in sync with typing_extensions._TypedDict/mypy_extensions._TypedDict
class _TypedDict(Mapping[str, object], metaclass=ABCMeta):
    __total__: ClassVar[bool]
    __required_keys__: ClassVar[frozenset[str]]
    __optional_keys__: ClassVar[frozenset[str]]
    # __orig_bases__ sometimes exists on <3.12, but not consistently,
    # so we only add it to the stub on 3.12+
    if sys.version_info >= (3, 12):
        __orig_bases__: ClassVar[tuple[Any, ...]]
    if sys.version_info >= (3, 13):
        __readonly_keys__: ClassVar[frozenset[str]]
        __mutable_keys__: ClassVar[frozenset[str]]

    def copy(self) -> typing_extensions.Self: ...
    # Using Never so that only calls using mypy plugin hook that specialize the signature
    # can go through.
    def setdefault(self, k: Never, default: object) -> object: ...
    # Mypy plugin hook for 'pop' expects that 'default' has a type variable type.
    def pop(self, k: Never, default: _T = ...) -> object: ...  # pyright: ignore[reportInvalidTypeVarUse]
    def update(self, m: typing_extensions.Self, /) -> None: ...
    def __delitem__(self, k: Never) -> None: ...
    def items(self) -> dict_items[str, object]: ...
    def keys(self) -> dict_keys[str, object]: ...
    def values(self) -> dict_values[str, object]: ...
    @overload
    def __or__(self, value: typing_extensions.Self, /) -> typing_extensions.Self: ...
    @overload
    def __or__(self, value: dict[str, Any], /) -> dict[str, object]: ...
    @overload
    def __ror__(self, value: typing_extensions.Self, /) -> typing_extensions.Self: ...
    @overload
    def __ror__(self, value: dict[str, Any], /) -> dict[str, object]: ...
    # supposedly incompatible definitions of __or__ and __ior__
    def __ior__(self, value: typing_extensions.Self, /) -> typing_extensions.Self: ...  # type: ignore[misc]

# Non-default variations to accommodate couroutines, and `AwaitableGenerator` having a 4th type parameter.
_S = TypeVar("_S")
_YieldT_co = TypeVar("_YieldT_co", covariant=True)
_SendT_nd_contra = TypeVar("_SendT_nd_contra", contravariant=True)
_ReturnT_nd_co = TypeVar("_ReturnT_nd_co", covariant=True)

# The parameters correspond to Generator, but the 4th is the original type.
class AwaitableGenerator(
    Awaitable[_ReturnT_nd_co],
    Generator[_YieldT_co, _SendT_nd_contra, _ReturnT_nd_co],
    Generic[_YieldT_co, _SendT_nd_contra, _ReturnT_nd_co, _S],
    metaclass=ABCMeta,
): ...

@final
class function:
    # Make sure this class definition stays roughly in line with `types.FunctionType`
    @property
    def __closure__(self) -> tuple[CellType, ...] | None: ...
    __code__: CodeType
    __defaults__: tuple[Any, ...] | None
    __dict__: dict[str, Any]
    @property
    def __globals__(self) -> dict[str, Any]: ...
    __name__: str
    __qualname__: str
    __annotations__: dict[str, Any]
    __kwdefaults__: dict[str, Any]
    if sys.version_info >= (3, 10):
        @property
        def __builtins__(self) -> dict[str, Any]: ...
    if sys.version_info >= (3, 12):
        __type_params__: tuple[TypeVar | ParamSpec | TypeVarTuple, ...]

    __module__: str
    # mypy uses `builtins.function.__get__` to represent methods, properties, and getset_descriptors so we type the return as Any.
    def __get__(self, instance: object, owner: type | None = None, /) -> Any: ...
