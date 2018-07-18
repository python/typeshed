import collections
from typing import Any, Optional, Mapping, Dict
from collections import Container, Iterable, MutableSet

def is_immutable(self): ...
def iter_multi_items(mapping): ...
def native_itermethods(names): ...

class ImmutableListMixin:
    def __hash__(self): ...
    def __reduce_ex__(self, protocol): ...
    def __delitem__(self, key): ...
    def __delslice__(self, i, j): ...
    def __iadd__(self, other): ...
    __imul__ = ...  # type: Any
    def __setitem__(self, key, value): ...
    def __setslice__(self, i, j, value): ...
    def append(self, item): ...
    remove = ...  # type: Any
    def extend(self, iterable): ...
    def insert(self, pos, value): ...
    def pop(self, index=-1): ...
    def reverse(self): ...
    def sort(self, cmp=None, key=None, reverse=None): ...

class ImmutableList(ImmutableListMixin, list): ...

class ImmutableDictMixin:
    @classmethod
    def fromkeys(cls, *args, **kwargs): ...
    def __reduce_ex__(self, protocol): ...
    def __hash__(self): ...
    def setdefault(self, key, default=None): ...
    def update(self, *args, **kwargs): ...
    def pop(self, key, default=None): ...
    def popitem(self): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def clear(self): ...

class ImmutableMultiDictMixin(ImmutableDictMixin):
    def __reduce_ex__(self, protocol): ...
    def add(self, key, value): ...
    def popitemlist(self): ...
    def poplist(self, key): ...
    def setlist(self, key, new_list): ...
    def setlistdefault(self, key, default_list=None): ...

class UpdateDictMixin:
    on_update = ...  # type: Any
    def setdefault(self, key, default=None): ...
    def pop(self, key, default=...): ...
    __setitem__ = ...  # type: Any
    __delitem__ = ...  # type: Any
    clear = ...  # type: Any
    popitem = ...  # type: Any
    update = ...  # type: Any

class TypeConversionDict(dict):
    def get(self, key, default=None, type=None): ...

class ImmutableTypeConversionDict(ImmutableDictMixin, TypeConversionDict):
    def copy(self): ...
    def __copy__(self): ...

class ViewItems:
    def __init__(self, multi_dict, method, repr_name, *a, **kw): ...
    def __iter__(self): ...

class MultiDict(TypeConversionDict):
    def __init__(self, mapping=None): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def add(self, key, value): ...
    def getlist(self, key, type=None): ...
    def setlist(self, key, new_list): ...
    def setdefault(self, key, default=None): ...
    def setlistdefault(self, key, default_list=None): ...
    def items(self, multi=False): ...
    def lists(self): ...
    def keys(self): ...
    __iter__ = ...  # type: Any
    def values(self): ...
    def listvalues(self): ...
    def copy(self): ...
    def deepcopy(self, memo=None): ...
    def to_dict(self, flat=True): ...
    def update(self, other_dict): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def poplist(self, key): ...
    def popitemlist(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class _omd_bucket:
    prev = ...  # type: Any
    key = ...  # type: Any
    value = ...  # type: Any
    next = ...  # type: Any
    def __init__(self, omd, key, value): ...
    def unlink(self, omd): ...

class OrderedMultiDict(MultiDict):
    def __init__(self, mapping=None): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __reduce_ex__(self, protocol): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def keys(self): ...
    __iter__ = ...  # type: Any
    def values(self): ...
    def items(self, multi=False): ...
    def lists(self): ...
    def listvalues(self): ...
    def add(self, key, value): ...
    def getlist(self, key, type=None): ...
    def setlist(self, key, new_list): ...
    def setlistdefault(self, key, default_list=None): ...
    def update(self, mapping): ...
    def poplist(self, key): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def popitemlist(self): ...

class Headers(collections.Mapping):
    def __init__(self, defaults=None): ...
    def __getitem__(self, key, _get_mode=False): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def get(self, key, default=None, type=None, as_bytes=False): ...
    def getlist(self, key, type=None, as_bytes=False): ...
    def get_all(self, name): ...
    def items(self, lower=False): ...
    def keys(self, lower=False): ...
    def values(self): ...
    def extend(self, iterable): ...
    def __delitem__(self, key: Any) -> None: ...
    def remove(self, key): ...
    def pop(self, **kwargs): ...
    def popitem(self): ...
    def __contains__(self, key): ...
    has_key = ...  # type: Any
    def __iter__(self): ...
    def __len__(self): ...
    def add(self, _key, _value, **kw): ...
    def add_header(self, _key, _value, **_kw): ...
    def clear(self): ...
    def set(self, _key, _value, **kw): ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value): ...
    def to_list(self, charset=''): ...
    def to_wsgi_list(self): ...
    def copy(self): ...
    def __copy__(self): ...

class ImmutableHeadersMixin:
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, key, value): ...
    set = ...  # type: Any
    def add(self, *args, **kwargs): ...
    remove = ...  # type: Any
    add_header = ...  # type: Any
    def extend(self, iterable): ...
    def insert(self, pos, value): ...
    def pop(self, **kwargs): ...
    def popitem(self): ...
    def setdefault(self, key, default): ...

class EnvironHeaders(ImmutableHeadersMixin, Headers):
    environ = ...  # type: Any
    def __init__(self, environ): ...
    def __eq__(self, other): ...
    def __getitem__(self, key, _get_mode=False): ...
    def __len__(self): ...
    def __iter__(self): ...
    def copy(self): ...

class CombinedMultiDict(ImmutableMultiDictMixin, MultiDict):
    def __reduce_ex__(self, protocol): ...
    dicts = ...  # type: Any
    def __init__(self, dicts=None): ...
    @classmethod
    def fromkeys(cls): ...
    def __getitem__(self, key): ...
    def get(self, key, default=None, type=None): ...
    def getlist(self, key, type=None): ...
    def keys(self): ...
    __iter__ = ...  # type: Any
    def items(self, multi=False): ...
    def values(self): ...
    def lists(self): ...
    def listvalues(self): ...
    def copy(self): ...
    def to_dict(self, flat=True): ...
    def __len__(self): ...
    def __contains__(self, key): ...
    has_key = ...  # type: Any

class FileMultiDict(MultiDict):
    def add_file(self, name, file, filename=None, content_type=None): ...

class ImmutableDict(ImmutableDictMixin, dict):
    def copy(self): ...
    def __copy__(self): ...

class ImmutableMultiDict(ImmutableMultiDictMixin, MultiDict):
    def copy(self): ...
    def __copy__(self): ...

class ImmutableOrderedMultiDict(ImmutableMultiDictMixin, OrderedMultiDict):
    def copy(self): ...
    def __copy__(self): ...

class Accept(ImmutableList):
    provided = ...  # type: Any
    def __init__(self, values=...): ...
    def __getitem__(self, key): ...
    def quality(self, key): ...
    def __contains__(self, value): ...
    def index(self, key): ...
    def find(self, key): ...
    def values(self): ...
    def to_header(self): ...
    def best_match(self, matches, default=None): ...
    @property
    def best(self): ...

class MIMEAccept(Accept):
    @property
    def accept_html(self): ...
    @property
    def accept_xhtml(self): ...
    @property
    def accept_json(self): ...

class LanguageAccept(Accept): ...
class CharsetAccept(Accept): ...

def cache_property(key, empty, type): ...

class _CacheControl(UpdateDictMixin, dict):
    no_cache = ...  # type: Any
    no_store = ...  # type: Any
    max_age = ...  # type: Any
    no_transform = ...  # type: Any
    on_update = ...  # type: Any
    provided = ...  # type: Any
    def __init__(self, values=..., on_update=None): ...
    def to_header(self): ...

class RequestCacheControl(ImmutableDictMixin, _CacheControl):
    max_stale = ...  # type: Any
    min_fresh = ...  # type: Any
    no_transform = ...  # type: Any
    only_if_cached = ...  # type: Any

class ResponseCacheControl(_CacheControl):
    public = ...  # type: Any
    private = ...  # type: Any
    must_revalidate = ...  # type: Any
    proxy_revalidate = ...  # type: Any
    s_maxage = ...  # type: Any

class CallbackDict(UpdateDictMixin, dict):
    on_update = ...  # type: Any
    def __init__(self, initial=None, on_update=None): ...

class HeaderSet(MutableSet):
    on_update = ...  # type: Any
    def __init__(self, headers=None, on_update=None): ...
    def add(self, header): ...
    def remove(self, header): ...
    def update(self, iterable): ...
    def discard(self, header): ...
    def find(self, header): ...
    def index(self, header): ...
    def clear(self): ...
    def as_set(self, preserve_casing=False): ...
    def to_header(self): ...
    def __getitem__(self, idx): ...
    def __delitem__(self, idx): ...
    def __setitem__(self, idx, value): ...
    def __contains__(self, header): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __nonzero__(self): ...

class ETags(Container, Iterable):
    star_tag = ...  # type: Any
    def __init__(self, strong_etags=None, weak_etags=None, star_tag=False): ...
    def as_set(self, include_weak=False): ...
    def is_weak(self, etag): ...
    def contains_weak(self, etag): ...
    def contains(self, etag): ...
    def contains_raw(self, etag): ...
    def to_header(self): ...
    def __call__(self, etag=None, data=None, include_weak=False): ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any
    def __iter__(self): ...
    def __contains__(self, etag): ...

class IfRange:
    etag = ...  # type: Any
    date = ...  # type: Any
    def __init__(self, etag=None, date=None): ...
    def to_header(self): ...

class Range:
    units = ...  # type: Any
    ranges = ...  # type: Any
    def __init__(self, units, ranges): ...
    def range_for_length(self, length): ...
    def make_content_range(self, length): ...
    def to_header(self): ...
    def to_content_range_header(self, length): ...

class ContentRange:
    on_update = ...  # type: Any
    def __init__(self, units, start, stop, length=None, on_update=None): ...
    units = ...  # type: Any
    start = ...  # type: Any
    stop = ...  # type: Any
    length = ...  # type: Any
    def set(self, start, stop, length=None, units=''): ...
    def unset(self): ...
    def to_header(self): ...
    def __nonzero__(self): ...
    __bool__ = ...  # type: Any

class Authorization(ImmutableDictMixin, Dict[str, Any]):
    type: str
    def __init__(self, auth_type: str, data: Optional[Mapping[str, Any]] = ...) -> None: ...
    @property
    def username(self) -> Optional[str]: ...
    @property
    def password(self) -> Optional[str]: ...
    @property
    def realm(self) -> Optional[str]: ...
    @property
    def nonce(self) -> Optional[str]: ...
    @property
    def uri(self) -> Optional[str]: ...
    @property
    def nc(self) -> Optional[str]: ...
    @property
    def cnonce(self) -> Optional[str]: ...
    @property
    def response(self) -> Optional[str]: ...
    @property
    def opaque(self) -> Optional[str]: ...
    @property
    def qop(self) -> Optional[str]: ...

class WWWAuthenticate(UpdateDictMixin, dict):
    on_update = ...  # type: Any
    def __init__(self, auth_type=None, values=None, on_update=None): ...
    def set_basic(self, realm=''): ...
    def set_digest(self, realm, nonce, qop=..., opaque=None, algorithm=None, stale=False): ...
    def to_header(self): ...
    @staticmethod
    def auth_property(name, doc=None): ...
    type = ...  # type: Any
    realm = ...  # type: Any
    domain = ...  # type: Any
    nonce = ...  # type: Any
    opaque = ...  # type: Any
    algorithm = ...  # type: Any
    qop = ...  # type: Any
    stale = ...  # type: Any

class FileStorage:
    name = ...  # type: Any
    stream = ...  # type: Any
    filename = ...  # type: Any
    headers = ...  # type: Any
    def __init__(self, stream=None, filename=None, name=None, content_type=None, content_length=None, headers=None): ...
    @property
    def content_type(self): ...
    @property
    def content_length(self): ...
    @property
    def mimetype(self): ...
    @property
    def mimetype_params(self): ...
    def save(self, dst, buffer_size=16384): ...
    def close(self): ...
    def __nonzero__(self): ...
    __bool__ = ...  # type: Any
    def __getattr__(self, name): ...
    def __iter__(self): ...
