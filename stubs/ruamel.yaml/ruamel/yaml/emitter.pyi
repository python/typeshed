from _typeshed import Incomplete
from typing import Any

from ruamel.yaml.compat import StreamType
from ruamel.yaml.error import YAMLError
from ruamel.yaml.events import *

__all__ = ["Emitter", "EmitterError"]

class EmitterError(YAMLError): ...

class ScalarAnalysis:
    scalar: Incomplete
    empty: Incomplete
    multiline: Incomplete
    allow_flow_plain: Incomplete
    allow_block_plain: Incomplete
    allow_single_quoted: Incomplete
    allow_double_quoted: Incomplete
    allow_block: Incomplete
    def __init__(
        self,
        scalar: Any,
        empty: Any,
        multiline: Any,
        allow_flow_plain: bool,
        allow_block_plain: bool,
        allow_single_quoted: bool,
        allow_double_quoted: bool,
        allow_block: bool,
    ) -> None: ...

class Indents:
    values: Incomplete
    def __init__(self) -> None: ...
    def append(self, val: Any, seq: Any) -> None: ...
    def pop(self) -> Any: ...
    def seq_seq(self) -> bool: ...
    def last_seq(self) -> bool: ...
    def seq_flow_align(self, seq_indent: int, column: int, pre_comment: bool | None = False) -> int: ...
    def __len__(self) -> int: ...

class Emitter:
    DEFAULT_TAG_PREFIXES: Incomplete
    MAX_SIMPLE_KEY_LENGTH: int
    flow_seq_start: str
    flow_seq_end: str
    flow_seq_separator: str
    flow_map_start: str
    flow_map_end: str
    flow_map_separator: str
    dumper: Incomplete
    encoding: Incomplete
    allow_space_break: Incomplete
    states: Incomplete
    state: Incomplete
    events: Incomplete
    event: Incomplete
    indents: Incomplete
    indent: Incomplete
    flow_context: Incomplete
    root_context: bool
    sequence_context: bool
    mapping_context: bool
    simple_key_context: bool
    line: int
    column: int
    whitespace: bool
    indention: bool
    compact_seq_seq: bool
    compact_seq_map: bool
    no_newline: Incomplete
    open_ended: bool
    colon: str
    prefixed_colon: Incomplete
    brace_single_entry_mapping_in_flow_sequence: Incomplete
    canonical: Incomplete
    allow_unicode: Incomplete
    unicode_supplementary: Incomplete
    sequence_dash_offset: Incomplete
    top_level_colon_align: Incomplete
    best_sequence_indent: int
    requested_indent: Incomplete
    best_map_indent: Incomplete
    best_width: int
    best_line_break: str
    tag_prefixes: Incomplete
    prepared_anchor: Incomplete
    prepared_tag: Incomplete
    analysis: Incomplete
    style: Incomplete
    scalar_after_indicator: bool
    alt_null: str
    def __init__(
        self,
        stream: StreamType,
        canonical: Any = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any = None,
        block_seq_indent: int | None = None,
        top_level_colon_align: bool | None = None,
        prefix_colon: Any = None,
        brace_single_entry_mapping_in_flow_sequence: bool | None = None,
        dumper: Any = None,
    ) -> None: ...
    @property
    def stream(self) -> Any: ...
    @stream.setter
    def stream(self, val: Any) -> None: ...
    @property
    def serializer(self) -> Any: ...
    @property
    def flow_level(self) -> int: ...
    def dispose(self) -> None: ...
    def emit(self, event: Any) -> None: ...
    def need_more_events(self) -> bool: ...
    def need_events(self, count: int) -> bool: ...
    def increase_indent(self, flow: bool = False, sequence: bool | None = None, indentless: bool = False) -> None: ...
    def expect_stream_start(self) -> None: ...
    def expect_nothing(self) -> None: ...
    def expect_first_document_start(self) -> Any: ...
    def expect_document_start(self, first: bool = False) -> None: ...
    def expect_document_end(self) -> None: ...
    def expect_document_root(self) -> None: ...
    def expect_node(
        self, root: bool = False, sequence: bool = False, mapping: bool = False, simple_key: bool = False
    ) -> None: ...
    def expect_alias(self) -> None: ...
    def expect_scalar(self) -> None: ...
    def expect_flow_sequence(self, force_flow_indent: bool | None = False) -> None: ...
    def expect_first_flow_sequence_item(self) -> None: ...
    def expect_flow_sequence_item(self) -> None: ...
    def expect_flow_mapping(self, single: bool | None = False, force_flow_indent: bool | None = False) -> None: ...
    def expect_first_flow_mapping_key(self) -> None: ...
    def expect_flow_mapping_key(self) -> None: ...
    def expect_flow_mapping_simple_value(self) -> None: ...
    def expect_flow_mapping_value(self) -> None: ...
    def expect_block_sequence(self) -> None: ...
    def expect_first_block_sequence_item(self) -> Any: ...
    def expect_block_sequence_item(self, first: bool = False) -> None: ...
    def expect_block_mapping(self) -> None: ...
    def expect_first_block_mapping_key(self) -> None: ...
    def expect_block_mapping_key(self, first: Any = False) -> None: ...
    def expect_block_mapping_simple_value(self) -> None: ...
    def expect_block_mapping_value(self) -> None: ...
    def check_empty_sequence(self) -> bool: ...
    def check_empty_mapping(self) -> bool: ...
    def check_empty_document(self) -> bool: ...
    def check_simple_key(self) -> bool: ...
    def process_anchor(self, indicator: Any) -> bool: ...
    def process_tag(self) -> None: ...
    def choose_scalar_style(self) -> Any: ...
    def process_scalar(self) -> None: ...
    def prepare_version(self, version: Any) -> Any: ...
    def prepare_tag_handle(self, handle: Any) -> Any: ...
    def prepare_tag_prefix(self, prefix: Any) -> Any: ...
    def prepare_tag(self, tag: Any) -> Any: ...
    def prepare_anchor(self, anchor: Any) -> Any: ...
    def analyze_scalar(self, scalar: Any) -> Any: ...
    def flush_stream(self) -> None: ...
    def write_stream_start(self) -> None: ...
    def write_stream_end(self) -> None: ...
    def write_indicator(
        self, indicator: Any, need_whitespace: Any, whitespace: bool = False, indention: bool = False
    ) -> None: ...
    def write_indent(self) -> None: ...
    def write_line_break(self, data: Any = None) -> None: ...
    def write_version_directive(self, version_text: Any) -> None: ...
    def write_tag_directive(self, handle_text: Any, prefix_text: Any) -> None: ...
    def write_single_quoted(self, text: Any, split: Any = True) -> None: ...
    ESCAPE_REPLACEMENTS: Incomplete
    def write_double_quoted(self, text: Any, split: Any = True) -> None: ...
    def determine_block_hints(self, text: Any) -> Any: ...
    def write_folded(self, text: Any, comment: Any) -> None: ...
    def write_literal(self, text: Any, comment: Any = None) -> None: ...
    def write_plain(self, text: Any, split: Any = True) -> None: ...
    def write_comment(self, comment: Any, pre: bool = False) -> None: ...
    def write_pre_comment(self, event: Any) -> bool: ...
    def write_post_comment(self, event: Any) -> bool: ...

class RoundTripEmitter(Emitter):
    def prepare_tag(self, ctag: Any) -> Any: ...
