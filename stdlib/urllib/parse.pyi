import sys
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping, Sequence
from types import GenericAlias
from typing import Any, AnyStr, Final, Generic, Literal, NamedTuple, Protocol, TypeAlias, overload, type_check_only

__all__ = [
    "urlparse",
    "urlunparse",
    "urljoin",
    "urldefrag",
    "urlsplit",
    "urlunsplit",
    "urlencode",
    "parse_qs",
    "parse_qsl",
    "quote",
    "quote_plus",
    "quote_from_bytes",
    "unquote",
    "unquote_plus",
    "unquote_to_bytes",
    "DefragResult",
    "ParseResult",
    "SplitResult",
    "DefragResultBytes",
    "ParseResultBytes",
    "SplitResultBytes",
]

uses_relative: Final[list[str]]
uses_netloc: Final[list[str]]
uses_params: Final[list[str]]
non_hierarchical: Final[list[str]]
uses_query: Final[list[str]]
uses_fragment: Final[list[str]]
scheme_chars: Final[str]
if sys.version_info < (3, 11):
    MAX_CACHE_SIZE: Final[int]

class _ResultMixinStr:
    __slots__ = ()
    def encode(self, encoding: str = "ascii", errors: str = "strict") -> _ResultMixinBytes: ...

class _ResultMixinBytes:
    __slots__ = ()
    def decode(self, encoding: str = "ascii", errors: str = "strict") -> _ResultMixinStr: ...

class _NetlocResultMixinBase(Generic[AnyStr]):
    __slots__ = ()
    @property
    def username(self) -> AnyStr | None: ...
    @property
    def password(self) -> AnyStr | None: ...
    @property
    def hostname(self) -> AnyStr | None: ...
    @property
    def port(self) -> int | None: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

class _NetlocResultMixinStr(_NetlocResultMixinBase[str], _ResultMixinStr):
    __slots__ = ()

class _NetlocResultMixinBytes(_NetlocResultMixinBase[bytes], _ResultMixinBytes):
    __slots__ = ()

class _DefragResultBase(NamedTuple, Generic[AnyStr]):
    url: AnyStr
    fragment: AnyStr
    def geturl(self) -> AnyStr: ...  # type: ignore[misc]

class _SplitResultBase(NamedTuple, Generic[AnyStr]):
    scheme: AnyStr
    netloc: AnyStr
    path: AnyStr
    query: AnyStr
    fragment: AnyStr
    def geturl(self) -> AnyStr: ...  # type: ignore[misc]

class _ParseResultBase(NamedTuple, Generic[AnyStr]):
    scheme: AnyStr
    netloc: AnyStr
    path: AnyStr
    params: AnyStr
    query: AnyStr
    fragment: AnyStr
    def geturl(self) -> AnyStr: ...  # type: ignore[misc]

# Structured result objects for string data
class DefragResult(_DefragResultBase[str], _ResultMixinStr):
    def geturl(self) -> str: ...

class SplitResult(_SplitResultBase[str], _NetlocResultMixinStr):
    def geturl(self) -> str: ...

class ParseResult(_ParseResultBase[str], _NetlocResultMixinStr):
    def geturl(self) -> str: ...

# Structured result objects for bytes data
class DefragResultBytes(_DefragResultBase[bytes], _ResultMixinBytes):
    def geturl(self) -> bytes: ...

class SplitResultBytes(_SplitResultBase[bytes], _NetlocResultMixinBytes):
    def geturl(self) -> bytes: ...

class ParseResultBytes(_ParseResultBase[bytes], _NetlocResultMixinBytes):
    def geturl(self) -> bytes: ...

if sys.version_info >= (3, 15):
    @type_check_only
    class DefragResultMaybeNone(NamedTuple):
        url: str
        fragment: str | None
        def encode(self, encoding: str = "ascii", errors: str = "strict") -> DefragResultBytesMaybeNone: ...
        def geturl(self) -> str: ...

    @type_check_only
    class SplitResultMaybeNone(NamedTuple):
        scheme: str | None
        netloc: str | None
        path: str
        query: str | None
        fragment: str | None
        @property
        def username(self) -> str | None: ...
        @property
        def password(self) -> str | None: ...
        @property
        def hostname(self) -> str | None: ...
        @property
        def port(self) -> int | None: ...
        def encode(self, encoding: str = "ascii", errors: str = "strict") -> SplitResultBytesMaybeNone: ...
        def geturl(self) -> str: ...

    @type_check_only
    class ParseResultMaybeNone(NamedTuple):
        scheme: str | None
        netloc: str | None
        path: str
        params: str | None
        query: str | None
        fragment: str | None
        @property
        def username(self) -> str | None: ...
        @property
        def password(self) -> str | None: ...
        @property
        def hostname(self) -> str | None: ...
        @property
        def port(self) -> int | None: ...
        def encode(self, encoding: str = "ascii", errors: str = "strict") -> ParseResultBytesMaybeNone: ...
        def geturl(self) -> str: ...

    @type_check_only
    class DefragResultBytesMaybeNone(NamedTuple):
        url: bytes
        fragment: bytes | None
        def decode(self, encoding: str = "ascii", errors: str = "strict") -> DefragResultMaybeNone: ...
        def geturl(self) -> bytes: ...

    @type_check_only
    class SplitResultBytesMaybeNone(NamedTuple):
        scheme: bytes | None
        netloc: bytes | None
        path: bytes
        query: bytes | None
        fragment: bytes | None
        @property
        def username(self) -> bytes | None: ...
        @property
        def password(self) -> bytes | None: ...
        @property
        def hostname(self) -> bytes | None: ...
        @property
        def port(self) -> int | None: ...
        def decode(self, encoding: str = "ascii", errors: str = "strict") -> SplitResultMaybeNone: ...
        def geturl(self) -> bytes: ...

    @type_check_only
    class ParseResultBytesMaybeNone(NamedTuple):
        scheme: bytes | None
        netloc: bytes | None
        path: bytes
        params: bytes | None
        query: bytes | None
        fragment: bytes | None
        @property
        def username(self) -> bytes | None: ...
        @property
        def password(self) -> bytes | None: ...
        @property
        def hostname(self) -> bytes | None: ...
        @property
        def port(self) -> int | None: ...
        def decode(self, encoding: str = "ascii", errors: str = "strict") -> ParseResultMaybeNone: ...
        def geturl(self) -> bytes: ...

def parse_qs(
    qs: AnyStr | None,
    keep_blank_values: bool = False,
    strict_parsing: bool = False,
    encoding: str = "utf-8",
    errors: str = "replace",
    max_num_fields: int | None = None,
    separator: str = "&",
) -> dict[AnyStr, list[AnyStr]]: ...
def parse_qsl(
    qs: AnyStr | None,
    keep_blank_values: bool = False,
    strict_parsing: bool = False,
    encoding: str = "utf-8",
    errors: str = "replace",
    max_num_fields: int | None = None,
    separator: str = "&",
) -> list[tuple[AnyStr, AnyStr]]: ...
@overload
def quote(string: str, safe: str | Iterable[int] = "/", encoding: str | None = None, errors: str | None = None) -> str: ...
@overload
def quote(string: bytes | bytearray, safe: str | Iterable[int] = "/") -> str: ...
def quote_from_bytes(bs: bytes | bytearray, safe: str | Iterable[int] = "/") -> str: ...
@overload
def quote_plus(string: str, safe: str | Iterable[int] = "", encoding: str | None = None, errors: str | None = None) -> str: ...
@overload
def quote_plus(string: bytes | bytearray, safe: str | Iterable[int] = "") -> str: ...
def unquote(string: str | bytes, encoding: str = "utf-8", errors: str = "replace") -> str: ...
def unquote_to_bytes(string: str | bytes | bytearray) -> bytes: ...
def unquote_plus(string: str, encoding: str = "utf-8", errors: str = "replace") -> str: ...
@overload
def urldefrag(url: str) -> DefragResult: ...
@overload
def urldefrag(url: bytes | bytearray | None) -> DefragResultBytes: ...

if sys.version_info >= (3, 15):
    @overload
    def urldefrag(url: str, *, missing_as_none: Literal[True]) -> DefragResultMaybeNone: ...
    @overload
    def urldefrag(url: str, *, missing_as_none: Literal[False] = False) -> DefragResult: ...
    @overload
    def urldefrag(url: bytes | bytearray | None, *, missing_as_none: Literal[True]) -> DefragResultBytesMaybeNone: ...
    @overload
    def urldefrag(url: bytes | bytearray | None, *, missing_as_none: Literal[False] = False) -> DefragResultBytes: ...
    @overload
    def urldefrag(url: str, *, missing_as_none: bool) -> DefragResult | DefragResultMaybeNone: ...
    @overload
    def urldefrag(url: bytes | bytearray | None, *, missing_as_none: bool) -> DefragResultBytes | DefragResultBytesMaybeNone: ...

# The values are passed through `str()` (unless they are bytes), so anything is valid.
_QueryType: TypeAlias = (
    Mapping[str, object]
    | Mapping[bytes, object]
    | Mapping[str | bytes, object]
    | Mapping[str, Sequence[object]]
    | Mapping[bytes, Sequence[object]]
    | Mapping[str | bytes, Sequence[object]]
    | Sequence[tuple[str | bytes, object]]
    | Sequence[tuple[str | bytes, Sequence[object]]]
)

@type_check_only
class _QuoteVia(Protocol):
    @overload
    def __call__(self, string: str, safe: str | bytes, encoding: str, errors: str, /) -> str: ...
    @overload
    def __call__(self, string: bytes, safe: str | bytes, /) -> str: ...

def urlencode(
    query: _QueryType,
    doseq: bool = False,
    safe: str | bytes = "",
    encoding: str | None = None,
    errors: str | None = None,
    quote_via: _QuoteVia = ...,
) -> str: ...
def urljoin(base: AnyStr, url: AnyStr | None, allow_fragments: bool = True) -> AnyStr: ...
@overload
def urlparse(url: str, scheme: str = "", allow_fragments: bool = True) -> ParseResult: ...
@overload
def urlparse(
    url: bytes | bytearray | None, scheme: bytes | bytearray | None | Literal[""] = "", allow_fragments: bool = True
) -> ParseResultBytes: ...

if sys.version_info >= (3, 15):
    @overload
    def urlparse(
        url: str, scheme: str = "", allow_fragments: bool = True, *, missing_as_none: Literal[True]
    ) -> ParseResultMaybeNone: ...
    @overload
    def urlparse(
        url: str, scheme: str = "", allow_fragments: bool = True, *, missing_as_none: Literal[False] = False
    ) -> ParseResult: ...
    @overload
    def urlparse(
        url: bytes | bytearray | None,
        scheme: bytes | bytearray | None | Literal[""] = "",
        allow_fragments: bool = True,
        *,
        missing_as_none: Literal[True],
    ) -> ParseResultBytesMaybeNone: ...
    @overload
    def urlparse(
        url: bytes | bytearray | None,
        scheme: bytes | bytearray | None | Literal[""] = "",
        allow_fragments: bool = True,
        *,
        missing_as_none: Literal[False] = False,
    ) -> ParseResultBytes: ...
    @overload
    def urlparse(
        url: str, scheme: str = "", allow_fragments: bool = True, *, missing_as_none: bool
    ) -> ParseResult | ParseResultMaybeNone: ...
    @overload
    def urlparse(
        url: bytes | bytearray | None,
        scheme: bytes | bytearray | None | Literal[""] = "",
        allow_fragments: bool = True,
        *,
        missing_as_none: bool,
    ) -> ParseResultBytes | ParseResultBytesMaybeNone: ...

@overload
def urlsplit(url: str, scheme: str = "", allow_fragments: bool = True) -> SplitResult: ...

if sys.version_info >= (3, 11):
    @overload
    def urlsplit(
        url: bytes | None, scheme: bytes | None | Literal[""] = "", allow_fragments: bool = True
    ) -> SplitResultBytes: ...

else:
    @overload
    def urlsplit(
        url: bytes | bytearray | None, scheme: bytes | bytearray | None | Literal[""] = "", allow_fragments: bool = True
    ) -> SplitResultBytes: ...

if sys.version_info >= (3, 15):
    @overload
    def urlsplit(
        url: str, scheme: str = "", allow_fragments: bool = True, *, missing_as_none: Literal[True]
    ) -> SplitResultMaybeNone: ...
    @overload
    def urlsplit(
        url: str, scheme: str = "", allow_fragments: bool = True, *, missing_as_none: Literal[False] = False
    ) -> SplitResult: ...
    @overload
    def urlsplit(
        url: bytes | None,
        scheme: bytes | None | Literal[""] = "",
        allow_fragments: bool = True,
        *,
        missing_as_none: Literal[True],
    ) -> SplitResultBytesMaybeNone: ...
    @overload
    def urlsplit(
        url: bytes | None,
        scheme: bytes | None | Literal[""] = "",
        allow_fragments: bool = True,
        *,
        missing_as_none: Literal[False] = False,
    ) -> SplitResultBytes: ...
    @overload
    def urlsplit(
        url: str, scheme: str = "", allow_fragments: bool = True, *, missing_as_none: bool
    ) -> SplitResult | SplitResultMaybeNone: ...
    @overload
    def urlsplit(
        url: bytes | None, scheme: bytes | None | Literal[""] = "", allow_fragments: bool = True, *, missing_as_none: bool
    ) -> SplitResultBytes | SplitResultBytesMaybeNone: ...

if sys.version_info >= (3, 15):
    # Requires an iterable of length 6
    @overload
    def urlunparse(components: Iterable[None], *, keep_empty: bool | None | Incomplete = ...) -> Literal[b""]: ...  # type: ignore[overload-overlap]
    @overload
    def urlunparse(components: Iterable[AnyStr | None], *, keep_empty: bool | None | Incomplete = ...) -> AnyStr: ...

else:
    # Requires an iterable of length 6
    @overload
    def urlunparse(components: Iterable[None]) -> Literal[b""]: ...  # type: ignore[overload-overlap]
    @overload
    def urlunparse(components: Iterable[AnyStr | None]) -> AnyStr: ...

if sys.version_info >= (3, 15):
    # Requires an iterable of length 5
    @overload
    def urlunsplit(components: Iterable[None], *, keep_empty: bool | None | Incomplete = ...) -> Literal[b""]: ...  # type: ignore[overload-overlap]
    @overload
    def urlunsplit(components: Iterable[AnyStr | None], *, keep_empty: bool | None | Incomplete = ...) -> AnyStr: ...

else:
    # Requires an iterable of length 5
    @overload
    def urlunsplit(components: Iterable[None]) -> Literal[b""]: ...  # type: ignore[overload-overlap]
    @overload
    def urlunsplit(components: Iterable[AnyStr | None]) -> AnyStr: ...

def unwrap(url: str) -> str: ...
