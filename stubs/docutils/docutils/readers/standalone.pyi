__docformat__: str

from typing import ClassVar, TypeVar

from docutils import readers

_S = TypeVar("_S")

class Reader(readers.Reader[_S]):

    supported: ClassVar[tuple[str]]

    config_section_dependencies: ClassVar[tuple[str]]
