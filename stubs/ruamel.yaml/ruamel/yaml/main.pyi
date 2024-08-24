from _typeshed import Incomplete, SupportsWrite
from pathlib import Path
from types import ModuleType, TracebackType
from typing import Callable, Final, Literal, NoReturn, Protocol, overload
from typing_extensions import Never, Self, TypeAlias, deprecated

from .comments import CommentedMap, CommentedSeq
from .compat import StreamTextType as StreamTextType, StreamType as StreamType, VersionType as VersionType, nprintf as nprintf
from .composer import Composer
from .constructor import BaseConstructor, Constructor, RoundTripConstructor
from .docinfo import DocInfo
from .dumper import _Inf
from .emitter import Emitter, RoundTripEmitter
from .error import UnsafeLoaderWarning as UnsafeLoaderWarning
from .events import *
from .nodes import *
from .parser import Parser, RoundTripParser
from .reader import Reader
from .representer import BaseRepresenter, Representer, RoundTripRepresenter
from .resolver import BaseResolver, VersionedResolver as VersionedResolver
from .scanner import RoundTripScanner, Scanner
from .serializer import Serializer
from .tokens import *

_YAMLType: TypeAlias = str | Literal["rt", "safe", "unsafe", "full", "base"]

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
    comment_handling: None
    Emitter: type[Emitter]  # TODO: CEmitter
    Parser: type[Parser]  # TODO: CParser
    Composer: type[Composer]
    stream: None
    canonical: bool | None
    old_indent: int | None
    width: int | _Inf | None
    line_break: str | None
    map_indent: int | None
    sequence_indent: int | None
    sequence_dash_offset: int
    compact_seq_seq: bool | None
    compact_seq_map: bool | None
    sort_base_mapping_type_on_output: bool | None
    top_level_colon_align: bool | None
    prefix_colon: str | None
    preserve_quotes: bool | None
    allow_duplicate_keys: bool
    encoding: str
    explicit_start: bool | None
    explicit_end: bool | None
    doc_infos: list[DocInfo]
    default_style: str | None
    top_level_block_style_scalar_no_indent_error_1_1: bool
    scalar_after_indicator: bool | None
    brace_single_entry_mapping_in_flow_sequence: bool
    @overload
    def __new__(
        cls,
        *,
        typ: Literal["rt"] | list[Literal["rt"]] | None = None,
        pure: bool = False,
        output: Path | SupportsWrite[str] | None = None,
        plug_ins: list[str] | None = None,
    ) -> _RoundTripYAML: ...
    @overload
    def __new__(
        cls,
        *,
        typ: Literal["full"] | list[Literal["full"]],
        pure: bool = False,
        output: Path | SupportsWrite[str] | None = None,
        plug_ins: list[str] | None = None,
    ) -> _FullYAML: ...
    @overload
    def __new__(
        cls,
        *,
        typ: _YAMLType | list[_YAMLType],
        pure: bool = False,
        output: Path | SupportsWrite[str] | None = None,
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
        output: Path | SupportsWrite[str] | None = None,
        plug_ins: list[str] | None = None,
    ) -> None: ...
    @overload
    @deprecated("For **dumping only** use YAML(typ='full')", category=PendingDeprecationWarning)
    def __init__(
        self,
        *,
        typ: Literal["unsafe"] | list[Literal["unsafe"]],
        pure: bool = False,
        output: Path | SupportsWrite[str] | None = None,
        plug_ins: list[str] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        typ: _YAMLType | list[_YAMLType],
        pure: bool = False,
        output: Path | SupportsWrite[str] | None = None,
        plug_ins: list[str] | None = None,
    ) -> None: ...
    @property
    def reader(self) -> Reader: ...
    @property
    def scanner(self) -> Scanner: ...
    @property
    def parser(self) -> Parser | None: ...  # TODO: CParser
    @property
    def composer(self) -> Composer: ...
    @property
    def constructor(self) -> Constructor: ...
    @property
    def resolver(self) -> BaseResolver: ...
    @property
    def emitter(self) -> Emitter | None: ...  # TODO: CEmitter
    @property
    def serializer(self) -> Serializer: ...
    @property
    def representer(self) -> BaseRepresenter: ...
    def scan(self, stream: StreamTextType): ...
    def parse(self, stream: StreamTextType): ...
    def compose(self, stream: Path | StreamTextType): ...
    def compose_all(self, stream: Path | StreamTextType): ...
    def load(self, stream: Path | StreamTextType): ...
    def load_all(self, stream: Path | StreamTextType): ...
    def get_constructor_parser(self, stream: StreamTextType): ...
    def emit(self, events, stream) -> None: ...
    def serialize(self, node, stream: StreamType | None): ...
    def serialize_all(self, nodes, stream: StreamType | None): ...
    def dump(self, data: Path | StreamType, stream: Incomplete | None = None, *, transform: Incomplete | None = None): ...
    def dump_all(self, documents, stream: Path | StreamType, *, transform: Incomplete | None = None): ...
    def Xdump_all(self, documents, stream, *, transform: Incomplete | None = None): ...
    def get_serializer_representer_emitter(self, stream: StreamType, tlca): ...
    def map(self, **kw) -> dict: ...
    def seq(self, *args) -> list: ...
    def official_plug_ins(self) -> list[str]: ...
    def register_class(self, cls: _RegistrableClass) -> _RegistrableClass: ...
    def __enter__(self) -> _YAMLContext: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    @property
    def version(self) -> tuple[int, int] | None: ...
    @version.setter
    def version(self, val: VersionType) -> None: ...
    @property
    def tags(self): ...
    @tags.setter
    def tags(self, val) -> None: ...
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
    def map(self, **kw) -> CommentedMap: ...
    def seq(self, *args) -> CommentedSeq: ...
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
    def scan(self, stream: Incomplete) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def parse(self, stream: Incomplete) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def compose(self, stream: Path | Incomplete) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def compose_all(self, stream: Path | Incomplete) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def load(self, stream: Path | Incomplete) -> NoReturn: ...
    @deprecated("You can only use YAML(typ='full') for dumping")
    def load_all(self, stream: Path | Incomplete) -> NoReturn: ...
    def get_constructor_parser(self, stream: StreamTextType) -> NoReturn: ...
    def __enter__(self) -> _FullYAMLContext: ...

class _YAMLContext(YAML):
    def dump_all(self, documents, stream: Path | Incomplete, *, transform: Incomplete | None = ...) -> NoReturn: ...

class _RoundTripYAMLContext(_YAMLContext, _RoundTripYAML): ...
class _FullYAMLContext(_YAMLContext, _FullYAML): ...

class YAMLContextManager:
    def __init__(self, yaml, transform: Incomplete | None = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data) -> None: ...
    def dump(self, data) -> None: ...

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
def scan(stream: StreamTextType, Loader=...) -> NoReturn: ...
@deprecated("Use YAML().parse() instead")
def parse(stream: StreamTextType, Loader=...) -> NoReturn: ...
@deprecated("Use YAML().compose() instead")
def compose(stream: StreamTextType, Loader=...) -> NoReturn: ...
@deprecated("Use YAML().compose_all() instead")
def compose_all(stream: StreamTextType, Loader=...) -> NoReturn: ...
@deprecated("Use YAML().load() instead")
def load(stream, Loader=None, version=None, preserve_quotes=None) -> NoReturn: ...
@deprecated("Use YAML().load_all() instead")
def load_all(stream, Loader=None, version=None, preserve_quotes=None) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).load() instead")
def safe_load(stream: StreamTextType, version: VersionType | None = None) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).load_all() instead")
def safe_load_all(stream: StreamTextType, version: VersionType | None = None) -> NoReturn: ...
@deprecated("Use YAML().load() instead")
def round_trip_load(
    stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
) -> NoReturn: ...
@deprecated("Use YAML().load_all() instead")
def round_trip_load_all(
    stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).emit() instead")
def emit(
    events,
    stream: StreamType | None = None,
    Dumper=...,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break=None,
) -> NoReturn: ...

enc: None

@deprecated("Use YAML(typ='safe', pure=True).serialize_all() instead")
def serialize_all(
    nodes,
    stream: StreamType | None = None,
    Dumper=...,
    canonical=None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break=None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags=None,
) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).serialize() instead")
def serialize(node, stream: StreamType | None = None, Dumper=..., **kwds) -> NoReturn: ...
@deprecated("Use YAML(typ='unsafe', pure=True).dump_all() instead")
def dump_all(
    documents,
    stream: StreamType | None = None,
    Dumper=...,
    default_style=None,
    default_flow_style=None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break=None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version=None,
    tags=None,
    block_seq_indent=None,
    top_level_colon_align=None,
    prefix_colon=None,
) -> NoReturn: ...
@deprecated("Use YAML(typ='unsafe', pure=True).dump() instead")
def dump(
    data,
    stream: StreamType | None = None,
    Dumper=...,
    default_style=None,
    default_flow_style=None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break=None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags=None,
    block_seq_indent=None,
) -> NoReturn: ...
@deprecated("Use YAML(typ='safe', pure=True).dump() instead")
def safe_dump(data, stream: StreamType | None = None, **kwds) -> NoReturn: ...
@deprecated("Use YAML().dump() instead")
def round_trip_dump(
    data,
    stream: StreamType | None = None,
    Dumper=...,
    default_style=None,
    default_flow_style=None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break=None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags=None,
    block_seq_indent=None,
    top_level_colon_align=None,
    prefix_colon=None,
) -> NoReturn: ...
def add_implicit_resolver(
    tag, regexp, first: Incomplete | None = None, Loader: Incomplete | None = None, Dumper: Incomplete | None = None, resolver=...
) -> None: ...
def add_path_resolver(
    tag, path, kind: Incomplete | None = None, Loader: Incomplete | None = None, Dumper: Incomplete | None = None, resolver=...
) -> None: ...
def add_constructor(tag, object_constructor, Loader: Incomplete | None = None, constructor=...) -> None: ...
def add_multi_constructor(tag_prefix, multi_constructor, Loader: Incomplete | None = None, constructor=...) -> None: ...
def add_representer(data_type, object_representer, Dumper: Incomplete | None = None, representer=...) -> None: ...
def add_multi_representer(data_type, multi_representer, Dumper: Incomplete | None = None, representer=...) -> None: ...

class YAMLObjectMetaclass(type):
    def __init__(cls, name, bases, kwds) -> None: ...

class YAMLObject(Incomplete):
    yaml_constructor = Constructor
    yaml_representer = Representer
    yaml_tag: Incomplete
    yaml_flow_style: Incomplete
    @classmethod
    def from_yaml(cls, constructor, node): ...
    @classmethod
    def to_yaml(cls, representer, data): ...
