from collections.abc import Callable, MutableSequence, Sequence
from re import Match, Pattern
from types import ModuleType
from typing import Any
from typing_extensions import TypeAlias

from docutils import ApplicationError, DataError, nodes
from docutils.parsers.rst import Directive, tableparser
from docutils.statemachine import StateMachine, StateMachineWS, StateWS, Stringlist
from docutils.utils import Reporter

BasicDefinition: TypeAlias = tuple[str, str, str, list[Pattern[str]]]
DefinitionParts: TypeAlias = tuple[str, str, str, list[Pattern[str] | BasicDefinition]]
Definitiontype: TypeAlias = tuple[str, str, str, list[Pattern[str] | DefinitionParts]]

__docformat__: str

class MarkupError(DataError): ...
class UnknownInterpretedRoleError(DataError): ...
class InterpretedRoleNotImplementedError(DataError): ...
class ParserError(ApplicationError): ...
class MarkupMismatch(Exception): ...

class Struct:
    def __init__(self, **keywordargs) -> None: ...

class RSTStateMachine(StateMachineWS):
    language: ModuleType
    match_titles: bool
    memo: Struct
    document: nodes.document
    reporter: Reporter
    node: nodes.Node
    def run(
        self,
        input_lines: list[str] | Stringlist,
        document: nodes.document,
        input_offset: int = ...,
        match_titles: bool = ...,
        inliner: Inliner | None = ...,
    ) -> None: ...

class NestedStateMachine(StateMachineWS):
    match_titles: bool
    memo: Struct
    document: nodes.document
    reporter: Reporter
    language: ModuleType
    node: nodes.Node
    def run(
        self, input_lines: list[str] | Stringlist, input_offset: int, memo: Struct, node: nodes.Node, match_titles: bool = ...
    ) -> list[Any]: ...

class RSTState(StateWS):
    nested_sm: type[StateMachine]
    nested_sm_cache: list[StateMachine]
    nested_sm_kwargs: dict[str, Any]
    def __init__(self, state_machine: StateMachine, debug: bool = ...) -> None: ...
    memo: Struct
    reporter: Reporter
    inliner: Inliner
    document: nodes.document
    parent: nodes.Node
    def runtime_init(self) -> None: ...
    def goto_line(self, abs_line_offset: int) -> None: ...
    def no_match(
        self, context, transitions: tuple[list[str], dict[str, tuple[Pattern[str], Callable, str]]]
    ) -> tuple[Any, str, list]: ...
    def bof(self, context) -> tuple[list, list]: ...
    def nested_parse(
        self,
        block: Stringlist,
        input_offset: int,
        node: nodes.Node,
        match_titles: bool = ...,
        state_machine_class: type[StateMachine] | None = ...,
        state_machine_kwargs: dict[str, Any] | None = ...,
    ) -> int: ...
    def nested_list_parse(
        self,
        block,
        input_offset,
        node,
        initial_state,
        blank_finish,
        blank_finish_state: Any | None = ...,
        extra_settings: Any = ...,
        match_titles: bool = ...,
        state_machine_class: Any | None = ...,
        state_machine_kwargs: Any | None = ...,
    ) -> tuple[int, bool]: ...
    def section(self, title: str, source: str, style: str, lineno: int, messages: list[str]) -> None: ...
    def check_subsection(self, source: str, style: str, lineno: int) -> int: ...
    def title_inconsistent(self, sourcetext: str, lineno: int) -> nodes.system_message: ...
    def new_subsection(self, title: str, lineno: int, messages: list[nodes.system_message]) -> None: ...
    def paragraph(self, lines: list[str], lineno: int) -> tuple[list[nodes.Node], int]: ...
    def inline_text(self, text: str, lineno: int) -> tuple[list[nodes.Node], list[nodes.system_message]]: ...
    def unindent_warning(self, node_name: str) -> nodes.system_message: ...

def build_regexp(definition: Definitiontype, compile: bool = ...) -> Pattern[str]: ...

class Inliner:
    implicit_dispatch: list[tuple[Pattern[str], Callable]] = ...
    def __init__(self) -> None: ...
    start_string_prefix: str
    end_string_suffix: str
    parts: Definitiontype
    patterns: Any
    def init_customizations(self, settings: Any) -> None: ...
    reporter: Reporter
    document: nodes.document
    language: ModuleType
    parent: nodes.Element
    def parse(
        self, text: str, lineno: int, memo: Any, parent: nodes.Element
    ) -> tuple[list[nodes.Node], list[nodes.system_message]]: ...
    non_whitespace_before: str
    non_whitespace_escape_before: str
    non_unescaped_whitespace_escape_before: str
    non_whitespace_after: str
    simplename: str
    uric: str
    uri_end_delim: str
    urilast: str
    uri_end: str
    emailc: str
    email_pattern: str
    def quoted_start(self, match: Match[str]) -> bool: ...
    def inline_obj(
        self,
        match: Match[str],
        lineno: int,
        end_pattern: Pattern[str],
        nodeclass: nodes.TextElement,
        restore_backslashes: bool = ...,
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message], str]: ...
    def problematic(self, text: str, rawsource: str, message: nodes.system_message) -> nodes.problematic: ...
    def emphasis(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def strong(self, match: Match[str], lineno: int) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def interpreted_or_phrase_ref(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def phrase_ref(
        self, before: str, after: str, rawsource: str, escaped: str, text: str | None = None
    ) -> tuple[str, list[nodes.Node], str, list[nodes.Node]]: ...
    def adjust_uri(self, uri: str) -> str: ...
    def interpreted(
        self, rawsource: str, text: str, role: str, lineno: int
    ) -> tuple[list[nodes.Node], list[nodes.system_message]]: ...
    def literal(self, match: Match[str], lineno: int) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def inline_internal_target(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def substitution_reference(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def footnote_reference(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def reference(
        self, match: Match[str], lineno: int, anonymous: bool = ...
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def anonymous_reference(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def standalone_uri(
        self, match: Match[str], lineno: int
    ) -> list[tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]: ...
    def pep_reference(
        self, match: Match[str], lineno: int
    ) -> list[tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]: ...
    rfc_url: str
    def rfc_reference(
        self, match: Match[str], lineno: int
    ) -> list[tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]: ...
    def implicit_inline(self, text: str, lineno: int) -> list[nodes.Text]: ...
    dispatch: dict[str, Callable[[Match[str], int], tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]]

class Body(RSTState):
    double_width_pad_char: str
    enum: Any
    grid_table_top_pat: Pattern[str]
    simple_table_top_pat: Pattern[str]
    simple_table_border_pat: Pattern[str]
    pats: dict[str, str]
    patterns: dict[str, str | Pattern[str]]
    initial_transitions: Sequence[str] | Sequence[tuple[str, str]]
    def indent(self, match: Match[str], context: Any, next_state: str) -> tuple[Any, str, list[Any]]: ...
    def block_quote(self, indented: Stringlist, line_offset: int) -> list[nodes.Element]: ...
    attribution_pattern: Pattern[str]
    def split_attribution(
        self, indented: Stringlist, line_offset: int
    ) -> tuple[Stringlist, Stringlist | None, int | None, Stringlist | None, int | None]: ...
    def check_attribution(self, indented: Stringlist, attribution_start: int) -> tuple[int | None, int | None]: ...
    def parse_attribution(
        self, indented: Stringlist, line_offset: int
    ) -> tuple[nodes.attribution, list[nodes.system_message]]: ...
    def bullet(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]] | None: ...
    def list_item(self, indent: int) -> tuple[nodes.list_item, bool]: ...
    def enumerator(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def parse_enumerator(self, match: Match[str], expected_sequence: Any | None = ...) -> tuple[str, str, str, str | None]: ...
    def is_enumerated_list_item(self, ordinal: int | None, sequence: str, format: str) -> int | None: ...
    def make_enumerator(self, ordinal: int, sequence: str, format: str) -> tuple[str, str] | None: ...
    def field_marker(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def field(self, match: Match[str]) -> tuple[nodes.field, bool]: ...
    def parse_field_marker(self, match: Match[str]) -> str: ...
    def parse_field_body(self, indented: Stringlist, offset, node) -> None: ...
    def option_marker(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def option_list_item(self, match: Match[str]) -> tuple[nodes.option_list_item, bool]: ...
    def parse_option_marker(self, match: Match[str]) -> list[nodes.option | nodes.option_argument]: ...
    def doctest(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def line_block(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def line_block_line(self, match: Match[str], lineno: int) -> tuple[nodes.line, list[nodes.system_message], bool]: ...
    def nest_line_block_lines(self, block: nodes.line_block) -> None: ...
    def nest_line_block_segment(self, block: nodes.line_block) -> None: ...
    def grid_table_top(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def simple_table_top(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def table_top(
        self,
        match: Match[str],
        context: Any,
        next_state: str,
        isolate_function: Callable[
            [], tuple[list[Any], list[nodes.system_message], bool] | tuple[Stringlist, list[nodes.system_message], bool]
        ],
        parser_class: type[tableparser.GridTableParser | tableparser.SimpleTableParser],
    ) -> tuple[list[Any], str, list[Any]]: ...
    def table(
        self,
        isolate_function: Callable[[], tuple[list[Any] | Stringlist, list[nodes.system_message], bool]],
        parser_class: type[tableparser.GridTableParser | tableparser.SimpleTableParser],
    ) -> tuple[list[nodes.Node], bool]: ...
    def isolate_grid_table(
        self,
    ) -> tuple[list[Any], list[nodes.system_message], bool] | tuple[Stringlist, list[nodes.system_message], bool]: ...
    def isolate_simple_table(
        self,
    ) -> tuple[list[Any], list[nodes.system_message], bool] | tuple[Stringlist, list[nodes.system_message], bool]: ...
    def malformed_table(self, block: Stringlist, detail: str = ..., offset: int = ...) -> list[nodes.system_message]: ...
    def build_table(
        self,
        tabledata: tuple[list[int], list[list[tuple[int, int, int, Stringlist]]], list[list[tuple[int, int, int, Stringlist]]]],
        tableline: int,
        stub_columns: int = ...,
        widths: None | str | list[int] = ...,
    ) -> nodes.table: ...
    def build_table_row(self, rowdata: list[tuple[int, int, int, Stringlist]], tableline: int) -> nodes.row: ...
    explicit: Struct = ...
    def footnote(self, match: Match[str]) -> tuple[list[nodes.footnote], bool]: ...
    def citation(self, match: Match[str]) -> tuple[list[nodes.citation], bool]: ...
    def hyperlink_target(self, match: Match[str]) -> tuple[list[nodes.target], bool] | tuple[list[str], bool]: ...
    def make_target(self, block: list[str], block_text: str, lineno: int, target_name: str) -> nodes.target | str: ...
    def parse_target(self, block: list[str], block_text: str, lineno: int) -> tuple[str, str]: ...
    def is_reference(self, reference: str) -> str | None: ...
    def add_target(self, targetname: str, refuri: str | None, target: nodes.target, lineno: int) -> None: ...
    def substitution_def(
        self, match: Match[str]
    ) -> tuple[list[nodes.system_message], bool] | tuple[list[nodes.substitution_definition], bool]: ...
    def disallowed_inside_substitution_definitions(self, node: nodes.Node) -> int: ...
    def directive(
        self, match: Match[str], **option_presets: Any
    ) -> tuple[list[nodes.system_message], bool] | tuple[list[nodes.literal_block], bool]: ...
    def run_directive(
        self, directive: type[Directive], match: Match[str], type_name: str, option_presets: dict[str, Any]
    ) -> tuple[list[nodes.system_message], bool] | tuple[list[nodes.literal_block], bool]: ...
    def parse_directive_block(
        self, indented: Stringlist, line_offset: int, directive: Directive, option_presets: dict[str, Any]
    ) -> tuple[list[str], dict[str, Any], Stringlist, int]: ...
    def parse_directive_options(
        self, option_presets: dict[str, Any], option_spec: dict[str, Callable[[str], str]], arg_block: Stringlist | list[Any]
    ) -> tuple[dict[str, Any], Stringlist]: ...
    def parse_directive_arguments(self, directive: Directive, arg_block: Stringlist | list[Any]) -> list[str]: ...
    def parse_extension_options(
        self, option_spec: dict[str, Callable[[str], str]], datalines: Stringlist | list[Any]
    ) -> tuple[int, str | dict[str, Any]]: ...
    def unknown_directive(self, type_name: str) -> tuple[list[nodes.system_message], bool]: ...
    def comment(self, match: Match[str]) -> tuple[list[nodes.comment], bool]: ...
    def explicit_markup(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def explicit_construct(
        self, match: Match[str]
    ) -> (
        tuple[list[nodes.footnote], bool]
        | tuple[list[nodes.citation], bool]
        | tuple[list[nodes.target], bool]
        | tuple[list[str], bool]
        | tuple[list[nodes.system_message], bool]
        | tuple[list[nodes.substitution_definition], bool]
        | tuple[list[nodes.literal_block], bool]
        | tuple[list[nodes.comment | nodes.system_message], bool]
    ): ...
    def explicit_list(self, blank_finish: bool) -> None: ...
    def anonymous(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def anonymous_target(self, match: Match[str]) -> tuple[list[nodes.target | str], bool]: ...
    def line(self, match: Match[str], context: Any, next_state: str) -> tuple[list[str], str, list[Any]]: ...
    def text(self, match: Match[str], context: Any, next_state: str) -> tuple[list[str], str, list[Any]] | None: ...

class RFC2822Body(Body):
    patterns: dict[str, str | Pattern[str]] = ...
    initial_transitions: Sequence[tuple[str, str]] = ...
    def rfc2822(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def rfc2822_field(self, match: Match[str]) -> tuple[nodes.field, bool]: ...

class SpecializedBody(Body):
    def invalid_input(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...
    # The following base class methods are overridden by setting equal to `invalid_input`, and then overriden once again in subclasses
    def indent(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def bullet(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def enumerator(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def field_marker(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def option_marker(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def doctest(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def line_block(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def grid_table_top(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def simple_table_top(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def explicit_markup(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def anonymous(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def line(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]
    def text(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...  # type: ignore[override]

class Bulletlist(SpecializedBody):
    blank_finish: bool = ...
    def bullet(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...

class Definitionlist(SpecializedBody):
    def text(self, match: Match[str], context: Any, next_state: str) -> tuple[list[str], str, list[Any]]: ...

class Enumeratedlist(SpecializedBody):
    auto: int = ...
    blank_finish: bool = ...
    lastordinal: int = ...
    def enumerator(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...

class Fieldlist(SpecializedBody):
    blank_finish: bool = ...
    def field_marker(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...

class Optionlist(SpecializedBody):
    blank_finish: bool = ...
    def option_marker(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...

class RFC2822list(SpecializedBody, RFC2822Body):
    patterns: dict[str, str | Pattern[str]] = ...
    initial_transitions: list[tuple[str, str]] = ...
    blank_finish: bool = ...
    def rfc2822(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    # blank

class ExtensionOptions(Fieldlist):
    def parse_field_body(self, indented: Stringlist, offset: int, node: nodes.Node) -> None: ...

class LineBlock(SpecializedBody):
    # blank
    blank_finish: bool = ...
    def line_block(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...

class Explicit(SpecializedBody):
    blank_finish: bool = ...
    def explicit_markup(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def anonymous(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    # blank

class SubstitutionDef(Body):
    patterns: dict[str, str | Pattern[str]] = ...
    initial_transitions: list[str] = ...
    blank_finish: bool = ...
    def embedded_directive(self, match: Match[str], context: Any, next_state: str) -> None: ...
    def text(self, match: Match[str], context: Any, next_state: str) -> None: ...

class Text(RSTState):
    patterns: dict[str, str | Pattern[str]] = ...
    initial_transitions: list[tuple[str, str]] = ...
    def blank(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def eof(self, context: Any) -> list[Any]: ...
    def indent(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def underline(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def text(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def literal_block(self) -> list[nodes.Node] | list[nodes.literal_block | nodes.system_message]: ...
    def quoted_literal_block(self) -> list[nodes.Node]: ...
    def definition_list_item(self, termline: MutableSequence[str]) -> tuple[nodes.definition_list_item, bool]: ...
    classifier_delimiter: Pattern[str] = ...
    def term(
        self, lines: MutableSequence[str], lineno: int
    ) -> tuple[list[nodes.term | nodes.classifier], list[nodes.system_message]]: ...

class SpecializedText(Text):
    def eof(self, context: Any) -> list[Any]: ...
    def invalid_input(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...
    def blank(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...
    def indent(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...
    def underline(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...
    def text(self, match: Match[str] | None = None, context: Any | None = None, next_state: str | None = None) -> None: ...

class Definition(SpecializedText):
    def eof(self, context: Any) -> list[Any]: ...
    blank_finish: bool = ...
    def indent(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...

class Line(SpecializedText):
    eofcheck: int = ...
    def eof(self, context: Any) -> list[Any]: ...
    def blank(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def text(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    # indent
    def underline(self, match: Match[str], context: Any, next_state: str) -> tuple[list[Any], str, list[Any]]: ...
    def short_overline(self, context: Any, blocktext: str, lineno: int, lines: int = ...) -> None: ...
    def state_correction(self, context: Any, lines: int = ...) -> None: ...

class QuotedLiteralBlock(RSTState):
    patterns: dict[str, str | Pattern[str]] = ...
    initial_transitions: tuple[str, str] = ...
    messages: list[nodes.system_message] = ...
    initial_lineno: int | None = ...
    def __init__(self, state_machine: StateMachine, debug: bool = ...) -> None: ...
    def blank(self, match: Match[str], context: Any, next_state: str) -> tuple[Any, str, list[Any]]: ...
    def eof(self, context: Any) -> list[Any]: ...
    def indent(self, match: Match[str], context: Any, next_state: str) -> None: ...
    def initial_quoted(self, match: Match[str], context: Any, next_state: str) -> tuple[list[str], str, list[Any]]: ...
    def quoted(self, match: Match[str], context: Any, next_state: str) -> tuple[Any, str, list[Any]]: ...
    def text(self, match: Match[str], context: Any, next_state: str) -> None: ...

state_classes: Sequence[type[RSTState]]
