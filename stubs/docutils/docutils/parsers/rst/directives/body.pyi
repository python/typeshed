from _typeshed import Incomplete
from typing import Final

from docutils import nodes
from docutils.parsers.rst import Directive

__docformat__: Final = "reStructuredText"

class BasePseudoSection(Directive):
    required_arguments: int
    optional_arguments: int
    final_argument_whitespace: bool
    option_spec: Incomplete
    has_content: bool
    node_class: Incomplete
    def run(self): ...

class Topic(BasePseudoSection):
    node_class = nodes.topic

class Sidebar(BasePseudoSection):
    node_class = nodes.sidebar
    required_arguments: int
    optional_arguments: int
    option_spec: Incomplete
    def run(self): ...

class LineBlock(Directive):
    option_spec: Incomplete
    has_content: bool
    def run(self): ...

class ParsedLiteral(Directive):
    option_spec: Incomplete
    has_content: bool
    def run(self): ...

class CodeBlock(Directive):
    optional_arguments: int
    option_spec: Incomplete
    has_content: bool
    def run(self): ...

class MathBlock(Directive):
    option_spec: Incomplete
    has_content: bool
    def run(self): ...

class Rubric(Directive):
    required_arguments: int
    optional_arguments: int
    final_argument_whitespace: bool
    option_spec: Incomplete
    def run(self): ...

class BlockQuote(Directive):
    has_content: bool
    classes: Incomplete
    def run(self): ...

class Epigraph(BlockQuote):
    classes: Incomplete

class Highlights(BlockQuote):
    classes: Incomplete

class PullQuote(BlockQuote):
    classes: Incomplete

class Compound(Directive):
    option_spec: Incomplete
    has_content: bool
    def run(self): ...

class Container(Directive):
    optional_arguments: int
    final_argument_whitespace: bool
    option_spec: Incomplete
    has_content: bool
    def run(self): ...
