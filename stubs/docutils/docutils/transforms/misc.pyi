from docutils.transforms import Transform

__docformat__: str

class CallBack(Transform):
    default_priority: int
    def apply(self) -> None: ...

class ClassAttribute(Transform):
    default_priority: int
    def apply(self) -> None: ...

class Transitions(Transform):
    default_priority: int
    def apply(self) -> None: ...
    def visit_transition(self, node) -> None: ...
