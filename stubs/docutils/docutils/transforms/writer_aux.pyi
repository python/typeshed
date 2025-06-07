from _typeshed import Incomplete

from docutils.transforms import Transform

__docformat__: str

class Compound(Transform):
    default_priority: int
    def __init__(self, document, startnode: Incomplete | None = None) -> None: ...
    def apply(self) -> None: ...

class Admonitions(Transform):
    default_priority: int
    def apply(self) -> None: ...
