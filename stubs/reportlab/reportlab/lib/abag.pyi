from typing import Any, Final
from typing_extensions import Self

__version__: Final[str]

# NOTE: just holds an arbitrary collection of attributes, so we subclass Any
class ABag(Any):
    def __init__(self, **attr: Any) -> None: ...
    def clone(self, **attr: Any) -> Self: ...
