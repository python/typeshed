# mypy: disable-error-code="attr-defined"

from abc import ABCMeta
from collections.abc import Iterable
from typing import Protocol, TypeVar

_T = TypeVar("_T")

class BasePathMixin(Protocol):
    uri: str | None
    @property
    def absolute_uri(self) -> str: ...
    @property
    def base_path(self) -> str: ...
    @base_path.setter
    def base_path(self, newbase_path: str) -> None: ...
    def get_path_from_uri(self) -> str: ...

class GroupedBasePathMixin(Iterable[_T], metaclass=ABCMeta):
    @property
    def base_uri(self) -> str: ...
    @base_uri.setter
    def base_uri(self, __new_url: str, /) -> None: ...
    @property
    def base_path(self) -> str: ...
    @base_path.setter
    def base_path(self, __new_url: str, /) -> None: ...
