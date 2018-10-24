import sys
from typing import Any, Optional, Text

if sys.version_info < (3,):
    import StringIO as BytesIO
else:
    from io import StringIO as BytesIO

PY2 = ...  # type: Any
WIN = ...  # type: Any
unichr = ...  # type: Any
text_type = ...  # type: Any
string_types = ...  # type: Any
integer_types = ...  # type: Any
iterkeys = ...  # type: Any
itervalues = ...  # type: Any
iteritems = ...  # type: Any
iterlists = ...  # type: Any
iterlistvalues = ...  # type: Any
int_to_byte = ...  # type: Any
iter_bytes = ...  # type: Any

def fix_tuple_repr(obj): ...
def implements_iterator(cls): ...
def implements_to_string(cls): ...
def native_string_result(func): ...
def implements_bool(cls): ...

range_type = ...  # type: Any
NativeStringIO = ...  # type: Any

def make_literal_wrapper(reference): ...
def normalize_string_tuple(tup): ...
def try_coerce_native(s): ...

wsgi_get_bytes = ...  # type: Any

def wsgi_decoding_dance(s, charset: Text = ..., errors: Text = ...): ...
def wsgi_encoding_dance(s, charset: Text = ..., errors: Text = ...): ...
def to_bytes(x, charset: Text = ..., errors: Text = ...): ...
def to_native(x, charset: Text = ..., errors: Text = ...): ...
def reraise(tp, value, tb: Optional[Any] = ...): ...

imap = ...  # type: Any
izip = ...  # type: Any
ifilter = ...  # type: Any

def to_unicode(x, charset: Text = ..., errors: Text = ..., allow_none_charset: bool = ...): ...
