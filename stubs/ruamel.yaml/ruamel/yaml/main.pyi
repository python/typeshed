from _typeshed import Incomplete
from pathlib import Path
from types import TracebackType

from ruamel.yaml.compat import (
    StreamTextType as StreamTextType,
    StreamType as StreamType,
    VersionType as VersionType,
    nprintf as nprintf,
)
from ruamel.yaml.constructor import Constructor
from ruamel.yaml.error import UnsafeLoaderWarning as UnsafeLoaderWarning
from ruamel.yaml.events import *
from ruamel.yaml.nodes import *
from ruamel.yaml.representer import Representer
from ruamel.yaml.resolver import VersionedResolver as VersionedResolver
from ruamel.yaml.tokens import *

class YAML:
    typ: Incomplete
    pure: Incomplete
    plug_ins: Incomplete
    Resolver: Incomplete
    allow_unicode: bool
    Reader: Incomplete
    Representer: Incomplete
    Constructor: Incomplete
    Scanner: Incomplete
    Serializer: Incomplete
    default_flow_style: Incomplete
    comment_handling: Incomplete
    Emitter: Incomplete
    Parser: Incomplete
    Composer: Incomplete
    stream: Incomplete
    canonical: Incomplete
    old_indent: Incomplete
    width: Incomplete
    line_break: Incomplete
    map_indent: Incomplete
    sequence_indent: Incomplete
    sequence_dash_offset: int
    compact_seq_seq: Incomplete
    compact_seq_map: Incomplete
    sort_base_mapping_type_on_output: Incomplete
    top_level_colon_align: Incomplete
    prefix_colon: Incomplete
    preserve_quotes: Incomplete
    allow_duplicate_keys: bool
    encoding: str
    explicit_start: Incomplete
    explicit_end: Incomplete
    doc_infos: Incomplete
    default_style: Incomplete
    top_level_block_style_scalar_no_indent_error_1_1: bool
    scalar_after_indicator: Incomplete
    brace_single_entry_mapping_in_flow_sequence: bool
    def __init__(
        self,
        *,
        typ: list[str] | str | None = None,
        pure: bool = False,
        output: Incomplete | None = None,
        plug_ins: Incomplete | None = None,
    ) -> None: ...
    @property
    def reader(self): ...
    @property
    def scanner(self): ...
    @property
    def parser(self): ...
    @property
    def composer(self): ...
    @property
    def constructor(self): ...
    @property
    def resolver(self): ...
    @property
    def emitter(self): ...
    @property
    def serializer(self): ...
    @property
    def representer(self): ...
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
    def map(self, **kw): ...
    def seq(self, *args): ...
    def official_plug_ins(self): ...
    def register_class(self, cls): ...
    def __enter__(self): ...
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
    def indent(self): ...
    @indent.setter
    def indent(self, val) -> None: ...
    @property
    def block_seq_indent(self): ...
    @block_seq_indent.setter
    def block_seq_indent(self, val) -> None: ...
    def compact(self, seq_seq: Incomplete | None = None, seq_map: Incomplete | None = None) -> None: ...

class YAMLContextManager:
    def __init__(self, yaml, transform: Incomplete | None = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data) -> None: ...
    def dump(self, data) -> None: ...

def yaml_object(yml): ...
def warn_deprecation(fun, method, arg: str = "") -> None: ...
def error_deprecation(fun, method, arg: str = "", comment: str = "instead of") -> None: ...
def scan(stream: StreamTextType, Loader=...): ...
def parse(stream: StreamTextType, Loader=...): ...
def compose(stream: StreamTextType, Loader=...): ...
def compose_all(stream: StreamTextType, Loader=...): ...
def load(
    stream, Loader: Incomplete | None = None, version: Incomplete | None = None, preserve_quotes: Incomplete | None = None
) -> None: ...
def load_all(
    stream, Loader: Incomplete | None = None, version: Incomplete | None = None, preserve_quotes: Incomplete | None = None
) -> None: ...
def safe_load(stream: StreamTextType, version: VersionType | None = None): ...
def safe_load_all(stream: StreamTextType, version: VersionType | None = None): ...
def round_trip_load(stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None): ...
def round_trip_load_all(stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None): ...
def emit(
    events,
    stream: StreamType | None = None,
    Dumper=...,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Incomplete | None = None,
): ...

enc: Incomplete

def serialize_all(
    nodes,
    stream: StreamType | None = None,
    Dumper=...,
    canonical: Incomplete | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Incomplete | None = None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Incomplete | None = None,
): ...
def serialize(node, stream: StreamType | None = None, Dumper=..., **kwds): ...
def dump_all(
    documents,
    stream: StreamType | None = None,
    Dumper=...,
    default_style: Incomplete | None = None,
    default_flow_style: Incomplete | None = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Incomplete | None = None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: Incomplete | None = None,
    tags: Incomplete | None = None,
    block_seq_indent: Incomplete | None = None,
    top_level_colon_align: Incomplete | None = None,
    prefix_colon: Incomplete | None = None,
): ...
def dump(
    data,
    stream: StreamType | None = None,
    Dumper=...,
    default_style: Incomplete | None = None,
    default_flow_style: Incomplete | None = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Incomplete | None = None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Incomplete | None = None,
    block_seq_indent: Incomplete | None = None,
): ...
def safe_dump(data, stream: StreamType | None = None, **kwds): ...
def round_trip_dump(
    data,
    stream: StreamType | None = None,
    Dumper=...,
    default_style: Incomplete | None = None,
    default_flow_style: Incomplete | None = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Incomplete | None = None,
    encoding=None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Incomplete | None = None,
    block_seq_indent: Incomplete | None = None,
    top_level_colon_align: Incomplete | None = None,
    prefix_colon: Incomplete | None = None,
): ...
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
