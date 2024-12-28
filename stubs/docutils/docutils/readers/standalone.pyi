__docformat__: str

from typing import ClassVar, Literal, TypeVar

from docutils import readers

_S = TypeVar("_S")

class Reader(readers.Reader[_S]):

    supported: ClassVar[tuple[Literal["standalone"]]]

    config_section: ClassVar[Literal["standalone reader"]]
    config_section_dependencies: ClassVar[tuple[Literal["readers"]]]
