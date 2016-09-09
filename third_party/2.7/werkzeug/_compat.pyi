# Stubs for werkzeug._compat (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import StringIO as BytesIO

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

def wsgi_decoding_dance(s, charset='', errors=''): ...
def wsgi_encoding_dance(s, charset='', errors=''): ...
def to_bytes(x, charset=..., errors=''): ...
def to_native(x, charset=..., errors=''): ...
def reraise(tp, value, tb=None): ...

imap = ...  # type: Any
izip = ...  # type: Any
ifilter = ...  # type: Any

def to_unicode(x, charset=..., errors='', allow_none_charset=False): ...
