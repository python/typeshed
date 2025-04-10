from collections.abc import Callable
from typing import Any, NoReturn, Protocol, TypeVar

from yaml.error import YAMLError

from .events import Event

_T_contra = TypeVar("_T_contra", str, bytes, contravariant=True)

class _WriteStream(Protocol[_T_contra]):
    def write(self, data: _T_contra, /) -> object: ...
    # Optional fields:
    # encoding: str
    # def flush(self) -> object: ...

class EmitterError(YAMLError): ...

class ScalarAnalysis:
    scalar: Any
    empty: Any
    multiline: Any
    allow_flow_plain: Any
    allow_block_plain: Any
    allow_single_quoted: Any
    allow_double_quoted: Any
    allow_block: Any
    def __init__(
        self, scalar, empty, multiline, allow_flow_plain, allow_block_plain, allow_single_quoted, allow_double_quoted, allow_block
    ) -> None: ...

class Emitter:
    DEFAULT_TAG_PREFIXES: dict[str, str]
    stream: _WriteStream[Any]
    encoding: str | None
    states: list[Callable[[], None]]
    state: Callable[[], None] | None
    events: list[Event]
    event: Event | None
    indents: list[int | None]
    indent: int | None
    flow_level: int
    root_context: bool
    sequence_context: bool
    mapping_context: bool
    simple_key_context: bool
    line: int
    column: int
    whitespace: bool
    indention: bool
    open_ended: bool
    canonical: bool | None
    allow_unicode: bool | None
    best_indent: int
    best_width: int
    best_line_break: str
    tag_prefixes: dict[str, str] | None
    prepared_anchor: str | None
    prepared_tag: str | None
    analysis: ScalarAnalysis | None
    style: str | None
    def __init__(
        self,
        stream: _WriteStream[Any],
        canonical: bool | None = ...,
        indent: int | None = ...,
        width: int | None = ...,
        allow_unicode: bool | None = ...,
        line_break: str | None = ...,
    ) -> None: ...
    def dispose(self) -> None: ...
    def emit(self, event: Event) -> None: ...
    def need_more_events(self) -> bool: ...
    def need_events(self, count: int) -> bool: ...
    def increase_indent(self, flow: bool = ..., indentless: bool = ...) -> None: ...
    def expect_stream_start(self) -> None: ...
    def expect_nothing(self) -> NoReturn: ...
    def expect_first_document_start(self) -> None: ...
    def expect_document_start(self, first: bool = False) -> None: ...
    def expect_document_end(self) -> None: ...
    def expect_document_root(self) -> None: ...
    def expect_node(self, root: bool = ..., sequence: bool = ..., mapping: bool = ..., simple_key: bool = ...) -> None: ...
    def expect_alias(self) -> None: ...
    def expect_scalar(self) -> None: ...
    def expect_flow_sequence(self) -> None: ...
    def expect_first_flow_sequence_item(self) -> None: ...
    def expect_flow_sequence_item(self) -> None: ...
    def expect_flow_mapping(self) -> None: ...
    def expect_first_flow_mapping_key(self) -> None: ...
    def expect_flow_mapping_key(self) -> None: ...
    def expect_flow_mapping_simple_value(self) -> None: ...
    def expect_flow_mapping_value(self) -> None: ...
    def expect_block_sequence(self) -> None: ...
    def expect_first_block_sequence_item(self) -> None: ...
    def expect_block_sequence_item(self, first: bool = ...) -> None: ...
    def expect_block_mapping(self) -> None: ...
    def expect_first_block_mapping_key(self) -> None: ...
    def expect_block_mapping_key(self, first: bool = ...) -> None: ...
    def expect_block_mapping_simple_value(self) -> None: ...
    def expect_block_mapping_value(self) -> None: ...
    def check_empty_sequence(self) -> bool: ...
    def check_empty_mapping(self) -> bool: ...
    def check_empty_document(self) -> bool: ...
    def check_simple_key(self) -> bool: ...
    def process_anchor(self, indicator: str) -> None: ...
    def process_tag(self) -> None: ...
    def choose_scalar_style(self) -> str: ...
    def process_scalar(self) -> None: ...
    def prepare_version(self, version) -> str: ...
    def prepare_tag_handle(self, handle: str) -> str: ...
    def prepare_tag_prefix(self, prefix: str) -> str: ...
    def prepare_tag(self, tag: str) -> str: ...
    def prepare_anchor(self, anchor: str) -> str: ...
    def analyze_scalar(self, scalar: str) -> ScalarAnalysis: ...
    def flush_stream(self) -> None: ...
    def write_stream_start(self) -> None: ...
    def write_stream_end(self) -> None: ...
    def write_indicator(self, indicator: str, need_whitespace: bool, whitespace: bool = ..., indention: bool = ...) -> None: ...
    def write_indent(self) -> None: ...
    def write_line_break(self, data: str | None = ...) -> None: ...
    def write_version_directive(self, version_text: str) -> None: ...
    def write_tag_directive(self, handle_text: str, prefix_text: str) -> None: ...
    def write_single_quoted(self, text: str, split: bool = ...) -> None: ...
    ESCAPE_REPLACEMENTS: dict[str, str]
    def write_double_quoted(self, text: str, split: bool = ...) -> None: ...
    def determine_block_hints(self, text: str) -> str: ...
    def write_folded(self, text: str) -> None: ...
    def write_literal(self, text: str) -> None: ...
    def write_plain(self, text: str, split: bool = ...) -> None: ...

__all__ = ["Emitter", "EmitterError"]
