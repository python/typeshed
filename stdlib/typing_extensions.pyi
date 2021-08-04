import abc
import sys
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Any
from typing import AsyncContextManager as AsyncContextManager
from typing import AsyncGenerator as AsyncGenerator
from typing import AsyncIterable as AsyncIterable
from typing import AsyncIterator as AsyncIterator
from typing import Awaitable as Awaitable
from typing import Callable
from typing import ChainMap as ChainMap
from typing import ClassVar as ClassVar
from typing import ContextManager as ContextManager
from typing import Coroutine as Coroutine
from typing import Counter as Counter
from typing import DefaultDict as DefaultDict
from typing import Deque as Deque
from typing import Dict, ItemsView, KeysView, Mapping
from typing import NewType as NewType
from typing import NoReturn as NoReturn
from typing import Optional
from typing import Text as Text
from typing import Tuple
from typing import Type as Type
from typing import TypeVar, Union, ValuesView, _Alias
from typing import overload as overload

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])
_TC = TypeVar("_TC", bound=Type[object])

class _SpecialForm:
    def __getitem__(self, typeargs: Any) -> Any: ...

def runtime_checkable(cls: _TC) -> _TC: ...

# This alias for above is kept here for backwards compatibility.
runtime = runtime_checkable
Protocol: _SpecialForm = ...
Final: _SpecialForm = ...

def final(f: _F) -> _F: ...

Literal: _SpecialForm = ...

def IntVar(name: str) -> Any: ...  # returns a new TypeVar

# Internal mypy fallback type for all typed dicts (does not exist at runtime)
class _TypedDict(Mapping[str, object], metaclass=abc.ABCMeta):
    def copy(self: _T) -> _T: ...
    # Using NoReturn so that only calls using mypy plugin hook that specialize the signature
    # can go through.
    def setdefault(self, k: NoReturn, default: object) -> object: ...
    # Mypy plugin hook for 'pop' expects that 'default' has a type variable type.
    def pop(self, k: NoReturn, default: _T = ...) -> object: ...  # type: ignore
    def update(self: _T, __m: _T) -> None: ...
    def items(self) -> ItemsView[str, object]: ...
    def keys(self) -> KeysView[str]: ...
    def values(self) -> ValuesView[object]: ...
    def __delitem__(self, k: NoReturn) -> None: ...

# TypedDict is a (non-subscriptable) special form.
TypedDict: object = ...

OrderedDict = _Alias()

def get_type_hints(
    obj: Callable[..., Any],
    globalns: Optional[Dict[str, Any]] = ...,
    localns: Optional[Dict[str, Any]] = ...,
    include_extras: bool = ...,
) -> Dict[str, Any]: ...

if sys.version_info >= (3, 7):
    def get_args(tp: Any) -> Tuple[Any, ...]: ...
    def get_origin(tp: Any) -> Optional[Any]: ...

Annotated: _SpecialForm = ...
_AnnotatedAlias: Any = ...  # undocumented

@runtime_checkable
class SupportsIndex(Protocol, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __index__(self) -> int: ...

# PEP 612 support for Python < 3.9
if sys.version_info >= (3, 10):
    from typing import Concatenate as Concatenate, ParamSpec as ParamSpec, TypeAlias as TypeAlias, TypeGuard as TypeGuard
else:
    class ParamSpecArgs:
        __origin__: ParamSpec
        def __init__(self, origin: ParamSpec) -> None: ...
    class ParamSpecKwargs:
        __origin__: ParamSpec
        def __init__(self, origin: ParamSpec) -> None: ...
    class ParamSpec:
        __name__: str
        __bound__: Optional[Type[Any]]
        __covariant__: bool
        __contravariant__: bool
        def __init__(
            self, name: str, *, bound: Union[None, Type[Any], str] = ..., contravariant: bool = ..., covariant: bool = ...
        ) -> None: ...
        @property
        def args(self) -> ParamSpecArgs: ...
        @property
        def kwargs(self) -> ParamSpecKwargs: ...
    Concatenate: _SpecialForm = ...
    TypeAlias: _SpecialForm = ...
    TypeGuard: _SpecialForm = ...
