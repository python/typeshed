from collections.abc import Generator, Iterator, Sequence
from email import _ParamsType, _ParamType
from email.charset import Charset
from email.contentmanager import ContentManager
from email.errors import MessageDefect
from email.policy import Policy
from typing import Any, TypeVar, overload
from typing_extensions import Self, TypeAlias

__all__ = ["Message", "EmailMessage"]

_T = TypeVar("_T")

_PayloadType: TypeAlias = list[Message] | str | bytes | bytearray
_CharsetType: TypeAlias = Charset | str | None
_HeaderType: TypeAlias = Any

class Message:
    policy: Policy[Any]  # undocumented
    preamble: str | None
    epilogue: str | None
    defects: list[MessageDefect]
    def is_multipart(self) -> bool: ...
    def set_unixfrom(self, unixfrom: str) -> None: ...
    def get_unixfrom(self) -> str | None: ...
    def attach(self, payload: Message) -> None: ...
    def get_payload(self, i: int | None = None, decode: bool = False) -> Any: ...  # returns _PayloadType | None
    def set_payload(self, payload: _PayloadType, charset: _CharsetType = None) -> None: ...
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
    @overload
    def get(self, name: str, failobj: None = None) -> _HeaderType | None: ...
    @overload
    def get(self, name: str, failobj: _T) -> _HeaderType | _T: ...
    @overload
    def get_all(self, name: str, failobj: None = None) -> list[_HeaderType] | None: ...
    @overload
    def get_all(self, name: str, failobj: _T) -> list[_HeaderType] | _T: ...
    def add_header(self, _name: str, _value: str, **_params: _ParamsType) -> None: ...
    def replace_header(self, _name: str, _value: _HeaderType) -> None: ...
    def get_content_type(self) -> str: ...
    def get_content_maintype(self) -> str: ...
    def get_content_subtype(self) -> str: ...
    def get_default_type(self) -> str: ...
    def set_default_type(self, ctype: str) -> None: ...
    @overload
    def get_params(
        self, failobj: None = None, header: str = "content-type", unquote: bool = True
    ) -> list[tuple[str, str]] | None: ...
    @overload
    def get_params(self, failobj: _T, header: str = "content-type", unquote: bool = True) -> list[tuple[str, str]] | _T: ...
    @overload
    def get_param(
        self, param: str, failobj: None = None, header: str = "content-type", unquote: bool = True
    ) -> _ParamType | None: ...
    @overload
    def get_param(self, param: str, failobj: _T, header: str = "content-type", unquote: bool = True) -> _ParamType | _T: ...
    def del_param(self, param: str, header: str = "content-type", requote: bool = True) -> None: ...
    def set_type(self, type: str, header: str = "Content-Type", requote: bool = True) -> None: ...
    @overload
    def get_filename(self, failobj: None = None) -> str | None: ...
    @overload
    def get_filename(self, failobj: _T) -> str | _T: ...
    @overload
    def get_boundary(self, failobj: None = None) -> str | None: ...
    @overload
    def get_boundary(self, failobj: _T) -> str | _T: ...
    def set_boundary(self, boundary: str) -> None: ...
    @overload
    def get_content_charset(self) -> str | None: ...
    @overload
    def get_content_charset(self, failobj: _T) -> str | _T: ...
    @overload
    def get_charsets(self, failobj: None = None) -> list[str | None]: ...
    @overload
    def get_charsets(self, failobj: _T) -> list[str | _T]: ...
    def walk(self) -> Generator[Self, None, None]: ...
    def get_content_disposition(self) -> str | None: ...
    def as_string(self, unixfrom: bool = False, maxheaderlen: int = 0, policy: Policy[Any] | None = None) -> str: ...
    def as_bytes(self, unixfrom: bool = False, policy: Policy[Any] | None = None) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def set_param(
        self,
        param: str,
        value: str,
        header: str = "Content-Type",
        requote: bool = True,
        charset: str | None = None,
        language: str = "",
        replace: bool = False,
    ) -> None: ...
    def __init__(self, policy: Policy[Any] = ...) -> None: ...
    # The following two methods are undocumented, but a source code comment states that they are public API
    def set_raw(self, name: str, value: _HeaderType) -> None: ...
    def raw_items(self) -> Iterator[tuple[str, _HeaderType]]: ...

class MIMEPart(Message):
    def __init__(self, policy: Policy[Any] | None = None) -> None: ...
    def get_body(self, preferencelist: Sequence[str] = ("related", "html", "plain")) -> Message | None: ...
    def iter_attachments(self) -> Iterator[Message]: ...
    def iter_parts(self) -> Iterator[Message]: ...
    def get_content(self, *args: Any, content_manager: ContentManager | None = None, **kw: Any) -> Any: ...
    def set_content(self, *args: Any, content_manager: ContentManager | None = None, **kw: Any) -> None: ...
    def make_related(self, boundary: str | None = None) -> None: ...
    def make_alternative(self, boundary: str | None = None) -> None: ...
    def make_mixed(self, boundary: str | None = None) -> None: ...
    def add_related(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def add_alternative(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def add_attachment(self, *args: Any, content_manager: ContentManager | None = ..., **kw: Any) -> None: ...
    def clear(self) -> None: ...
    def clear_content(self) -> None: ...
    def as_string(self, unixfrom: bool = False, maxheaderlen: int | None = None, policy: Policy[Any] | None = None) -> str: ...
    def is_attachment(self) -> bool: ...

class EmailMessage(MIMEPart): ...
