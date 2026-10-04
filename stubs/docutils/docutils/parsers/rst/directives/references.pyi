from collections.abc import Callable, Sequence
from typing import ClassVar, Final

from docutils import nodes
from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

class TargetNotes(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...
