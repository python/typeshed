from typing import Any

from pygments.filter import Filter as Filter
from pygments.plugin import find_plugin_filters as find_plugin_filters
from pygments.token import (
    Comment as Comment,
    Error as Error,
    Keyword as Keyword,
    Name as Name,
    String as String,
    Whitespace as Whitespace,
    string_to_tokentype as string_to_tokentype,
)
from pygments.util import (
    ClassNotFound as ClassNotFound,
    OptionError as OptionError,
    get_bool_opt as get_bool_opt,
    get_choice_opt as get_choice_opt,
    get_int_opt as get_int_opt,
    get_list_opt as get_list_opt,
)

def find_filter_class(filtername): ...
def get_filter_by_name(filtername, **options): ...
def get_all_filters() -> None: ...

class CodeTagFilter(Filter):
    tag_re: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream) -> None: ...

class SymbolFilter(Filter):
    latex_symbols: Any
    isabelle_symbols: Any
    lang_map: Any
    symbols: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream) -> None: ...

class KeywordCaseFilter(Filter):
    convert: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream) -> None: ...

class NameHighlightFilter(Filter):
    names: Any
    tokentype: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream) -> None: ...

class ErrorToken(Exception): ...

class RaiseOnErrorTokenFilter(Filter):
    exception: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream) -> None: ...

class VisibleWhitespaceFilter(Filter):
    wstt: Any
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream): ...

class GobbleFilter(Filter):
    n: Any
    def __init__(self, **options) -> None: ...
    def gobble(self, value, left): ...
    def filter(self, lexer, stream) -> None: ...

class TokenMergeFilter(Filter):
    def __init__(self, **options) -> None: ...
    def filter(self, lexer, stream) -> None: ...

FILTERS: Any
