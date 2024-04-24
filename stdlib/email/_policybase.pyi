from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from email.errors import MessageDefect
from email.header import Header
from email.message import Message
from typing import Any, Generic, TypeVar
from typing_extensions import Self

_MessageT = TypeVar("_MessageT", bound=Message)

class _PolicyBase:
    def __add__(self, other: Any) -> Self: ...
    def clone(self, **kw: Any) -> Self: ...

class Policy(_PolicyBase, Generic[_MessageT], metaclass=ABCMeta):
    max_line_length: int | None
    linesep: str
    cte_type: str
    raise_on_defect: bool
    mangle_from_: bool
    message_factory: Callable[[[_MessageT]], [_MessageT]] | None
    @overload
    def __init__(
        self: Policy[Message[str, str]],
        *,
        max_line_length: int | None = ...,
        linesep: str = ...,
        cte_type: str = ...,
        raise_on_defect: bool = ...,
        mangle_from_: bool = ...,
        message_factory: None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        max_line_length: int | None = ...,
        linesep: str = ...,
        cte_type: str = ...,
        raise_on_defect: bool = ...,
        mangle_from_: bool = ...,
        message_factory: Callable[[Policy[_MessageT]], _MessageT],
    ) -> None: ...
    def handle_defect(self, obj: _MessageT, defect: MessageDefect) -> None: ...
    def register_defect(self, obj: _MessageT, defect: MessageDefect) -> None: ...
    def header_max_count(self, name: str) -> int | None: ...
    @abstractmethod
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    @abstractmethod
    def header_store_parse(self, name: str, value: str) -> tuple[str, str]: ...
    @abstractmethod
    def header_fetch_parse(self, name: str, value: str) -> str: ...
    @abstractmethod
    def fold(self, name: str, value: str) -> str: ...
    @abstractmethod
    def fold_binary(self, name: str, value: str) -> bytes: ...

class Compat32(Policy[_MessageT]):
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    def header_store_parse(self, name: str, value: str) -> tuple[str, str]: ...
    def header_fetch_parse(self, name: str, value: str) -> str | Header: ...  # type: ignore[override]
    def fold(self, name: str, value: str) -> str: ...
    def fold_binary(self, name: str, value: str) -> bytes: ...

compat32: Compat32[Message]
