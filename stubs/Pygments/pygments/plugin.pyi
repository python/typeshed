from typing import Any, Iterable, Generator
from pygments.lexer import Lexer
from pygments.style import Style
from pygments.formatter import Formatter
from pygments.filter import Filter

LEXER_ENTRY_POINT: str
FORMATTER_ENTRY_POINT: str
STYLE_ENTRY_POINT: str
FILTER_ENTRY_POINT: str

def iter_entry_points(group_name: str) -> Iterable[Any]: ...
def find_plugin_lexers() -> Generator[type[Lexer], None, None]: ...
def find_plugin_formatters() -> Generator[tuple[str, type[Formatter]], None, None]: ...
def find_plugin_styles() -> Generator[tuple[str, type[Style]], None, None]: ...
def find_plugin_filters() -> Generator[tuple[str, type[Filter]], None, None]: ...
