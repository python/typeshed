from collections.abc import Generator
from typing import Any

from ..formatter import Formatter
from .bbcode import BBCodeFormatter as BBCodeFormatter
from .html import HtmlFormatter as HtmlFormatter
from .img import (
    BmpImageFormatter as BmpImageFormatter,
    GifImageFormatter as GifImageFormatter,
    ImageFormatter as ImageFormatter,
    JpgImageFormatter as JpgImageFormatter,
)
from .irc import IRCFormatter as IRCFormatter
from .latex import LatexFormatter as LatexFormatter
from .other import NullFormatter as NullFormatter, RawTokenFormatter as RawTokenFormatter, TestcaseFormatter as TestcaseFormatter
from .pangomarkup import PangoMarkupFormatter as PangoMarkupFormatter
from .rtf import RtfFormatter as RtfFormatter
from .svg import SvgFormatter as SvgFormatter
from .terminal import TerminalFormatter as TerminalFormatter
from .terminal256 import Terminal256Formatter as Terminal256Formatter, TerminalTrueColorFormatter as TerminalTrueColorFormatter

def get_all_formatters() -> Generator[type[Formatter[Any]], None, None]: ...
def find_formatter_class(alias: str) -> type[Formatter[Any]]: ...
def get_formatter_by_name(_alias: str, **options: Any) -> Formatter[Any]: ...
def load_formatter_from_file(filename: str, formattername: str = "CustomFormatter", **options: Any) -> Formatter[Any]: ...
def get_formatter_for_filename(fn: str, **options: Any) -> Formatter[Any]: ...
