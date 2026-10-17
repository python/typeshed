from collections.abc import Callable, Sequence
from typing import ClassVar, Final

from docutils import nodes
from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

class BasePseudoSection(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    # `None` at runtime; subclasses must set this to the appropriate node class.
    # The contract specifies all subclasses must override such that it is not None.
    node_class: ClassVar[type[nodes.Element] | None]
    invalid_parents: ClassVar[
        tuple[type[nodes.Element | nodes.SubStructural | nodes.Bibliographic | nodes.Decorative | nodes.Body | nodes.Part], ...]
    ]
    def run(self) -> Sequence[nodes.Node]: ...

class Topic(BasePseudoSection):
    node_class: ClassVar[type[nodes.topic]]

class Sidebar(BasePseudoSection):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    node_class: ClassVar[type[nodes.sidebar]]
    def run(self) -> Sequence[nodes.Node]: ...

class LineBlock(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class ParsedLiteral(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class CodeBlock(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class MathBlock(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class Rubric(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class BlockQuote(Directive):
    classes: ClassVar[list[str]]
    def run(self) -> Sequence[nodes.Node]: ...

class Epigraph(BlockQuote): ...
class Highlights(BlockQuote): ...
class PullQuote(BlockQuote): ...

class Compound(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class Container(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...
