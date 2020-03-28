# Stubs for urlparse (Python 2)

from typing import AnyStr, Dict, List, NamedTuple, Tuple, TypeVar, Sequence, Union, overload, Optional

_String = Union[str, unicode]
_AnyText = TypeVar('_AnyText', str, bytes, unicode)

uses_relative: List[str]
uses_netloc: List[str]
uses_params: List[str]
non_hierarchical: List[str]
uses_query: List[str]
uses_fragment: List[str]
scheme_chars: str
MAX_CACHE_SIZE: int

def clear_cache() -> None: ...

class ResultMixin(object):
    @property
    def username(self) -> Optional[_String]: ...
    @property
    def password(self) -> Optional[_String]: ...
    @property
    def hostname(self) -> Optional[_String]: ...
    @property
    def port(self) -> Optional[int]: ...

class _SplitResult(NamedTuple):
    scheme: _String
    netloc: _String
    path: _String
    query: _String
    fragment: _String
class SplitResult(_SplitResult, ResultMixin):
    def geturl(self) -> _String: ...

class _ParseResult(NamedTuple):
    scheme: _String
    netloc: _String
    path: _String
    params: _String
    query: _String
    fragment: _String
class ParseResult(_ParseResult, ResultMixin):
    def geturl(self) -> _String: ...

def urlparse(url: _String, scheme: _String = ...,
             allow_fragments: bool = ...) -> ParseResult: ...
def urlsplit(url: _String, scheme: _String = ...,
             allow_fragments: bool = ...) -> SplitResult: ...
@overload
def urlunparse(data: Tuple[_String, _String, _String, _String, _String, _String]) -> _String: ...
@overload
def urlunparse(data: Sequence[_String]) -> _String: ...
@overload
def urlunsplit(data: Tuple[_String, _String, _String, _String, _String]) -> _String: ...
@overload
def urlunsplit(data: Sequence[_String]) -> _String: ...
def urljoin(base: _String, url: _String,
            allow_fragments: bool = ...) -> _String: ...
def urldefrag(url: _AnyText) -> Tuple[_AnyText, _AnyText]: ...
def unquote(s: _AnyText) -> _AnyText: ...
def parse_qs(qs: _AnyText, keep_blank_values: bool = ...,
             strict_parsing: bool = ...) -> Dict[_AnyText, List[_AnyText]]: ...
def parse_qsl(qs: _AnyText, keep_blank_values: int = ...,
              strict_parsing: bool = ...) -> List[Tuple[_AnyText, _AnyText]]: ...
