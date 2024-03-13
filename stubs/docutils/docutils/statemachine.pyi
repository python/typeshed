from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from re import Match, Pattern
from typing import Any, ClassVar, Generic, SupportsIndex, TypeVar, overload
from typing_extensions import Self, TypeAlias

_T = TypeVar("_T")
_Context = TypeVar("_Context")
_TransitionResult: TypeAlias = tuple[_Context, str | None, list[str]]
_TransitionMethod: TypeAlias = Callable[[Match[str], _Context, str], _TransitionResult[_Context]]
_Observer: TypeAlias = Callable[[StateMachine[_Context]], None]

class StateMachine(Generic[_Context]):
    input_lines: StringList | None
    input_offset: int
    line: str | None
    line_offset: int
    debug: bool
    initial_state: str
    current_state: str
    states: dict[str, State[_Context]]
    observers: list[_Observer[_Context]]
    def __init__(self, state_classes: Iterable[type[State[_Context]]], initial_state: str, debug: bool = False) -> None: ...
    def unlink(self) -> None: ...
    def run(
        self,
        input_lines: Sequence[str] | StringList,
        input_offset: int = 0,
        context: _Context | None = None,
        input_source: str | None = None,
        initial_state: str | None = None,
    ) -> list[str]: ...
    def get_state(self, next_state: str | None = None) -> State[_Context]: ...
    def next_line(self, n: int = 1) -> str: ...
    def is_next_line_blank(self) -> bool: ...
    def at_eof(self) -> bool: ...
    def at_bof(self) -> bool: ...
    def previous_line(self, n: int = 1) -> str | None: ...
    def goto_line(self, line_offset: int) -> str | None: ...
    def get_source(self, line_offset: int) -> str: ...
    def abs_line_offset(self) -> int: ...
    def abs_line_number(self) -> int: ...
    def get_source_and_line(self, lineno: int | None = None) -> tuple[str, int] | tuple[None, None]: ...
    def insert_input(self, input_lines: list[str] | StringList, source: str) -> None: ...
    def get_text_block(self, flush_left: bool = False) -> StringList: ...
    def check_line(
        self, context: _Context, state: State[_Context], transitions: list[str] | None = ...
    ) -> _TransitionResult[_Context]: ...
    def add_state(self, state_class: type[State[_Context]]) -> None: ...
    def add_states(self, state_classes: Iterable[type[State[_Context]]]) -> None: ...
    def runtime_init(self) -> None: ...
    def error(self) -> None: ...
    def attach_observer(self, observer: _Observer[_Context]) -> None: ...
    def detach_observer(self, observer: _Observer[_Context]) -> None: ...
    def notify_observers(self) -> None: ...

class State(Generic[_Context]):
    patterns: ClassVar[dict[str, str | Pattern[str]] | None]
    initial_transitions: ClassVar[Sequence[str] | Sequence[tuple[str, str]] | None]
    nested_sm: type[StateMachine[_Context]]
    nested_sm_kwargs: dict[str, Any]
    transition_order: list[str]
    transitions: dict[str, tuple[Pattern[str], Callable[[], None], str]]
    state_machine: StateMachine[_Context]
    debug: bool
    def __init__(self, state_machine: StateMachine[_Context], debug: bool = False) -> None: ...
    def runtime_init(self) -> None: ...
    def unlink(self) -> None: ...
    def add_initial_transitions(self) -> None: ...
    def add_transitions(self, names: Iterable[str], transitions) -> None: ...
    def add_transition(self, name: str, transition: tuple[Pattern[str], str, str]) -> None: ...
    def remove_transition(self, name: str) -> None: ...
    def make_transition(
        self, name: str, next_state: str | None = None
    ) -> tuple[Pattern[str], _TransitionMethod[_Context], str]: ...
    def make_transitions(
        self, name_list: list[str | tuple[str] | tuple[str, str]]
    ) -> tuple[list[str], dict[str, tuple[Pattern[str], _TransitionMethod[_Context], str]]]: ...
    def no_match(
        self, context: _Context, transitions: tuple[list[str], dict[str, tuple[Pattern[str], _TransitionMethod[_Context], str]]]
    ) -> _TransitionResult[_Context]: ...
    def bof(self, context: _Context) -> tuple[list[str], list[str]]: ...
    def eof(self, context: _Context) -> list[str]: ...
    def nop(self, match: Match[str], context: _Context, next_state: str) -> _TransitionResult[_Context]: ...

class StateMachineWS(StateMachine[_Context]):
    def get_indented(self, until_blank: bool = False, strip_indent: bool = True) -> tuple[StringList, int, int, bool]: ...
    def get_known_indented(
        self, indent: int, until_blank: bool = False, strip_indent: bool = True
    ) -> tuple[list[str], int, bool]: ...
    def get_first_known_indented(
        self, indent: int, until_blank: bool = False, strip_indent: bool = True, strip_top: bool = True
    ) -> tuple[list[str], int, int, bool]: ...

class StateWS(State[_Context]):
    indent_sm: type[StateMachine[_Context]] | None
    indent_sm_kwargs: dict[str, Any] | None
    known_indent_sm: type[StateMachine[_Context]] | None
    known_indent_sm_kwargs: dict[str, Any] | None
    ws_patterns: dict[str, Pattern[str]]
    ws_initial_transitions: Sequence[str]
    def __init__(self, state_machine: StateMachine[_Context], debug: bool = False) -> None: ...
    def add_initial_transitions(self) -> None: ...
    def blank(self, match: Match[str], context: _Context, next_state: str) -> _TransitionResult[_Context]: ...
    def indent(self, match: Match[str], context: _Context, next_state: str) -> _TransitionResult[_Context]: ...
    def known_indent(self, match: Match[str], context: _Context, next_state: str) -> _TransitionResult[_Context]: ...
    def first_known_indent(self, match: Match[str], context: _Context, next_state: str) -> _TransitionResult[_Context]: ...

class _SearchOverride:
    def match(self, pattern: Pattern[str]) -> Match[str]: ...

class SearchStateMachine(_SearchOverride, StateMachine[_Context]): ...
class SearchStateMachineWS(_SearchOverride, StateMachineWS[_Context]): ...

class ViewList(Generic[_T]):
    data: list[_T]
    items: list[tuple[str, int]]
    parent: Self
    parent_offset: int
    def __init__(
        self,
        initlist: Self | Sequence[_T] | None = None,
        source: str | None = None,
        items: list[tuple[str, int]] | None = None,
        parent: Self | None = None,
        parent_offset: int | None = None,
    ) -> None: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __contains__(self, item: _T) -> bool: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, i: slice) -> Self: ...
    @overload
    def __getitem__(self, i: SupportsIndex) -> _T: ...
    @overload
    def __setitem__(self, i: slice, item: Self) -> None: ...
    @overload
    def __setitem__(self, i: SupportsIndex, item: _T) -> None: ...
    def __delitem__(self, i: SupportsIndex) -> None: ...
    def __add__(self, other: Self) -> Self: ...
    def __radd__(self, other: Self) -> Self: ...
    def __iadd__(self, other: Self) -> Self: ...
    def __mul__(self, n: int) -> Self: ...
    __rmul__ = __mul__
    def __imul__(self, n: int) -> Self: ...
    def extend(self, other: Self) -> None: ...
    def append(self, item: _T, source: str | None = None, offset: int = 0) -> None: ...
    def insert(self, i: int, item: _T, source: str | None = None, offset: int = 0) -> None: ...
    def pop(self, i: int = -1) -> _T: ...
    def trim_start(self, n: int = 1) -> None: ...
    def trim_end(self, n: int = 1) -> None: ...
    def remove(self, item: _T) -> None: ...
    def count(self, item: _T) -> int: ...
    def index(self, item: _T) -> int: ...
    def reverse(self) -> None: ...
    def sort(self, *args: tuple[_T, tuple[str, int]]) -> None: ...
    def info(self, i: int) -> tuple[str, int | None]: ...
    def source(self, i: int) -> str: ...
    def offset(self, i: int) -> int: ...
    def disconnect(self) -> None: ...
    def xitems(self) -> Generator[tuple[str, int, str], None, None]: ...
    def pprint(self) -> None: ...

    # dummy atribute to indicate to mypy that ViewList is Iterable[str]
    def __iter__(self) -> Iterator[str]: ...

class StringList(ViewList[str]):
    def trim_left(self, length: int, start: int = 0, end: int = ...) -> None: ...
    def get_text_block(self, start: int, flush_left: bool = False) -> StringList: ...
    def get_indented(
        self,
        start: int = 0,
        until_blank: bool = False,
        strip_indent: bool = True,
        block_indent: int | None = None,
        first_indent: int | None = None,
    ) -> tuple[StringList, int, bool]: ...
    def get_2D_block(self, top: int, left: int, bottom: int, right: int, strip_indent: bool = True) -> StringList: ...
    def pad_double_width(self, pad_char: str) -> None: ...
    def replace(self, old: str, new: str) -> None: ...

class StateMachineError(Exception): ...
class UnknownStateError(StateMachineError): ...
class DuplicateStateError(StateMachineError): ...
class UnknownTransitionError(StateMachineError): ...
class DuplicateTransitionError(StateMachineError): ...
class TransitionPatternNotFound(StateMachineError): ...
class TransitionMethodNotFound(StateMachineError): ...
class UnexpectedIndentationError(StateMachineError): ...
class TransitionCorrection(Exception): ...
class StateCorrection(Exception): ...

def string2lines(
    astring: str, tab_width: int = 8, convert_whitespace: bool = False, whitespace: Pattern[str] = ...
) -> list[str]: ...
