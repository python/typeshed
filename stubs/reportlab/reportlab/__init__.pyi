from _typeshed import SupportsRichComparison
from typing import Literal, TypeVar

_SupportsRichComparisonT = TypeVar("_SupportsRichComparisonT", bound=SupportsRichComparison)

Version: str
__version__: str
__date__: str
__min_python_version__: tuple[int, int]

def cmp(a: _SupportsRichComparisonT, b: _SupportsRichComparisonT) -> Literal[-1, 0, 1]: ...
