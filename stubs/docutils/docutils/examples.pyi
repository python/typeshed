from _typeshed import Incomplete
from typing import Literal, overload

from docutils.core import Publisher, _WriterParts
from docutils.io import FileInput, StringInput
from docutils.nodes import document

def html_parts(
    input_string: str,
    source_path=None,
    destination_path=None,
    input_encoding: str = "unicode",
    doctitle: bool = True,
    initial_header_level: Literal[1, 2, 3, 4, 5, 6] = 1,
) -> _WriterParts: ...
@overload
def html_body(
    input_string: str,
    source_path=None,
    destination_path=None,
    input_encoding: str = "unicode",
    output_encoding: Literal["unicode"] = "unicode",
    doctitle: bool = True,
    initial_header_level: Literal[1, 2, 3, 4, 5, 6] = 1,
) -> str: ...
@overload
def html_body(
    input_string: str,
    source_path=None,
    destination_path=None,
    input_encoding: str = "unicode",
    output_encoding: str = "unicode",
    doctitle: bool = True,
    initial_header_level: Literal[1, 2, 3, 4, 5, 6] = 1,
) -> str | bytes: ...
def internals(
    input_string,
    source_path: FileInput | StringInput | None = None,
    destination_path: FileInput | StringInput | None = None,
    input_encoding: str = "unicode",
    settings_overrides: dict[str, Incomplete] | None = None,
) -> tuple[document | None, Publisher]: ...
