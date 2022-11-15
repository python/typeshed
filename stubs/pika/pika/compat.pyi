from abc import ABCMeta
from io import StringIO as StringIO
from re import Pattern
from typing import Final, Literal
from urllib.parse import parse_qs, quote, unquote, urlencode as urlencode, urlparse as urlparse

url_quote = quote
url_unquote = unquote
url_parse_qs = parse_qs

PY2: Final[Literal[False]]
PY3: Final[Literal[True]]
RE_NUM: Final[Pattern[str]]
ON_LINUX: Final[bool]
ON_OSX: Final[bool]
ON_WINDOWS: Final[bool]

class AbstractBase(metaclass=ABCMeta): ...

SOCKET_ERROR = OSError
SOL_TCP: Final[int]
basestring: Final[tuple[type[str]]]
str_or_bytes: Final[tuple[type[str], type[bytes]]]
xrange = range
unicode_type = str

def time_now(): ...
def dictkeys(dct): ...
def dictvalues(dct): ...
def dict_iteritems(dct): ...
def dict_itervalues(dct): ...
def byte(*args): ...

class long(int): ...

def canonical_str(value): ...
def is_integer(value): ...
def as_bytes(value): ...
def to_digit(value): ...
def get_linux_version(release_str: str) -> tuple[int, int, int]: ...

HAVE_SIGNAL: Final[bool]
EINTR_IS_EXPOSED: Final[Literal[False]]
LINUX_VERSION: tuple[int, int, int] | None
