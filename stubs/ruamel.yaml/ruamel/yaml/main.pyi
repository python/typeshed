from _typeshed import Incomplete
from pathlib import Path
from types import TracebackType
from typing import Any

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
        self, *, typ: list[str] | str | None = None, pure: Any = False, output: Any = None, plug_ins: Any = None
    ) -> None: ...
    @property
    def reader(self) -> Any: ...
    @property
    def scanner(self) -> Any: ...
    @property
    def parser(self) -> Any: ...
    @property
    def composer(self) -> Any: ...
    @property
    def constructor(self) -> Any: ...
    @property
    def resolver(self) -> Any: ...
    @property
    def emitter(self) -> Any: ...
    @property
    def serializer(self) -> Any: ...
    @property
    def representer(self) -> Any: ...
    def scan(self, stream: StreamTextType) -> Any: ...
    def parse(self, stream: StreamTextType) -> Any: ...
    def compose(self, stream: Path | StreamTextType) -> Any: ...
    def compose_all(self, stream: Path | StreamTextType) -> Any: ...
    def load(self, stream: Path | StreamTextType) -> Any: ...
    def load_all(self, stream: Path | StreamTextType) -> Any: ...
    def get_constructor_parser(self, stream: StreamTextType) -> Any: ...
    def emit(self, events: Any, stream: Any) -> None: ...
    def serialize(self, node: Any, stream: StreamType | None) -> Any: ...
    def serialize_all(self, nodes: Any, stream: StreamType | None) -> Any: ...
    def dump(self, data: Path | StreamType, stream: Any = None, *, transform: Any = None) -> Any: ...
    def dump_all(self, documents: Any, stream: Path | StreamType, *, transform: Any = None) -> Any: ...
    def Xdump_all(self, documents: Any, stream: Any, *, transform: Any = None) -> Any: ...
    def get_serializer_representer_emitter(self, stream: StreamType, tlca: Any) -> Any: ...
    def map(self, **kw: Any) -> Any: ...
    def seq(self, *args: Any) -> Any: ...
    def official_plug_ins(self) -> Any: ...
    def register_class(self, cls: Any) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    @property
    def version(self) -> tuple[int, int] | None: ...
    @version.setter
    def version(self, val: VersionType) -> None: ...
    @property
    def tags(self) -> Any: ...
    @tags.setter
    def tags(self, val: Any) -> None: ...
    @property
    def indent(self) -> Any: ...
    @indent.setter
    def indent(self, val: Any) -> None: ...
    @property
    def block_seq_indent(self) -> Any: ...
    @block_seq_indent.setter
    def block_seq_indent(self, val: Any) -> None: ...
    def compact(self, seq_seq: Any = None, seq_map: Any = None) -> None: ...

class YAMLContextManager:
    def __init__(self, yaml: Any, transform: Any = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data: Any) -> None: ...
    def dump(self, data: Any) -> None: ...

def yaml_object(yml: Any) -> Any: ...
def warn_deprecation(fun: Any, method: Any, arg: str = "") -> None: ...
def error_deprecation(fun: Any, method: Any, arg: str = "", comment: str = "instead of") -> None: ...
def scan(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def parse(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def compose(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def compose_all(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def load(stream: Any, Loader: Any = None, version: Any = None, preserve_quotes: Any = None) -> Any: ...
def load_all(stream: Any, Loader: Any = None, version: Any = None, preserve_quotes: Any = None) -> Any: ...
def safe_load(stream: StreamTextType, version: VersionType | None = None) -> Any: ...
def safe_load_all(stream: StreamTextType, version: VersionType | None = None) -> Any: ...
def round_trip_load(stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> Any: ...
def round_trip_load_all(
    stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
) -> Any: ...
def emit(
    events: Any,
    stream: StreamType | None = None,
    Dumper: Any = ...,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any = None,
) -> Any: ...

enc: Incomplete

def serialize_all(
    nodes: Any,
    stream: StreamType | None = None,
    Dumper: Any = ...,
    canonical: Any = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any = None,
    encoding: Any = None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Any = None,
) -> Any: ...
def serialize(node: Any, stream: StreamType | None = None, Dumper: Any = ..., **kwds: Any) -> Any: ...
def dump_all(
    documents: Any,
    stream: StreamType | None = None,
    Dumper: Any = ...,
    default_style: Any = None,
    default_flow_style: Any = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any = None,
    encoding: Any = None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: Any = None,
    tags: Any = None,
    block_seq_indent: Any = None,
    top_level_colon_align: Any = None,
    prefix_colon: Any = None,
) -> Any: ...
def dump(
    data: Any,
    stream: StreamType | None = None,
    Dumper: Any = ...,
    default_style: Any = None,
    default_flow_style: Any = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any = None,
    encoding: Any = None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Any = None,
    block_seq_indent: Any = None,
) -> Any: ...
def safe_dump(data: Any, stream: StreamType | None = None, **kwds: Any) -> Any: ...
def round_trip_dump(
    data: Any,
    stream: StreamType | None = None,
    Dumper: Any = ...,
    default_style: Any = None,
    default_flow_style: Any = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any = None,
    encoding: Any = None,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Any = None,
    block_seq_indent: Any = None,
    top_level_colon_align: Any = None,
    prefix_colon: Any = None,
) -> Any: ...
def add_implicit_resolver(
    tag: Any, regexp: Any, first: Any = None, Loader: Any = None, Dumper: Any = None, resolver: Any = ...
) -> None: ...
def add_path_resolver(
    tag: Any, path: Any, kind: Any = None, Loader: Any = None, Dumper: Any = None, resolver: Any = ...
) -> None: ...
def add_constructor(tag: Any, object_constructor: Any, Loader: Any = None, constructor: Any = ...) -> None: ...
def add_multi_constructor(tag_prefix: Any, multi_constructor: Any, Loader: Any = None, constructor: Any = ...) -> None: ...
def add_representer(data_type: Any, object_representer: Any, Dumper: Any = None, representer: Any = ...) -> None: ...
def add_multi_representer(data_type: Any, multi_representer: Any, Dumper: Any = None, representer: Any = ...) -> None: ...

class YAMLObjectMetaclass(type):
    def __init__(cls, name: Any, bases: Any, kwds: Any) -> None: ...

class YAMLObject(Incomplete):
    yaml_constructor = Constructor
    yaml_representer = Representer
    yaml_tag: Any
    yaml_flow_style: Any
    @classmethod
    def from_yaml(cls, constructor: Any, node: Any) -> Any: ...
    @classmethod
    def to_yaml(cls, representer: Any, data: Any) -> Any: ...
