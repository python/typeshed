from collections.abc import Callable
from email._policybase import Compat32 as Compat32, Policy as Policy, compat32 as compat32
from email.contentmanager import ContentManager
from email.message import EmailMessage, Message
from typing import Any, TypeVar, overload

__all__ = ["Compat32", "compat32", "Policy", "EmailPolicy", "default", "strict", "SMTP", "HTTP"]

_MessageT = TypeVar("_MessageT", bound=Message)

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
        message_factory: Callable[[Policy[_MessageT]], _MessageT],
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
