from _typeshed import Unused
from collections.abc import Callable, Iterable, Iterator, Sequence
from pathlib import Path
from re import Pattern
from types import ModuleType, TracebackType
from typing import Any, ClassVar, Final, Literal, NoReturn, Protocol, TypeVar, overload
from typing_extensions import Never, Self, TypeAlias, deprecated

from _ruamel_yaml import CEmitter, CParser

from .comments import CommentedMap, CommentedSeq
from .compat import VersionType, _ReadStream, _WriteStream
from .composer import Composer
from .constructor import BaseConstructor, Constructor, RoundTripConstructor, _ConstructorFunction, _MultiConstructorFunction
from .docinfo import DocInfo
from .emitter import Emitter, RoundTripEmitter, _Inf, _LineBreak
from .events import Event
from .nodes import Node
from .parser import Parser, RoundTripParser
from .reader import Reader
from .representer import BaseRepresenter, Representer, RoundTripRepresenter, _RepresenterFunction
from .resolver import BaseResolver, _First, _TagStr
from .scanner import RoundTripScanner, Scanner
from .serializer import Serializer
from .tag import Tag, _TagHandleToPrefix
from .tokens import Token, _ScalarStyle, _VersionTuple

_T = TypeVar("_T")
_Constructor = TypeVar("_Constructor", bound=BaseConstructor)
_Representer = TypeVar("_Representer", bound=BaseRepresenter)

_YAMLType: TypeAlias = str | Literal["rt", "safe", "unsafe", "full", "base"]  # noqa: Y051

class YAML:
    typ: list[_YAMLType]
    pure: Final[bool]
    plug_ins: list[ModuleType]
    Resolver: type[BaseResolver]
    allow_unicode: bool
    Reader: type[Reader] | None
    Representer: type[BaseRepresenter]
    Constructor: type[BaseConstructor]
    Scanner: type[Scanner] | None
    Serializer: type[Serializer] | None
    default_flow_style: bool | None
    comment_handling: int | None
    Emitter: type[Emitter | CEmitter]
    Parser: type[Parser | CParser]
    Composer: type[Composer]
    stream: None
    canonical: bool | None
    old_indent: int | None
    width: int | _Inf | None
    line_break: _LineBreak | None
    map_indent: int | None
    sequence_indent: int | None
    sequence_dash_offset: int
    compact_seq_seq: bool | None
    compact_seq_map: bool | None
    sort_base_mapping_type_on_output: bool | None
    top_level_colon_align: int | Literal[True] | None
    prefix_colon: str | None
    preserve_quotes: bool | None
    allow_duplicate_keys: bool
    encoding: str
    explicit_start: bool | None
    explicit_end: bool | None
    doc_infos: list[DocInfo]
    default_style: _ScalarStyle | None
    top_level_block_style_scalar_no_indent_error_1_1: bool
    scalar_after_indicator: bool | None
    brace_single_entry_mapping_in_flow_sequence: bool
    boolean_representation: Sequence[str]
    @overload
    def __new__(
        cls,
        *,
        typ: Literal["rt"] | list[Literal["rt"]] | None = None,
        pure: bool = False,
        output: Path | _WriteStream | None = None,
        plug_ins: list[str] | None = None,
    ) -> _RoundTripYAML: ...
    @overload
    def __new__(
        cls,
        *,
        typ: Literal["full"] | list[Literal["full"]],
        pure: bool = False,
        output: Path | _WriteStream | None = None,
        plug_ins: list[str] | None = None,
    ) -> _FullYAML: ...
    @overload
    def __new__(
        cls,
        *,
        typ: _YAMLType | list[_YAMLType],
        pure: bool = False,
        output: Path | _WriteStream | None = None,
        plug_ins: list[str] | None = None,
    ) -> Self: ...
    # This redundant overload prevents type checkers from matching the deprecated "unsafe" overload
    # when users are typing `YAML(typ=)`.
    @overload
    def __init__(
        self,
        *,
        typ: Literal["rt"] | list[Literal["rt"]] | None = None,
        pure: bool = False,
        output: Path | _WriteStream | None = None,
        plug_ins: list[str] | None = None,
    ) -> None: ...
    @overload
    @deprecated("For **dumping only** use YAML(typ='full')", category=PendingDeprecationWarning)
    def __init__(
        self,
        *,
        typ: Literal["unsafe"] | list[Literal["unsafe"]],
        pure: bool = False,
        output: Path | _WriteStream | None = None,
        plug_ins: list[str] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        typ: _YAMLType | list[_YAMLType],
        pure: bool = False,
        output: Path | _WriteStream | None = None,
        plug_ins: list[str] | None = None,
    ) -> None: ...
    @property
    def reader(self) -> Reader: ...
    @property
    def scanner(self) -> Scanner: ...
    @property
    def parser(self) -> Parser | CParser | None: ...
    @property
    def composer(self) -> Composer: ...
    @property
    def constructor(self) -> Constructor: ...
    @property
    def resolver(self) -> BaseResolver: ...
    @property
    def emitter(self) -> Emitter | CEmitter | None: ...
    @property
    def serializer(self) -> Serializer: ...
    @property
    def representer(self) -> BaseRepresenter: ...
    def scan(self, stream: _ReadStream) -> Iterator[Token]: ...
    def parse(self, stream: _ReadStream) -> Iterator[Event]: ...
    def compose(self, stream: Path | _ReadStream) -> Node: ...
    def compose_all(self, stream: _ReadStream) -> Iterator[Node]: ...
    def load(self, stream: Path | _ReadStream) -> Any: ...
    def load_all(self, stream: Path | _ReadStream) -> Iterator[Any]: ...
    def get_constructor_parser(self, stream: _ReadStream) -> tuple[BaseConstructor, Parser | CParser]: ...
    def emit(self, events: Iterable[Event], stream: _WriteStream) -> None: ...
    def serialize(self, node: Node, stream: _WriteStream) -> None: ...
    def serialize_all(self, nodes: Iterable[Node], stream: _WriteStream) -> None: ...
    def dump(self, data: Any, stream: Path | _WriteStream, *, transform: Callable[[str], str] | None = None) -> None: ...
    def dump_all(
        self, documents: Iterable[Any], stream: Path | _WriteStream, *, transform: Callable[[str], str] | None = None
    ) -> None: ...
    def Xdump_all(
        self, documents: Iterable[Any], stream: Path | _WriteStream, *, transform: Callable[[str], str] | None = None
    ) -> None: ...
    def get_serializer_representer_emitter(
        self, stream: _WriteStream, tlca: int | None
    ) -> tuple[Serializer, BaseRepresenter, Emitter | CEmitter]: ...
    @overload
    def map(self) -> dict[Any, Any]: ...
    @overload
    def map(self, **kw: _T) -> dict[str, _T]: ...
    @overload
    def seq(self) -> list[Any]: ...
    @overload
    def seq(self, iterable: Iterable[_T], /) -> list[_T]: ...
    def official_plug_ins(self) -> list[str]: ...
    def register_class(self, cls: _RegistrableClass) -> _RegistrableClass: ...
    def __enter__(self) -> _YAMLContext: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    @property
    def version(self) -> _VersionTuple | None: ...
    @version.setter
    def version(self, val: VersionType) -> None: ...
    @property
    def tags(self) -> _TagHandleToPrefix | None: ...
    @tags.setter
    def tags(self, val: _TagHandleToPrefix | None) -> None: ...
    @property
    def indent(self) -> _IndentSetter: ...
    @indent.setter
    def indent(self, val: int | None) -> None: ...
    @property
    def block_seq_indent(self) -> int: ...
    @block_seq_indent.setter
    def block_seq_indent(self, val: int) -> None: ...
    def compact(self, seq_seq: bool | None = None, seq_map: bool | None = None) -> None: ...

class _IndentSetter(Protocol):
    def __call__(self, mapping: int | None = None, sequence: int | None = None, offset: int | None = None) -> None: ...

class _RoundTripYAML(YAML):
    typ: list[Literal["rt"]]
    Representer: type[RoundTripRepresenter]
    Constructor: type[RoundTripConstructor]
    Scanner: type[RoundTripScanner]
    Emitter: type[RoundTripEmitter]
    Parser: type[RoundTripParser]
    @overload
    def map(self) -> CommentedMap[Any, Any]: ...
    @overload
    def map(self, **kw: _T) -> CommentedMap[str, _T]: ...
    @overload
    def seq(self) -> CommentedSeq[Any]: ...
    @overload
    def seq(self, iterable: Iterable[_T], /) -> CommentedSeq[_T]: ...
    def __enter__(self) -> _RoundTripYAMLContext: ...

class _FullYAML(YAML):
    typ: list[Literal["full"]]
    Composer: None
    Constructor: Never
    @property
    def composer(self) -> NoReturn: ...
    @property
    def constructor(self) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def scan(self, stream) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def parse(self, stream) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def compose(self, stream) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def compose_all(self, stream) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def load(self, stream) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def load_all(self, stream) -> NoReturn: ...
    def get_constructor_parser(self, stream) -> NoReturn: ...
    def __enter__(self) -> _FullYAMLContext: ...

class _YAMLContext(YAML):
    def dump(self, data: Any, stream: Unused = None, *, transform: None = None) -> None: ...
    def dump_all(self, documents, stream=None, *, transform=None) -> NoReturn: ...

class _RoundTripYAMLContext(_YAMLContext, _RoundTripYAML): ...
class _FullYAMLContext(_YAMLContext, _FullYAML): ...

class YAMLContextManager:
    def __init__(self, yaml: YAML, transform: Callable[[str], str] | None = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data: Any) -> None: ...
    def dump(self, data: Any) -> None: ...

# This is because we can't mark protocol fields as not required
# See https://github.com/python/typing/issues/601
_RegistrableClass: TypeAlias = type[_RegistrableObject | object]

class _RegistrableObject(Protocol):
    yaml_tag: str
    @classmethod
    def to_yaml(cls, representer: BaseRepresenter, data: Self, /) -> Node: ...
    @classmethod
    def from_yaml(cls, constructor: BaseConstructor, node: Node, /) -> Self: ...

def yaml_object(yml: YAML) -> Callable[[_RegistrableClass], _RegistrableClass]: ...
def warn_deprecation(fun: str, method: str, arg: str = "") -> None: ...
def error_deprecation(fun: str, method: str, arg: str = "", comment: str = "instead of") -> NoReturn: ...
@deprecated("Use YAML().scan() instead")
def scan(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().parse() instead")
def parse(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().compose() instead")
def compose(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().compose_all() instead")
def compose_all(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().load() instead")
def load(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().load_all() instead")
def load_all(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).load() instead")
def safe_load(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).load_all() instead")
def safe_load_all(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().load() instead")
def round_trip_load(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().load_all() instead")
def round_trip_load_all(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).emit() instead")
def emit(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).serialize_all() instead")
def serialize_all(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).serialize() instead")
def serialize(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='unsafe', pure=True).dump_all() instead")
def dump_all(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='unsafe', pure=True).dump() instead")
def dump(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).dump() instead")
def safe_dump(*args, **kwargs) -> NoReturn: ...
@deprecated("Use YAML().dump() instead")
def round_trip_dump(*args, **kwargs) -> NoReturn: ...
def add_implicit_resolver(
    tag: _TagStr,
    regexp: Pattern[str],
    first: list[_First] | None = None,
    Loader: type[BaseResolver] | None = None,
    Dumper: type[BaseResolver] | None = None,
    resolver: type[BaseResolver] = ...,
) -> None: ...
def add_path_resolver(
    tag: _TagStr,
    path: Iterable[Any],
    kind: type | None = None,
    Loader: type[BaseResolver] | None = None,
    Dumper: type[BaseResolver] | None = None,
    resolver: type[BaseResolver] = ...,
) -> None: ...
@overload
def add_constructor(
    tag: Tag | str | None, object_constructor: _ConstructorFunction[_Constructor], *, constructor: type[_Constructor]
) -> None: ...
@overload
def add_constructor(
    tag: Tag | str | None, object_constructor: _ConstructorFunction[_Constructor], Loader: type[_Constructor]
) -> None: ...
@overload
def add_constructor(tag: Tag | str | None, object_constructor: _ConstructorFunction[Constructor]) -> None: ...
@overload
def add_multi_constructor(
    tag_prefix: str | None, multi_constructor: _MultiConstructorFunction[_Constructor], *, constructor: type[_Constructor]
) -> None: ...
@overload
def add_multi_constructor(
    tag_prefix: str | None, multi_constructor: _MultiConstructorFunction[_Constructor], Loader: type[_Constructor]
) -> None: ...
@overload
def add_multi_constructor(tag_prefix: str | None, multi_constructor: _MultiConstructorFunction[Constructor]) -> None: ...
@overload
def add_representer(
    data_type: type[_T] | None, object_representer: _RepresenterFunction[_Representer, _T], *, representer: type[_Representer]
) -> None: ...
@overload
def add_representer(
    data_type: type[_T] | None, object_representer: _RepresenterFunction[_Representer, _T], Dumper: type[_Representer]
) -> None: ...
@overload
def add_representer(data_type: type[_T] | None, object_representer: _RepresenterFunction[Representer, _T]) -> None: ...
@overload
def add_multi_representer(
    data_type: type[_T] | None, multi_representer: _RepresenterFunction[_Representer, _T], *, representer: type[_Representer]
) -> None: ...
@overload
def add_multi_representer(
    data_type: type[_T] | None, multi_representer: _RepresenterFunction[_Representer, _T], Dumper: type[_Representer]
) -> None: ...
@overload
def add_multi_representer(data_type: type[_T] | None, multi_representer: _RepresenterFunction[Representer, _T]) -> None: ...

class YAMLObjectMetaclass(type):
    def __init__(cls, name: str, bases: tuple[type, ...], kwds: dict[str, Any], /) -> None: ...

class YAMLObject(metaclass=YAMLObjectMetaclass):
    yaml_constructor: ClassVar[type[BaseConstructor]]
    yaml_representer: ClassVar[type[BaseRepresenter]]
    yaml_tag: Tag | str | None
    yaml_flow_style: bool | None
    @classmethod
    def from_yaml(cls, constructor: BaseConstructor, node: Node) -> Self: ...
    @classmethod
    def to_yaml(cls, representer: BaseRepresenter, data: Self) -> Node: ...
