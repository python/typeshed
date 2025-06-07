from typing import Any, ClassVar, Final

from docutils import Component
from docutils.nodes import _Document

__docformat__: Final = "reStructuredText"

class Parser(Component):
    settings_spec: ClassVar[tuple[Any, ...]]
    component_type: ClassVar[str]
    config_section: ClassVar[str]
    inputstring: str  # defined after call to setup_parse()
    document: _Document  # defined after call to setup_parse()
    def parse(self, inputstring: str, document: _Document) -> None: ...
    def setup_parse(self, inputstring: str, document: _Document) -> None: ...
    def finish_parse(self) -> None: ...

_parser_aliases: dict[str, str]

def get_parser_class(parser_name: str) -> type[Parser]: ...
