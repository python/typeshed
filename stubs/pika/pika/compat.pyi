from _typeshed import Incomplete
from io import StringIO as StringIO
from urllib.parse import urlencode as urlencode, urlparse as urlparse

PY2: Incomplete
PY3: Incomplete
RE_NUM: Incomplete
ON_LINUX: Incomplete
ON_OSX: Incomplete
ON_WINDOWS: Incomplete
AbstractBase: Incomplete
SOCKET_ERROR: Incomplete
SOCKET_ERROR = OSError
SOL_TCP: Incomplete
basestring: Incomplete
str_or_bytes: Incomplete
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
def get_linux_version(release_str): ...

HAVE_SIGNAL: Incomplete
EINTR_IS_EXPOSED: Incomplete
LINUX_VERSION: Incomplete
