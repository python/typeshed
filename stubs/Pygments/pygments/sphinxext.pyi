from typing import TypeVar

from docutils.parsers.rst import Directive

MODULEDOC: str
LEXERDOC: str
FMTERDOC: str
FILTERDOC: str

_Context = TypeVar("_Context")

class PygmentsDoc(Directive[_Context]):
    filenames: set[str]
    def document_lexers(self) -> str: ...
    def document_formatters(self) -> str: ...
    def document_filters(self) -> str: ...

def setup(app) -> None: ...
