from collections.abc import Callable, Sequence
from typing import ClassVar, Final, Literal

from docutils import nodes
from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

class Contents(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    backlinks_values: ClassVar[tuple[str, ...]]
    # See the comment in the adjacent file `images.pyi` for why this is a staticmethod.
    @staticmethod
    def backlinks(arg: str) -> Literal["top", "entry"] | None: ...
    def run(self) -> Sequence[nodes.Node]: ...

class Sectnum(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class Header(Directive):
    def run(self) -> Sequence[nodes.Node]: ...

class Footer(Directive):
    def run(self) -> Sequence[nodes.Node]: ...
