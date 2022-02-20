import collections  # Needed by aliases like DefaultDict, see mypy issue 2986
from _typeshed import Self
from abc import ABCMeta, abstractmethod
from types import CodeType, FrameType, TracebackType

# Definitions of special type checking related constructs.  Their definitions
# are not used, so their value does not matter.

Any = object()

class TypeVar:
    __name__: str
    __bound__: type[Any] | None
    __constraints__: tuple[type[Any], ...]
    __covariant__: bool
    __contravariant__: bool
    def __init__(
        self, name: str, *constraints: type[Any], bound: type[Any] | None = ..., covariant: bool = ..., contravariant: bool = ...
    ) -> None: ...

_promote = object()

# N.B. Keep this definition in sync with typing_extensions._SpecialForm
class _SpecialForm(object):
    def __getitem__(self, typeargs: Any) -> object: ...

# Unlike the vast majority module-level objects in stub files,
# these `_SpecialForm` objects in typing need the default value `= ...`,
# due to the fact that they are used elswhere in the same file.
# Otherwise, flake8 erroneously flags them as undefined.
# `_SpecialForm` objects in typing.py that are not used elswhere in the same file
# do not need the default value assignment.
Generic: _SpecialForm = ...
Protocol: _SpecialForm = ...
Callable: _SpecialForm = ...
Union: _SpecialForm = ...

Optional: _SpecialForm
Tuple: _SpecialForm
Type: _SpecialForm
ClassVar: _SpecialForm
Final: _SpecialForm
_F = TypeVar("_F", bound=Callable[..., Any])

def final(f: _F) -> _F: ...
def overload(f: _F) -> _F: ...

Literal: _SpecialForm
# TypedDict is a (non-subscriptable) special form.
TypedDict: object

class GenericMeta(type): ...

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
NoReturn = Union[None]

# These type variables are used by the container types.
_T = TypeVar("_T")
_KT = TypeVar("_KT")  # Key type.
_VT = TypeVar("_VT")  # Value type.
_T_co = TypeVar("_T_co", covariant=True)  # Any type covariant containers.
_V_co = TypeVar("_V_co", covariant=True)  # Any type covariant containers.
_KT_co = TypeVar("_KT_co", covariant=True)  # Key type covariant containers.
_VT_co = TypeVar("_VT_co", covariant=True)  # Value type covariant containers.
_T_contra = TypeVar("_T_contra", contravariant=True)  # Ditto contravariant.
_TC = TypeVar("_TC", bound=type[object])

def no_type_check(f: _F) -> _F: ...
def no_type_check_decorator(decorator: _F) -> _F: ...

# Type aliases and type constructors

class _Alias:
    # Class for defining generic aliases for library types.
    def __getitem__(self, typeargs: Any) -> Any: ...

List = _Alias()
Dict = _Alias()
DefaultDict = _Alias()
Set = _Alias()
FrozenSet = _Alias()
Counter = _Alias()
Deque = _Alias()

# Predefined type variables.
AnyStr = TypeVar("AnyStr", str, unicode)  # noqa: Y001

# Abstract base classes.

def runtime_checkable(cls: _TC) -> _TC: ...
@runtime_checkable
class SupportsInt(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __int__(self) -> int: ...

@runtime_checkable
class SupportsFloat(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __float__(self) -> float: ...

@runtime_checkable
class SupportsComplex(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __complex__(self) -> complex: ...

@runtime_checkable
class SupportsAbs(Protocol[_T_co]):
    @abstractmethod
    def __abs__(self) -> _T_co: ...

@runtime_checkable
class Reversible(Protocol[_T_co]):
    @abstractmethod
    def __reversed__(self) -> Iterator[_T_co]: ...

@runtime_checkable
class Sized(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __len__(self) -> int: ...

@runtime_checkable
class Hashable(Protocol, metaclass=ABCMeta):
    # TODO: This is special, in that a subclass of a hashable class may not be hashable
    #   (for example, list vs. object). It's not obvious how to represent this. This class
    #   is currently mostly useless for static checking.
    @abstractmethod
    def __hash__(self) -> int: ...

@runtime_checkable
class Iterable(Protocol[_T_co]):
    @abstractmethod
    def __iter__(self) -> Iterator[_T_co]: ...

@runtime_checkable
class Iterator(Iterable[_T_co], Protocol[_T_co]):
    @abstractmethod
    def next(self) -> _T_co: ...
    def __iter__(self) -> Iterator[_T_co]: ...

class Generator(Iterator[_T_co], Generic[_T_co, _T_contra, _V_co]):
    @abstractmethod
    def next(self) -> _T_co: ...
    @abstractmethod
    def send(self, __value: _T_contra) -> _T_co: ...
    @overload
    @abstractmethod
    def throw(
        self, __typ: type[BaseException], __val: BaseException | object = ..., __tb: TracebackType | None = ...
    ) -> _T_co: ...
    @overload
    @abstractmethod
    def throw(self, __typ: BaseException, __val: None = ..., __tb: TracebackType | None = ...) -> _T_co: ...
    @abstractmethod
    def close(self) -> None: ...
    @property
    def gi_code(self) -> CodeType: ...
    @property
    def gi_frame(self) -> FrameType: ...
    @property
    def gi_running(self) -> bool: ...

@runtime_checkable
class Container(Protocol[_T_co]):
    @abstractmethod
    def __contains__(self, x: object) -> bool: ...

class Sequence(Iterable[_T_co], Container[_T_co], Reversible[_T_co], Generic[_T_co]):
    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> _T_co: ...
    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[_T_co]: ...
    # Mixin methods
    def index(self, x: Any) -> int: ...
    def count(self, x: Any) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[_T_co]: ...
    def __reversed__(self) -> Iterator[_T_co]: ...
    # Implement Sized (but don't have it as a base class).
    @abstractmethod
    def __len__(self) -> int: ...

class MutableSequence(Sequence[_T], Generic[_T]):
    @abstractmethod
    def insert(self, index: int, object: _T) -> None: ...
    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> _T: ...
    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> MutableSequence[_T]: ...
    @overload
    @abstractmethod
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    @abstractmethod
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...
    @overload
    @abstractmethod
    def __delitem__(self, i: int) -> None: ...
    @overload
    @abstractmethod
    def __delitem__(self, i: slice) -> None: ...
    # Mixin methods
    def append(self, object: _T) -> None: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def reverse(self) -> None: ...
    def pop(self, index: int = ...) -> _T: ...
    def remove(self, object: _T) -> None: ...
    def __iadd__(self: Self, x: Iterable[_T]) -> Self: ...

class AbstractSet(Iterable[_T_co], Container[_T_co], Generic[_T_co]):
    @abstractmethod
    def __contains__(self, x: object) -> bool: ...
    # Mixin methods
    def __le__(self, s: AbstractSet[Any]) -> bool: ...
    def __lt__(self, s: AbstractSet[Any]) -> bool: ...
    def __gt__(self, s: AbstractSet[Any]) -> bool: ...
    def __ge__(self, s: AbstractSet[Any]) -> bool: ...
    def __and__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
    def __or__(self, s: AbstractSet[_T]) -> AbstractSet[_T_co | _T]: ...
    def __sub__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
    def __xor__(self, s: AbstractSet[_T]) -> AbstractSet[_T_co | _T]: ...
    # TODO: argument can be any container?
    def isdisjoint(self, s: AbstractSet[Any]) -> bool: ...
    # Implement Sized (but don't have it as a base class).
    @abstractmethod
    def __len__(self) -> int: ...

class MutableSet(AbstractSet[_T], Generic[_T]):
    @abstractmethod
    def add(self, x: _T) -> None: ...
    @abstractmethod
    def discard(self, x: _T) -> None: ...
    # Mixin methods
    def clear(self) -> None: ...
    def pop(self) -> _T: ...
    def remove(self, element: _T) -> None: ...
    def __ior__(self: Self, s: AbstractSet[_T]) -> Self: ...
    def __iand__(self: Self, s: AbstractSet[Any]) -> Self: ...
    def __ixor__(self: Self, s: AbstractSet[_T]) -> Self: ...
    def __isub__(self: Self, s: AbstractSet[Any]) -> Self: ...

class MappingView(object):
    def __len__(self) -> int: ...

class ItemsView(MappingView, AbstractSet[tuple[_KT_co, _VT_co]], Generic[_KT_co, _VT_co]):
    def __init__(self, mapping: Mapping[_KT_co, _VT_co]) -> None: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[tuple[_KT_co, _VT_co]]: ...

class KeysView(MappingView, AbstractSet[_KT_co], Generic[_KT_co]):
    def __init__(self, mapping: Mapping[_KT_co, _VT_co]) -> None: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT_co]: ...

class ValuesView(MappingView, Iterable[_VT_co], Generic[_VT_co]):
    def __init__(self, mapping: Mapping[_KT_co, _VT_co]) -> None: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_VT_co]: ...

@runtime_checkable
class ContextManager(Protocol[_T_co]):
    def __enter__(self) -> _T_co: ...
    def __exit__(
        self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None
    ) -> bool | None: ...

class Mapping(Iterable[_KT], Container[_KT], Generic[_KT, _VT_co]):
    # TODO: We wish the key type could also be covariant, but that doesn't work,
    # see discussion in https: //github.com/python/typing/pull/273.
    @abstractmethod
    def __getitem__(self, k: _KT) -> _VT_co: ...
    # Mixin methods
    @overload
    def get(self, k: _KT) -> _VT_co | None: ...
    @overload
    def get(self, k: _KT, default: _VT_co | _T) -> _VT_co | _T: ...
    def keys(self) -> list[_KT]: ...
    def values(self) -> list[_VT_co]: ...
    def items(self) -> list[tuple[_KT, _VT_co]]: ...
    def iterkeys(self) -> Iterator[_KT]: ...
    def itervalues(self) -> Iterator[_VT_co]: ...
    def iteritems(self) -> Iterator[tuple[_KT, _VT_co]]: ...
    def __contains__(self, o: object) -> bool: ...
    # Implement Sized (but don't have it as a base class).
    @abstractmethod
    def __len__(self) -> int: ...

class MutableMapping(Mapping[_KT, _VT], Generic[_KT, _VT]):
    @abstractmethod
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    @abstractmethod
    def __delitem__(self, v: _KT) -> None: ...
    def clear(self) -> None: ...
    @overload
    def pop(self, k: _KT) -> _VT: ...
    @overload
    def pop(self, k: _KT, default: _VT | _T = ...) -> _VT | _T: ...
    def popitem(self) -> tuple[_KT, _VT]: ...
    def setdefault(self, k: _KT, default: _VT = ...) -> _VT: ...
    @overload
    def update(self, __m: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def update(self, __m: Iterable[tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    @overload
    def update(self, **kwargs: _VT) -> None: ...

Text = unicode

TYPE_CHECKING: bool

class IO(Iterator[AnyStr], Generic[AnyStr]):
    # TODO detach
    # TODO use abstract properties
    @property
    def mode(self) -> str: ...
    @property
    def name(self) -> str: ...
    @abstractmethod
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    @abstractmethod
    def fileno(self) -> int: ...
    @abstractmethod
    def flush(self) -> None: ...
    @abstractmethod
    def isatty(self) -> bool: ...
    # TODO what if n is None?
    @abstractmethod
    def read(self, n: int = ...) -> AnyStr: ...
    @abstractmethod
    def readable(self) -> bool: ...
    @abstractmethod
    def readline(self, limit: int = ...) -> AnyStr: ...
    @abstractmethod
    def readlines(self, hint: int = ...) -> list[AnyStr]: ...
    @abstractmethod
    def seek(self, offset: int, whence: int = ...) -> int: ...
    @abstractmethod
    def seekable(self) -> bool: ...
    @abstractmethod
    def tell(self) -> int: ...
    @abstractmethod
    def truncate(self, size: int | None = ...) -> int: ...
    @abstractmethod
    def writable(self) -> bool: ...
    # TODO buffer objects
    @abstractmethod
    def write(self, s: AnyStr) -> int: ...
    @abstractmethod
    def writelines(self, lines: Iterable[AnyStr]) -> None: ...
    @abstractmethod
    def next(self) -> AnyStr: ...
    @abstractmethod
    def __iter__(self) -> Iterator[AnyStr]: ...
    @abstractmethod
    def __enter__(self) -> IO[AnyStr]: ...
    @abstractmethod
    def __exit__(
        self, t: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> bool | None: ...

class BinaryIO(IO[str]):
    # TODO readinto
    # TODO read1?
    # TODO peek?
    @abstractmethod
    def __enter__(self) -> BinaryIO: ...

class TextIO(IO[unicode]):
    # TODO use abstractproperty
    @property
    def buffer(self) -> BinaryIO: ...
    @property
    def encoding(self) -> str: ...
    @property
    def errors(self) -> str | None: ...
    @property
    def line_buffering(self) -> bool: ...
    @property
    def newlines(self) -> Any: ...  # None, str or tuple
    @abstractmethod
    def __enter__(self) -> TextIO: ...

class ByteString(Sequence[int], metaclass=ABCMeta): ...

class Match(Generic[AnyStr]):
    pos: int
    endpos: int
    lastindex: int | None
    string: AnyStr

    # The regular expression object whose match() or search() method produced
    # this match instance. This should not be Pattern[AnyStr] because the type
    # of the pattern is independent of the type of the matched string in
    # Python 2. Strictly speaking Match should be generic over AnyStr twice:
    # once for the type of the pattern and once for the type of the matched
    # string.
    re: Pattern[Any]
    # Can be None if there are no groups or if the last group was unnamed;
    # otherwise matches the type of the pattern.
    lastgroup: Any | None
    def expand(self, template: str | Text) -> Any: ...
    @overload
    def group(self, group1: int = ...) -> AnyStr: ...
    @overload
    def group(self, group1: str) -> AnyStr: ...
    @overload
    def group(self, group1: int, group2: int, *groups: int) -> tuple[AnyStr, ...]: ...
    @overload
    def group(self, group1: str, group2: str, *groups: str) -> tuple[AnyStr, ...]: ...
    def groups(self, default: AnyStr = ...) -> tuple[AnyStr, ...]: ...
    def groupdict(self, default: AnyStr = ...) -> Dict[str, AnyStr]: ...
    def start(self, __group: int | str = ...) -> int: ...
    def end(self, __group: int | str = ...) -> int: ...
    def span(self, __group: int | str = ...) -> tuple[int, int]: ...
    @property
    def regs(self) -> tuple[tuple[int, int], ...]: ...  # undocumented

# We need a second TypeVar with the same definition as AnyStr, because
# Pattern is generic over AnyStr (determining the type of its .pattern
# attribute), but at the same time its methods take either bytes or
# Text and return the same type, regardless of the type of the pattern.
_AnyStr2 = TypeVar("_AnyStr2", bytes, Text)

class Pattern(Generic[AnyStr]):
    flags: int
    groupindex: Dict[AnyStr, int]
    groups: int
    pattern: AnyStr
    def search(self, string: _AnyStr2, pos: int = ..., endpos: int = ...) -> Match[_AnyStr2] | None: ...
    def match(self, string: _AnyStr2, pos: int = ..., endpos: int = ...) -> Match[_AnyStr2] | None: ...
    def split(self, string: _AnyStr2, maxsplit: int = ...) -> List[_AnyStr2]: ...
    # Returns either a list of _AnyStr2 or a list of tuples, depending on
    # whether there are groups in the pattern.
    def findall(self, string: bytes | Text, pos: int = ..., endpos: int = ...) -> List[Any]: ...
    def finditer(self, string: _AnyStr2, pos: int = ..., endpos: int = ...) -> Iterator[Match[_AnyStr2]]: ...
    @overload
    def sub(self, repl: _AnyStr2, string: _AnyStr2, count: int = ...) -> _AnyStr2: ...
    @overload
    def sub(self, repl: Callable[[Match[_AnyStr2]], _AnyStr2], string: _AnyStr2, count: int = ...) -> _AnyStr2: ...
    @overload
    def subn(self, repl: _AnyStr2, string: _AnyStr2, count: int = ...) -> tuple[_AnyStr2, int]: ...
    @overload
    def subn(self, repl: Callable[[Match[_AnyStr2]], _AnyStr2], string: _AnyStr2, count: int = ...) -> tuple[_AnyStr2, int]: ...

# Functions

def get_type_hints(
    obj: Callable[..., Any], globalns: Dict[Text, Any] | None = ..., localns: Dict[Text, Any] | None = ...
) -> None: ...
@overload
def cast(tp: type[_T], obj: Any) -> _T: ...
@overload
def cast(tp: str, obj: Any) -> Any: ...
@overload
def cast(tp: object, obj: Any) -> Any: ...

# Type constructors

# NamedTuple is special-cased in the type checker
class NamedTuple(tuple[Any, ...]):
    _fields: tuple[str, ...]
    def __init__(self, typename: Text, fields: Iterable[tuple[Text, Any]] = ..., **kwargs: Any) -> None: ...
    @classmethod
    def _make(cls: type[Self], iterable: Iterable[Any]) -> Self: ...
    def _asdict(self) -> Dict[str, Any]: ...
    def _replace(self: Self, **kwargs: Any) -> Self: ...

# Internal mypy fallback type for all typed dicts (does not exist at runtime)
class _TypedDict(Mapping[str, object], metaclass=ABCMeta):
    def copy(self: Self) -> Self: ...
    # Using NoReturn so that only calls using mypy plugin hook that specialize the signature
    # can go through.
    def setdefault(self, k: NoReturn, default: object) -> object: ...
    # Mypy plugin hook for 'pop' expects that 'default' has a type variable type.
    def pop(self, k: NoReturn, default: _T = ...) -> object: ...
    def update(self: _T, __m: _T) -> None: ...
    def has_key(self, k: str) -> bool: ...
    def viewitems(self) -> ItemsView[str, object]: ...
    def viewkeys(self) -> KeysView[str]: ...
    def viewvalues(self) -> ValuesView[object]: ...
    def __delitem__(self, k: NoReturn) -> None: ...

def NewType(name: str, tp: type[_T]) -> type[_T]: ...

# This itself is only available during type checking
def type_check_only(func_or_cls: _F) -> _F: ...
