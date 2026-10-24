from collections.abc import Callable, Sequence
from typing import ClassVar, Final

from docutils import nodes
from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

class BaseAdmonition(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    # `None` at runtime; subclasses must set this to the appropriate admonition node class.
    # The contract specifies all subclasses must override such that it is not None.
    node_class: type[nodes.Admonition]
    def run(self) -> Sequence[nodes.Node]: ...

class Admonition(BaseAdmonition):
    node_class: type[nodes.admonition]

class Attention(BaseAdmonition):
    node_class: type[nodes.attention]

class Caution(BaseAdmonition):
    node_class: type[nodes.caution]

class Danger(BaseAdmonition):
    node_class: type[nodes.danger]

class Error(BaseAdmonition):
    node_class: type[nodes.error]

class Hint(BaseAdmonition):
    node_class: type[nodes.hint]

class Important(BaseAdmonition):
    node_class: type[nodes.important]

class Note(BaseAdmonition):
    node_class: type[nodes.note]

class Tip(BaseAdmonition):
    node_class: type[nodes.tip]

class Warning(BaseAdmonition):
    node_class: type[nodes.warning]
