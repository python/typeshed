from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import TypeAlias

__version__: str

_Argv: TypeAlias = Iterable[str] | str

class DocoptLanguageError(Exception): ...

class DocoptExit(SystemExit):
    def __init__(self, message: str = ""): ...

def printable_usage(doc: str) -> str: ...
def docopt(
    doc: str, argv: _Argv | None = ..., help: bool = ..., version: Incomplete | None = ..., options_first: bool = ...
) -> dict[str, Any]: ...  # Really should be dict[str, str | bool]
