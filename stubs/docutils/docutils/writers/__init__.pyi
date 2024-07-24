from typing import Any, ClassVar, Generic, TypeVar

from docutils import Component, nodes
from docutils.io import Output
from docutils.languages import LanguageImporter

_S = TypeVar("_S", bound=str | bytes)

class Writer(Component, Generic[_S]):

    document: ClassVar[nodes.document | None] = None

    output: _S | None = None

    language: ClassVar[LanguageImporter | None] = None

    destination: ClassVar[Output | None] = None

    parts: dict[str, Any]

    def __init__(self) -> None: ...
    def write(self, document: nodes.document, destination: Output) -> _S: ...
    def translate(self) -> None: ...
    def assemble_parts(self) -> None: ...

class UnfilteredWriter(Writer[_S]): ...

def get_writer_class(writer_name: str) -> type[Writer[str | bytes]]: ...
