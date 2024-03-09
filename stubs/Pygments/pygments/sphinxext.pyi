from typing import Any, ClassVar

from docutils.parsers.rst import Directive

MODULEDOC: str
LEXERDOC: str
FMTERDOC: str
FILTERDOC: str

class PygmentsDoc(Directive):
    has_content: ClassVar[bool]
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    option_spec: ClassVar[Any]
    filenames: Any
    def run(self): ...
    def document_lexers(self): ...
    def document_formatters(self): ...
    def document_filters(self): ...

def setup(app) -> None: ...
