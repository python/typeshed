import types
from typing import Any

def get_all_formatters() -> None: ...
def get_formatter_by_name(_alias: Any, **options: Any): ...
def load_formatter_from_file(filename: Any, formattername: str = ..., **options: Any): ...
def get_formatter_for_filename(fn: Any, **options: Any): ...

class _automodule(types.ModuleType):
    def __getattr__(self, name: Any): ...

# Names in __all__ with no definition:
#   BBCodeFormatter
#   BmpImageFormatter
#   GifImageFormatter
#   HtmlFormatter
#   IRCFormatter
#   ImageFormatter
#   JpgImageFormatter
#   LatexFormatter
#   NullFormatter
#   PangoMarkupFormatter
#   RawTokenFormatter
#   RtfFormatter
#   SvgFormatter
#   Terminal256Formatter
#   TerminalFormatter
#   TerminalTrueColorFormatter
#   TestcaseFormatter
