__docformat__: str

from typing import ClassVar, TypeVar

from docutils.parsers import Parser
from docutils.parsers.rst.states import Inliner
from docutils.readers import standalone

_S = TypeVar("_S")

class Reader(standalone.Reader[_S]):

    settings_default_overrides: ClassVar[dict[str, int]]

    inliner_class: ClassVar[type[Inliner]]

    def __init__(self, parser: Parser | None = None, parser_name: str | None = None): ...
