from collections.abc import Iterable, Iterator
from typing import Any, Literal

from wtforms.meta import _MultiDictLikeWithGetall

def clean_datetime_format_for_strptime(formats: Iterable[str]) -> list[str]: ...

class UnsetValue:
    def __bool__(self) -> Literal[False]: ...

unset_value: UnsetValue

class WebobInputWrapper:
    def __init__(self, multidict: _MultiDictLikeWithGetall) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, name: str) -> bool: ...
    def getlist(self, name: str) -> list[Any]: ...
