import re
from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Iterator, Sequence
from re import RegexFlag
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from pygments.filter import Filter
from pygments.token import _TokenType
from pygments.util import Future

__all__ = [
    "Lexer",
    "RegexLexer",
    "ExtendedRegexLexer",
    "DelegatingLexer",
    "LexerContext",
    "include",
    "inherit",
    "bygroups",
    "using",
    "this",
    "default",
    "words",
    "line_re",
]

line_re: re.Pattern[str]

class LexerMeta(type):
    def __new__(cls, name: str, bases: tuple[type, ...], d: dict[str, Any]): ...
    def analyse_text(self, text: str) -> float: ...  # actually defined in class Lexer
    # ClassVars of Lexer, but same situation as with StyleMeta and Style
    name: str
    aliases: Sequence[str]  # not intended mutable
    filenames: Sequence[str]
    alias_filenames: Sequence[str]
    mimetypes: Sequence[str]
    priority: float
    url: str | None

class Lexer(metaclass=LexerMeta):
    options: dict[str, Any]
    stripnl: bool
    stripall: bool
    ensurenl: bool
    tabsize: int
    encoding: str
    filters: list[Filter]
    def __init__(self, **options: Any) -> None: ...
    def add_filter(self, filter_: str | Filter, **options: Any) -> None: ...
    def get_tokens(self, text: str, unfiltered: bool = False) -> Iterator[tuple[_TokenType, str]]: ...
    def get_tokens_unprocessed(self, text: str) -> Iterator[tuple[int, _TokenType, str]]: ...

class DelegatingLexer(Lexer):
    root_lexer: Lexer
    language_lexer: Lexer
    needle: Incomplete
    def __init__(
        self, _root_lexer: type[Lexer], _language_lexer: type[Lexer], _needle: _TokenType = ..., **options: Any
    ) -> None: ...
    def get_tokens_unprocessed(self, text: str) -> Iterator[tuple[int, _TokenType, str]]: ...

class include(str): ...
class _inherit: ...

inherit: _inherit

class combined(tuple[str, ...]):
    def __new__(cls, *args: str): ...
    def __init__(self, *args: str) -> None: ...

class _PseudoMatch:
    def __init__(self, start: int, text: str) -> None: ...
    def start(self, arg=None) -> int: ...
    def end(self, arg=None) -> int: ...
    def group(self, arg=None) -> str: ...
    def groups(self) -> tuple[str]: ...
    def groupdict(self) -> dict[str, Any]: ...

def bygroups(
    *args: _TokenType | Callable[[Lexer, _PseudoMatch, LexerContext], Iterator[tuple[int, _TokenType, str]]]
) -> Callable[[Lexer, _PseudoMatch, LexerContext], Iterator[tuple[int, _TokenType, str]]]: ...

class _This: ...

this: _This

def using(
    _other: _This | Lexer, **kwargs: Any
) -> Callable[[Lexer, _PseudoMatch, LexerContext], Iterator[tuple[int, _TokenType, str]]]: ...

class default:
    state: str
    def __init__(self, state: str) -> None: ...

class words(Future):
    words: Sequence[str]
    prefix: str
    suffix: str
    def __init__(self, words: Sequence[str], prefix: str = "", suffix: str = "") -> None: ...
    def get(self) -> str: ...

class RegexLexerMeta(LexerMeta):
    def process_tokendef(
        cls,
        name: str,
        tokendefs: (
            dict[
                str,
                list[
                    tuple[str, _TokenType | Iterator[tuple[int, _TokenType, str]]]
                    | tuple[str, _TokenType | Iterator[tuple[int, _TokenType, str]], str]
                ],
            ]
            | None
        ) = None,
    ): ...
    def get_tokendefs(
        cls,
    ) -> dict[
        str,
        list[
            tuple[str, _TokenType | Iterator[tuple[int, _TokenType, str]]]
            | tuple[str, _TokenType | Iterator[tuple[int, _TokenType, str]], str]
        ],
    ]: ...
    def __call__(cls, *args: Any, **kwds: Any) -> Any: ...

_TokenListSecondItemType: TypeAlias = (
    _TokenType
    | Iterator[tuple[int, _TokenType, str]]
    | Callable[[Lexer, _PseudoMatch, LexerContext], Iterator[tuple[int, _TokenType, str]]]
)

class RegexLexer(Lexer, metaclass=RegexLexerMeta):
    flags: ClassVar[RegexFlag]
    tokens: ClassVar[dict[str, list[tuple[str, _TokenListSecondItemType] | tuple[str, _TokenListSecondItemType, str] | include]]]
    def get_tokens_unprocessed(self, text: str, stack: Iterable[str] = ("root",)) -> Iterator[tuple[int, _TokenType, str]]: ...

class LexerContext:
    text: str
    pos: int
    end: int
    stack: list[str]
    def __init__(self, text: str, pos: int, stack: list[str] | None = None, end: int | None = None) -> None: ...

class ExtendedRegexLexer(RegexLexer):
    def get_tokens_unprocessed(  # type: ignore[override]
        self, text: str | None = None, context: LexerContext | None = None
    ) -> Iterator[tuple[int, _TokenType, str]]: ...

def do_insertions(
    insertions: list[tuple[int, list[tuple[int, _TokenType, str]]]],
    tokens: dict[
        str,
        list[
            tuple[str, _TokenType | Iterator[tuple[int, _TokenType, str]]]
            | tuple[str, _TokenType | Iterator[tuple[int, _TokenType, str]], str]
        ],
    ],
) -> Iterator[tuple[int, _TokenType, str]]: ...

class ProfilingRegexLexerMeta(RegexLexerMeta): ...

class ProfilingRegexLexer(RegexLexer, metaclass=ProfilingRegexLexerMeta):
    def get_tokens_unprocessed(self, text: str, stack: Iterable[str] = ("root",)) -> Iterator[tuple[int, _TokenType, str]]: ...
