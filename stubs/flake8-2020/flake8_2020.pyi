# flake8-2020 has type annotations, but PEP 561 states:
# This PEP does not support distributing typing information as part of module-only distributions or single-file modules within namespace packages.
# Therefore typeshed is the best place.

import ast
from collections.abc import Generator
from typing import ClassVar, Final
from typing_extensions import Self

YTT101: Final[str]
YTT102: Final[str]
YTT103: Final[str]
YTT201: Final[str]
YTT202: Final[str]
YTT203: Final[str]
YTT204: Final[str]
YTT301: Final[str]
YTT302: Final[str]
YTT303: Final[str]

class Visitor(ast.NodeVisitor): ...

class Plugin:
    name: ClassVar[str]
    version: ClassVar[str]
    def __init__(self, tree: ast.AST) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, type[Self]], None, None]: ...
