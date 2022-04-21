from collections.abc import Generator, Iterator, Sequence
from email import _ParamsType, _ParamType
from email.charset import Charset
from email.contentmanager import ContentManager
from email.errors import MessageDefect
from email.policy import Policy
from typing import Any, TypeVar
from typing_extensions import TypeAlias

__all__ = ["Message", "EmailMessage"]

_T = TypeVar("_T")

_PayloadType: TypeAlias = list[Message] | str | bytes
_CharsetType: TypeAlias = Charset | str | None
_HeaderType: TypeAlias = Any

class Message:
    policy: Policy  # undocumented
    preamble: str | None
    epilogue: str | None
    defects: list[MessageDefect]
    def is_multipart(self) -> bool: ...
    def set_unixfrom(self, unixfrom: str) -> None: ...
    def get_unixfrom(self) -> str | None: ...
    def attach(self, payload: Message) -> None: ...
    def get_payload(self, i: int | None = ..., decode: bool = ...) -> Any: ...  # returns _PayloadType | None
    def set_payload(self, payload: _PayloadType, charset: _CharsetType = ...) -> None: ...
    def set_charset(self, charset: _CharsetType) -> None: ...
    def get_charset(self) -> _CharsetType: ...
    def __len__(self) -> int: ...
    def __contains__(self, name: str) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, name: str) -> _HeaderType: ...
    def __setitem__(self, name: str, val: _HeaderType) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[_HeaderType]: ...
    def items(self) -> list[tuple[str, _HeaderType]]: ...
    def get(self, name: str, failobj: _T = ...) -> _HeaderType | _T: ...
    def get_all(self, name: str, failobj: _T = ...) -> list[_HeaderType] | _T: ...
    def add_header(self, _name: str, _value: str, **_params: _ParamsType) -> None: ...
    def replace_header(self, _name: str, _value: _HeaderType) -> None: ...
    def get_content_type(self) -> str: ...
    def get_content_maintype(self) -> str: ...
    def get_content_subtype(self) -> str: ...
    def get_default_type(self) -> str: ...
    def set_default_type(self, ctype: str) -> None: ...
    def get_params(self, failobj: _T = ..., header: str = ..., unquote: bool = ...) -> list[tuple[str, str]] | _T: ...
    def get_param(self, param: str, failobj: _T = ..., header: str = ..., unquote: bool = ...) -> _T | _ParamType: ...
    def del_param(self, param: str, header: str = ..., requote: bool = ...) -> None: ...
    def set_type(self, type: str, header: str = ..., requote: bool = ...) -> None: ...
    def get_filename(self, failobj: _T = ...) -> _T | str: ...
    def get_boundary(self, failobj: _T = ...) -> _T | str: ...
    def set_boundary(self, boundary: str) -> None: ...
    def get_content_charset(self, failobj: _T = ...) -> _T | str: ...
    def get_charsets(self, failobj: _T = ...) -> _T | list[str]: ...
    def walk(self) -> Generator[Message, None, None]: ...
    def get_content_disposition(self) -> str | None: ...
    def as_string(self, unixfrom: bool = ..., maxheaderlen: int = ..., policy: Policy | None = ...) -> str: ...
    def as_bytes(self, unixfrom: bool = ..., policy: Policy | None = ...) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def set_param(
        self,
        param: str,
        value: str,
        header: str = ...,
        requote: bool = ...,
        charset: str | None = ...,
        language: str = ...,
        replace: bool = ...,
    ) -> None: ...
    def __init__(self, policy: Policy = ...) -> None: ...
    # The following two methods are undocumented, but a source code comment states that they are public API
    def set_raw(self, name: str, value: str) -> None: ...
    def raw_items(self) -> Iterator[tuple[str, str]]: ...

class MIMEPart(Message):
    def __init__(self, policy: Policy | None = ...) -> None: ...
    def get_body(self, preferencelist: Sequence[str] = ...) -> Message | None: ...
    def iter_attachments(self) -> Iterator[Message]: ...
    def iter_parts(self) -> Iterator[Message]: ...
    def get_content(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> Any: ...
    def set_content(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def make_related(self, boundary: str | None = ...) -> None: ...
    def make_alternative(self, boundary: str | None = ...) -> None: ...
    def make_mixed(self, boundary: str | None = ...) -> None: ...
    def add_related(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def add_alternative(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def add_attachment(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def clear(self) -> None: ...
    def clear_content(self) -> None: ...
    def as_string(self, unixfrom: bool = ..., maxheaderlen: int | None = ..., policy: Policy | None = ...) -> str: ...
    def is_attachment(self) -> bool: ...

class EmailMessage(MIMEPart): ...
