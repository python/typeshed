from docutils.transforms import Transform

__docformat__: str

class Filter(Transform):
    default_priority: int
    def apply(self) -> None: ...
