from _typeshed import Incomplete
from collections.abc import Generator

from docutils.transforms import Transform

__docformat__: str

class Decorations(Transform):
    default_priority: int
    def apply(self) -> None: ...
    def generate_header(self) -> None: ...
    def generate_footer(self): ...

class ExposeInternals(Transform):
    default_priority: int
    def not_Text(self, node): ...
    def apply(self) -> None: ...

class Messages(Transform):
    default_priority: int
    def apply(self) -> None: ...

class FilterMessages(Transform):
    default_priority: int
    def apply(self) -> None: ...

class TestMessages(Transform):
    __test__: bool
    default_priority: int
    def apply(self) -> None: ...

class StripComments(Transform):
    default_priority: int
    def apply(self) -> None: ...

class StripClassesAndElements(Transform):
    default_priority: int
    strip_elements: Incomplete
    def apply(self) -> None: ...
    def check_classes(self, node): ...

class SmartQuotes(Transform):
    default_priority: int
    nodes_to_skip: Incomplete
    literal_nodes: Incomplete
    smartquotes_action: str
    unsupported_languages: Incomplete
    def __init__(self, document, startnode) -> None: ...
    def get_tokens(self, txtnodes) -> Generator[Incomplete]: ...
    def apply(self) -> None: ...
