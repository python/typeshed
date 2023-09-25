from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from email.contentmanager import ContentManager
from email.errors import MessageDefect
from email.header import Header
from email.message import EmailMessage, Message
from typing import Any, TypeVar, overload
from typing_extensions import Self

__all__ = ["Compat32", "compat32", "Policy", "EmailPolicy", "default", "strict", "SMTP", "HTTP"]

_MessageT = TypeVar("_MessageT", bound=Message)

class Policy(Generic[_MessageT], metaclass=ABCMeta):
    max_line_length: int | None
    linesep: str
    cte_type: str
    raise_on_defect: bool
    mangle_from_: bool
    message_factory: Callable[[Policy], _MessageT] | None
    @overload
    def __init__(
        self: Policy[Message],
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
        message_factory: Callable[[Policy], _MessageT],
    ) -> None: ...
    def clone(self, **kw: Any) -> Self: ...
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

class EmailPolicy(Policy[_MessageT]):
    utf8: bool
    refold_source: str
    header_factory: Callable[[str, Any], Any]
    content_manager: ContentManager
    @overload
    def __init__(
        self: EmailPolicy[EmailMessage],
        *,
        max_line_length: int | None = ...,
        linesep: str = ...,
        cte_type: str = ...,
        raise_on_defect: bool = ...,
        mangle_from_: bool = ...,
        message_factory: None = None,
        utf8: bool = ...,
        refold_source: str = ...,
        header_factory: Callable[[str, str], str] = ...,
        content_manager: ContentManager = ...,
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
        message_factory: Callable[[Policy], _MessageT] | None = ...,
        utf8: bool = ...,
        refold_source: str = ...,
        header_factory: Callable[[str, str], str] = ...,
        content_manager: ContentManager = ...,
    ) -> None: ...
    def header_source_parse(self, sourcelines: list[str]) -> tuple[str, str]: ...
    def header_store_parse(self, name: str, value: Any) -> tuple[str, Any]: ...
    def header_fetch_parse(self, name: str, value: str) -> Any: ...
    def fold(self, name: str, value: str) -> Any: ...
    def fold_binary(self, name: str, value: str) -> bytes: ...

default: EmailPolicy[EmailMessage]
SMTP: EmailPolicy[EmailMessage]
SMTPUTF8: EmailPolicy[EmailMessage]
HTTP: EmailPolicy[EmailMessage]
strict: EmailPolicy[EmailMessage]
