import argparse
from typing import Any, Optional

from pygments import highlight as highlight
from pygments.filters import find_filter_class as find_filter_class, get_all_filters as get_all_filters
from pygments.formatters import (
    find_formatter_class as find_formatter_class,
    get_all_formatters as get_all_formatters,
    get_formatter_by_name as get_formatter_by_name,
    get_formatter_for_filename as get_formatter_for_filename,
    load_formatter_from_file as load_formatter_from_file,
)
from pygments.formatters.latex import LatexEmbeddedLexer as LatexEmbeddedLexer, LatexFormatter as LatexFormatter
from pygments.formatters.terminal import TerminalFormatter as TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter as Terminal256Formatter
from pygments.lexers import (
    find_lexer_class_for_filename as find_lexer_class_for_filename,
    get_all_lexers as get_all_lexers,
    get_lexer_by_name as get_lexer_by_name,
    get_lexer_for_filename as get_lexer_for_filename,
    guess_lexer as guess_lexer,
    load_lexer_from_file as load_lexer_from_file,
)
from pygments.lexers.special import TextLexer as TextLexer
from pygments.styles import get_all_styles as get_all_styles, get_style_by_name as get_style_by_name
from pygments.util import (
    ClassNotFound as ClassNotFound,
    OptionError as OptionError,
    UnclosingTextIOWrapper as UnclosingTextIOWrapper,
    docstring_headline as docstring_headline,
    guess_decode as guess_decode,
    guess_decode_from_terminal as guess_decode_from_terminal,
    terminal_encoding as terminal_encoding,
)

def main_inner(parser, argns): ...

class HelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog, indent_increment: int = ..., max_help_position: int = ..., width: Optional[Any] = ...) -> None: ...

def main(args=...): ...
