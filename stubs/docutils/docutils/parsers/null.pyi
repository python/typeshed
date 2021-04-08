from typing import ClassVar

from .. import parsers

class Parser(parsers.Parser):
    config_section_dependencies: ClassVar[tuple[str, ...]]
