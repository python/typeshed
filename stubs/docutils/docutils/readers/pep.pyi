__docformat__: str

from typing import Any, ClassVar, Literal

from docutils.parsers import Parser
from docutils.parsers.rst.states import Inliner
from docutils.readers import standalone
from docutils.transforms import Transform

class Reader(standalone.Reader):

    supported: ClassVar[tuple[str]] = ("pep",)

    settings_spec: ClassVar[tuple[Any, ...]]

    config_section: ClassVar[str]
    config_section_dependencies: ClassVar[tuple[Literal['readers'], Literal['standalone reader']]]

    def get_transforms(self) -> list[type[Transform]]: ...

    settings_default_overrides = {"pep_references": 1, "rfc_references": 1}

    inliner_class: ClassVar[type[Inliner]]

    def __init__(self, parser: Parser | None = None, parser_name: str | None = None): ...
