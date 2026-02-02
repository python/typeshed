from _typeshed import Incomplete
from collections.abc import Generator

from pygments.filter import Filter
from pygments.formatter import Formatter
from pygments.lexer import Lexer
from pygments.style import Style

LEXER_ENTRY_POINT: str
FORMATTER_ENTRY_POINT: str
STYLE_ENTRY_POINT: str
FILTER_ENTRY_POINT: str

from importlib.metadata import EntryPoints

def iter_entry_points(group_name: str) -> EntryPoints: ...
def find_plugin_lexers() -> Generator[type[Lexer]]: ...
def find_plugin_formatters() -> Generator[tuple[str, type[Formatter[Incomplete]]]]: ...
def find_plugin_styles() -> Generator[tuple[str, type[Style]]]: ...
def find_plugin_filters() -> Generator[tuple[str, type[Filter]]]: ...
