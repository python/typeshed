from typing import ClassVar, Final, Literal

from docutils import Component
from docutils.nodes import _Document

__docformat__: Final = "reStructuredText"

class Parser(Component):
    component_type: ClassVar[Literal["parser"]]
    config_section: ClassVar[str]
    # `input_string` is defined after calling `setup_parse()`.
    inputstring: str
    # `document` is defined after calling `setup_parse()`.
    document: _Document
    def parse(self, inputstring: str, document: _Document) -> None: ...
    def setup_parse(self, inputstring: str, document: _Document) -> None: ...
    def finish_parse(self) -> None: ...

PARSER_ALIASES: Final[dict[str, str]]

def get_parser_class(parser_name: str) -> type[Parser]: ...
