from typing_extensions import Self
import sys
from _typeshed import SupportsWrite
from collections.abc import Generator, Iterable, Iterator, Mapping
from types import FrameType, TracebackType
from typing import Any, overload
from typing_extensions import Literal, TypeAlias

__all__ = [
    "extract_stack",
    "extract_tb",
    "format_exception",
    "format_exception_only",
    "format_list",
    "format_stack",
    "format_tb",
    "print_exc",
    "format_exc",
    "print_exception",
    "print_last",
    "print_stack",
    "print_tb",
    "clear_frames",
    "FrameSummary",
    "StackSummary",
    "TracebackException",
    "walk_stack",
    "walk_tb",
]

_PT: TypeAlias = tuple[str, int, str, str | None]

def print_tb(tb: TracebackType | None, limit: int | None = None, file: SupportsWrite[str] | None = None) -> None: ...

if sys.version_info >= (3, 10):
    @overload
    def print_exception(
        __exc: type[BaseException] | None,
        value: BaseException | None = ...,
        tb: TracebackType | None = ...,
        limit: int | None = None,
        file: SupportsWrite[str] | None = None,
        chain: bool = True,
    ) -> None: ...
    @overload
    def print_exception(
        __exc: BaseException, *, limit: int | None = None, file: SupportsWrite[str] | None = None, chain: bool = True
    ) -> None: ...
    @overload
    def format_exception(
        __exc: type[BaseException] | None,
        value: BaseException | None = ...,
        tb: TracebackType | None = ...,
        limit: int | None = None,
        chain: bool = True,
    ) -> list[str]: ...
    @overload
    def format_exception(__exc: BaseException, *, limit: int | None = None, chain: bool = True) -> list[str]: ...

else:
    def print_exception(
        etype: type[BaseException] | None,
        value: BaseException | None,
        tb: TracebackType | None,
        limit: int | None = None,
        file: SupportsWrite[str] | None = None,
        chain: bool = True,
    ) -> None: ...
    def format_exception(
        etype: type[BaseException] | None,
        value: BaseException | None,
        tb: TracebackType | None,
        limit: int | None = None,
        chain: bool = True,
    ) -> list[str]: ...

def print_exc(limit: int | None = None, file: SupportsWrite[str] | None = None, chain: bool = True) -> None: ...
def print_last(limit: int | None = None, file: SupportsWrite[str] | None = None, chain: bool = True) -> None: ...
def print_stack(f: FrameType | None = None, limit: int | None = None, file: SupportsWrite[str] | None = None) -> None: ...
def extract_tb(tb: TracebackType | None, limit: int | None = None) -> StackSummary: ...
def extract_stack(f: FrameType | None = None, limit: int | None = None) -> StackSummary: ...
def format_list(extracted_list: list[FrameSummary]) -> list[str]: ...

# undocumented
def print_list(extracted_list: list[FrameSummary], file: SupportsWrite[str] | None = None) -> None: ...

if sys.version_info >= (3, 10):
    def format_exception_only(__exc: type[BaseException] | None, value: BaseException | None = ...) -> list[str]: ...

else:
    def format_exception_only(etype: type[BaseException] | None, value: BaseException | None) -> list[str]: ...

def format_exc(limit: int | None = None, chain: bool = True) -> str: ...
def format_tb(tb: TracebackType | None, limit: int | None = None) -> list[str]: ...
def format_stack(f: FrameType | None = None, limit: int | None = None) -> list[str]: ...
def clear_frames(tb: TracebackType | None) -> None: ...
def walk_stack(f: FrameType | None) -> Iterator[tuple[FrameType, int]]: ...
def walk_tb(tb: TracebackType | None) -> Iterator[tuple[FrameType, int]]: ...

if sys.version_info >= (3, 11):
    class _ExceptionPrintContext:
        def indent(self) -> str: ...
        def emit(self, text_gen: str | Iterable[str], margin_char: str | None = None) -> Generator[str, None, None]: ...

class TracebackException:
    __cause__: TracebackException
    __context__: TracebackException
    __suppress_context__: bool
    stack: StackSummary
    exc_type: type[BaseException]
    filename: str
    lineno: int
    text: str
    offset: int
    msg: str
    if sys.version_info >= (3, 11):
        def __init__(
            self,
            exc_type: type[BaseException],
            exc_value: BaseException,
            exc_traceback: TracebackType | None,
            *,
            limit: int | None = None,
            lookup_lines: bool = True,
            capture_locals: bool = False,
            compact: bool = False,
            max_group_width: int = 15,
            max_group_depth: int = 10,
            _seen: set[int] | None = None,
        ) -> None: ...
        @classmethod
        def from_exception(
            cls,
            exc: BaseException,
            *,
            limit: int | None = ...,
            lookup_lines: bool = ...,
            capture_locals: bool = ...,
            compact: bool = ...,
            max_group_width: int = ...,
            max_group_depth: int = ...,
        ) -> Self: ...
    elif sys.version_info >= (3, 10):
        def __init__(
            self,
            exc_type: type[BaseException],
            exc_value: BaseException,
            exc_traceback: TracebackType | None,
            *,
            limit: int | None = None,
            lookup_lines: bool = True,
            capture_locals: bool = False,
            compact: bool = False,
            _seen: set[int] | None = None,
        ) -> None: ...
        @classmethod
        def from_exception(
            cls,
            exc: BaseException,
            *,
            limit: int | None = ...,
            lookup_lines: bool = ...,
            capture_locals: bool = ...,
            compact: bool = ...,
        ) -> Self: ...
    else:
        def __init__(
            self,
            exc_type: type[BaseException],
            exc_value: BaseException,
            exc_traceback: TracebackType | None,
            *,
            limit: int | None = None,
            lookup_lines: bool = True,
            capture_locals: bool = False,
            _seen: set[int] | None = None,
        ) -> None: ...
        @classmethod
        def from_exception(
            cls, exc: BaseException, *, limit: int | None = ..., lookup_lines: bool = ..., capture_locals: bool = ...
        ) -> Self: ...

    def __eq__(self, other: object) -> bool: ...
    if sys.version_info >= (3, 11):
        def format(self, *, chain: bool = True, _ctx: _ExceptionPrintContext | None = None) -> Generator[str, None, None]: ...
    else:
        def format(self, *, chain: bool = True) -> Generator[str, None, None]: ...

    def format_exception_only(self) -> Generator[str, None, None]: ...

    if sys.version_info >= (3, 11):
        def print(self, *, file: SupportsWrite[str] | None = None, chain: bool = True) -> None: ...

class FrameSummary(Iterable[Any]):
    if sys.version_info >= (3, 11):
        def __init__(
            self,
            filename: str,
            lineno: int | None,
            name: str,
            *,
            lookup_line: bool = True,
            locals: Mapping[str, str] | None = None,
            line: str | None = None,
            end_lineno: int | None = None,
            colno: int | None = None,
            end_colno: int | None = None,
        ) -> None: ...
        end_lineno: int | None
        colno: int | None
        end_colno: int | None
    else:
        def __init__(
            self,
            filename: str,
            lineno: int | None,
            name: str,
            *,
            lookup_line: bool = True,
            locals: Mapping[str, str] | None = None,
            line: str | None = None,
        ) -> None: ...
    filename: str
    lineno: int | None
    name: str
    locals: dict[str, str] | None
    @property
    def line(self) -> str | None: ...
    @overload
    def __getitem__(self, pos: Literal[0]) -> str: ...
    @overload
    def __getitem__(self, pos: Literal[1]) -> int: ...
    @overload
    def __getitem__(self, pos: Literal[2]) -> str: ...
    @overload
    def __getitem__(self, pos: Literal[3]) -> str | None: ...
    @overload
    def __getitem__(self, pos: int) -> Any: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __eq__(self, other: object) -> bool: ...
    if sys.version_info >= (3, 8):
        def __len__(self) -> Literal[4]: ...

class StackSummary(list[FrameSummary]):
    @classmethod
    def extract(
        cls,
        frame_gen: Iterable[tuple[FrameType, int]],
        *,
        limit: int | None = None,
        lookup_lines: bool = True,
        capture_locals: bool = False,
    ) -> StackSummary: ...
    @classmethod
    def from_list(cls, a_list: Iterable[FrameSummary | _PT]) -> StackSummary: ...
    if sys.version_info >= (3, 11):
        def format_frame_summary(self, frame_summary: FrameSummary) -> str: ...

    def format(self) -> list[str]: ...
