from typing import Any

from docutils.parsers.rst import Directive

MODULEDOC: str
LEXERDOC: str
FMTERDOC: str
FILTERDOC: str

class PygmentsDoc(Directive):
    filenames: Any
    def document_lexers(self): ...
    def document_formatters(self): ...
    def document_filters(self): ...

def setup(app) -> None: ...
