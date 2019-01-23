# Stubs for typing (Python 2.7)

from abc import abstractmethod, ABCMeta
from types import CodeType, FrameType, TracebackType
import collections  # Needed by aliases like DefaultDict, see mypy issue 2986

# Definitions of special type checking related constructs.  Their definitions
# are not used, so their value does not matter.

overload = object()
Any = object()
TypeVar = object()
_promote = object()
no_type_check = object()

class _SpecialForm(object):
    def __getitem__(self, typeargs: Any) -> object: ...

Tuple: _SpecialForm = ...
Generic: _SpecialForm = ...
Protocol: _SpecialForm = ...
Callable: _SpecialForm = ...
Type: _SpecialForm = ...
ClassVar: _SpecialForm = ...

class GenericMeta(type): ...

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
NoReturn = Union[None]

# Type aliases and type constructors

class TypeAlias:
    # Class for defining generic aliases for library types.
    def __init__(self, target_type: type) -> None: ...
    def __getitem__(self, typeargs: Any) -> Any: ...

Union = TypeAlias(object)
Optional = TypeAlias(object)
List = TypeAlias(object)
Dict = TypeAlias(object)
DefaultDict = TypeAlias(object)
Set = TypeAlias(object)
FrozenSet = TypeAlias(object)
Counter = TypeAlias(object)
Deque = TypeAlias(object)

# Predefined type variables.
AnyStr = TypeVar('AnyStr', str, unicode)

# Abstract base classes.

# These type variables are used by the container types.
_T = TypeVar('_T')
_S = TypeVar('_S')
_KT = TypeVar('_KT')  # Key type.
_VT = TypeVar('_VT')  # Value type.
_T_co = TypeVar('_T_co', covariant=True)  # Any type covariant containers.
_V_co = TypeVar('_V_co', covariant=True)  # Any type covariant containers.
_KT_co = TypeVar('_KT_co', covariant=True)  # Key type covariant containers.
_VT_co = TypeVar('_VT_co', covariant=True)  # Value type covariant containers.
_T_contra = TypeVar('_T_contra', contravariant=True)  # Ditto contravariant.
_TC = TypeVar('_TC', bound=Type[object])

def runtime(cls: _TC) -> _TC: ...

@runtime
class SupportsInt(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __int__(self) -> int: ...

@runtime
class SupportsFloat(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __float__(self) -> float: ...

@runtime
class SupportsComplex(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __complex__(self) -> complex: ...

@runtime
class SupportsAbs(Protocol[_T_co]):
    @abstractmethod
    def __abs__(self) -> _T_co: ...

@runtime
class SupportsRound(Protocol[_T_co]):
    @abstractmethod
    def __round__(self, ndigits: int = ...) -> _T_co: ...

@runtime
class Reversible(Protocol[_T_co]):
    @abstractmethod
    def __reversed__(self) -> Iterator[_T_co]: ...

@runtime
class Sized(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __len__(self) -> int: ...

@runtime
class Hashable(Protocol, metaclass=ABCMeta):
    # TODO: This is special, in that a subclass of a hashable class may not be hashable
    #   (for example, list vs. object). It's not obvious how to represent this. This class
    #   is currently mostly useless for static checking.
    @abstractmethod
    def __hash__(self) -> int: ...

@runtime
class Iterable(Protocol[_T_co]):
    @abstractmethod
    def __iter__(self) -> Iterator[_T_co]: ...

@runtime
class Iterator(Iterable[_T_co], Protocol[_T_co]):
    @abstractmethod
    def next(self) -> _T_co: ...
    def __iter__(self) -> Iterator[_T_co]: ...

class Generator(Iterator[_T_co], Generic[_T_co, _T_contra, _V_co]):
    @abstractmethod
    def next(self) -> _T_co: ...

    @abstractmethod
    def send(self, value: _T_contra) -> _T_co: ...

    @abstractmethod
    def throw(self, typ: Type[BaseException], val: Optional[BaseException] = ...,
              tb: TracebackType = ...) -> _T_co: ...
    @abstractmethod
    def close(self) -> None: ...
    @property
    def gi_code(self) -> CodeType: ...
    @property
    def gi_frame(self) -> FrameType: ...
    @property
    def gi_running(self) -> bool: ...

@runtime
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
    def __iadd__(self, x: Iterable[_T]) -> MutableSequence[_T]: ...

class AbstractSet(Iterable[_T_co], Container[_T_co], Generic[_T_co]):
    @abstractmethod
    def __contains__(self, x: object) -> bool: ...
    # Mixin methods
    def __le__(self, s: AbstractSet[Any]) -> bool: ...
    def __lt__(self, s: AbstractSet[Any]) -> bool: ...
    def __gt__(self, s: AbstractSet[Any]) -> bool: ...
    def __ge__(self, s: AbstractSet[Any]) -> bool: ...
    def __and__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
    def __or__(self, s: AbstractSet[_T]) -> AbstractSet[Union[_T_co, _T]]: ...
    def __sub__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
    def __xor__(self, s: AbstractSet[_T]) -> AbstractSet[Union[_T_co, _T]]: ...
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
    def __ior__(self, s: AbstractSet[_S]) -> MutableSet[Union[_T, _S]]: ...
    def __iand__(self, s: AbstractSet[Any]) -> MutableSet[_T]: ...
    def __ixor__(self, s: AbstractSet[_S]) -> MutableSet[Union[_T, _S]]: ...
    def __isub__(self, s: AbstractSet[Any]) -> MutableSet[_T]: ...

class MappingView(object):
    def __len__(self) -> int: ...

class ItemsView(MappingView, AbstractSet[Tuple[_KT_co, _VT_co]], Generic[_KT_co, _VT_co]):
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[Tuple[_KT_co, _VT_co]]: ...

class KeysView(MappingView, AbstractSet[_KT_co], Generic[_KT_co]):
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT_co]: ...

class ValuesView(MappingView, Iterable[_VT_co], Generic[_VT_co]):
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_VT_co]: ...

@runtime
class ContextManager(Protocol[_T_co]):
    def __enter__(self) -> _T_co: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]: ...

class Mapping(Iterable[_KT], Container[_KT], Generic[_KT, _VT_co]):
    # TODO: We wish the key type could also be covariant, but that doesn't work,
    # see discussion in https: //github.com/python/typing/pull/273.
    @abstractmethod
    def __getitem__(self, k: _KT) -> _VT_co:
        ...
    # Mixin methods
    @overload
    def get(self, k: _KT) -> Optional[_VT_co]: ...
    @overload
    def get(self, k: _KT, default: Union[_VT_co, _T]) -> Union[_VT_co, _T]: ...
    def keys(self) -> list[_KT]: ...
    def values(self) -> list[_VT_co]: ...
    def items(self) -> list[Tuple[_KT, _VT_co]]: ...
    def iterkeys(self) -> Iterator[_KT]: ...
    def itervalues(self) -> Iterator[_VT_co]: ...
    def iteritems(self) -> Iterator[Tuple[_KT, _VT_co]]: ...
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
    def pop(self, k: _KT, default: Union[_VT, _T] = ...) -> Union[_VT, _T]: ...
    def popitem(self) -> Tuple[_KT, _VT]: ...
    def setdefault(self, k: _KT, default: _VT = ...) -> _VT: ...
    @overload
    def update(self, __m: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def update(self, __m: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    @overload
    def update(self, **kwargs: _VT) -> None: ...

Text = unicode

TYPE_CHECKING = True

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
    def truncate(self, size: Optional[int] = ...) -> int: ...
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
    def __exit__(self, t: Optional[Type[BaseException]], value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> bool: ...

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
    def errors(self) -> Optional[str]: ...
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
    lastindex: Optional[int]
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
    lastgroup: Optional[Any]

    def expand(self, template: Union[str, Text]) -> Any: ...

    @overload
    def group(self, group1: int = ...) -> AnyStr: ...
    @overload
    def group(self, group1: str) -> AnyStr: ...
    @overload
    def group(self, group1: int, group2: int,
              *groups: int) -> Tuple[AnyStr, ...]: ...
    @overload
    def group(self, group1: str, group2: str,
              *groups: str) -> Tuple[AnyStr, ...]: ...

    def groups(self, default: AnyStr = ...) -> Tuple[AnyStr, ...]: ...
    def groupdict(self, default: AnyStr = ...) -> Dict[str, AnyStr]: ...
    def start(self, group: Union[int, str] = ...) -> int: ...
    def end(self, group: Union[int, str] = ...) -> int: ...
    def span(self, group: Union[int, str] = ...) -> Tuple[int, int]: ...

# We need a second TypeVar with the same definition as AnyStr, because
# Pattern is generic over AnyStr (determining the type of its .pattern
# attribute), but at the same time its methods take either bytes or
# Text and return the same type, regardless of the type of the pattern.
_AnyStr2 = TypeVar('_AnyStr2', bytes, Text)

class Pattern(Generic[AnyStr]):
    flags: int
    groupindex: Dict[AnyStr, int]
    groups: int
    pattern: AnyStr

    def search(self, string: _AnyStr2, pos: int = ...,
               endpos: int = ...) -> Optional[Match[_AnyStr2]]: ...
    def match(self, string: _AnyStr2, pos: int = ...,
              endpos: int = ...) -> Optional[Match[_AnyStr2]]: ...
    def split(self, string: _AnyStr2, maxsplit: int = ...) -> List[_AnyStr2]: ...
    # Returns either a list of _AnyStr2 or a list of tuples, depending on
    # whether there are groups in the pattern.
    def findall(self, string: Union[bytes, Text], pos: int = ...,
                endpos: int = ...) -> List[Any]: ...
    def finditer(self, string: _AnyStr2, pos: int = ...,
                 endpos: int = ...) -> Iterator[Match[_AnyStr2]]: ...

    @overload
    def sub(self, repl: _AnyStr2, string: _AnyStr2,
            count: int = ...) -> _AnyStr2: ...
    @overload
    def sub(self, repl: Callable[[Match[_AnyStr2]], _AnyStr2], string: _AnyStr2,
            count: int = ...) -> _AnyStr2: ...

    @overload
    def subn(self, repl: _AnyStr2, string: _AnyStr2,
             count: int = ...) -> Tuple[_AnyStr2, int]: ...
    @overload
    def subn(self, repl: Callable[[Match[_AnyStr2]], _AnyStr2], string: _AnyStr2,
             count: int = ...) -> Tuple[_AnyStr2, int]: ...

# Functions

def get_type_hints(obj: Callable, globalns: Optional[dict[Text, Any]] = ...,
                   localns: Optional[dict[Text, Any]] = ...) -> None: ...

@overload
def cast(tp: Type[_T], obj: Any) -> _T: ...
@overload
def cast(tp: str, obj: Any) -> Any: ...

# Type constructors

# NamedTuple is special-cased in the type checker
class NamedTuple(tuple):
    _fields = ...  # type: Tuple[str, ...]

    def __init__(self, typename: AnyStr,
                 fields: Iterable[Tuple[AnyStr, Any]] = ..., *,
                 verbose: bool = ..., rename: bool = ..., **kwargs: Any) -> None: ...

    @classmethod
    def _make(cls: Type[_T], iterable: Iterable[Any]) -> _T: ...

    def _asdict(self) -> dict: ...
    def _replace(self: _T, **kwargs: Any) -> _T: ...

def NewType(name: str, tp: Type[_T]) -> Type[_T]: ...
