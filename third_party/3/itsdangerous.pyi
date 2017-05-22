from datetime import datetime
from typing import Any, Callable, IO, MutableMapping, Optional, Text, Tuple, TypeVar, Union

PY2 = ...  # type: bool
text_type = str
int_to_byte = Callable[[int], bytes]
number_types = (int, float)
izip = zip

_bytes_like = Union[bytearray, bytes]
_str_like = Union[str, bytes]
_can_become_bytes = Union[str, bytes, bytearray]
_comparable_bytes = TypeVar('_comparable_bytes', str, _bytes_like)
_serializer = Any  # must be an object that has "dumps" and "loads" attributes (e.g. the json module)

class _CompactJSON:
    def loads(self, payload: Text) -> Any: ...
    def dumps(self, obj: Any) -> Text: ...

compact_json = _CompactJSON
EPOCH = ...  # type: int

def want_bytes(s: _can_become_bytes, encoding: str='', errors: str='') -> bytes: ...
def is_text_serializer(serializer: _serializer) -> bool: ...
def constant_time_compare(val1: _comparable_bytes, val2: _comparable_bytes) -> bool: ...

class BadData(Exception):
    message = ...  # type: str
    def __init__(self, message: str) -> None: ...

class BadPayload(BadData):
    original_error = ...  # type: Optional[Exception]
    def __init__(self, message: str, original_error: Optional[Exception]=None) -> None: ...

class BadSignature(BadData):
    payload = ...  # type: Optional[Any]
    def __init__(self, message: str, payload: Optional[Any]=None) -> None: ...

class BadTimeSignature(BadSignature):
    date_signed = ...  # type: Optional[int]
    def __init__(self, message: str, payload: Optional[Any]=None, date_signed: Optional[int]=None) -> None: ...

class BadHeader(BadSignature):
    header = ...  # type: Any
    original_error = ...  # type: Any
    def __init__(self, message, payload=None, header=None, original_error=None) -> None: ...

class SignatureExpired(BadTimeSignature): ...

def base64_encode(string: _can_become_bytes) -> bytes: ...
def base64_decode(string: _can_become_bytes) -> bytes: ...
def int_to_bytes(num: int) -> bytes: ...
def bytes_to_int(bytestr: _can_become_bytes) -> bytes: ...

class SigningAlgorithm:
    def get_signature(self, key: _bytes_like, value: _bytes_like) -> bytes: ...
    def verify_signature(self, key: _bytes_like, value: _bytes_like, sig: _can_become_bytes) -> bool: ...

class NoneAlgorithm(SigningAlgorithm):
    def get_signature(self, key: _bytes_like, value: _bytes_like) -> bytes: ...

class HMACAlgorithm(SigningAlgorithm):
    default_digest_method = ...  # type: Callable
    digest_method = ...  # type: Callable
    def __init__(self, digest_method: Optional[Callable]=None) -> None: ...
    def get_signature(self, key: _bytes_like, value: _bytes_like) -> bytes: ...

class Signer:
    default_digest_method = ...  # type: Callable
    default_key_derivation = ...  # type: str
    secret_key = ...  # type: _can_become_bytes
    sep = ...  # type: _can_become_bytes
    salt = ...  # type: _can_become_bytes
    key_derivation = ...  # type: str
    digest_method = ...  # type: Callable
    algorithm = ...  # type: SigningAlgorithm
    def __init__(self, secret_key: _can_become_bytes, salt: Optional[_can_become_bytes]=None, sep: Optional[_can_become_bytes]='',
                 key_derivation: Optional[str]=None,
                 digest_method: Optional[Callable]=None,
                 algorithm: Optional[SigningAlgorithm]=None) -> None: ...
    def derive_key(self) -> bytes: ...
    def get_signature(self, value: _bytes_like) -> bytes: ...
    def sign(self, value: _bytes_like) -> bytes: ...
    def verify_signature(self, value: _bytes_like, sig: _can_become_bytes) -> bool: ...
    def unsign(self, signed_value: _can_become_bytes) -> str: ...
    def validate(self, signed_value: _can_become_bytes) -> bool: ...

class TimestampSigner(Signer):
    def get_timestamp(self) -> int: ...
    def timestamp_to_datetime(self, ts: int) -> datetime: ...
    def sign(self, value: _bytes_like) -> bytes: ...
    def unsign(self, value: _can_become_bytes, max_age: Optional[int]=None, return_timestamp: bool=False) -> Any: ...
    def validate(self, signed_value: _can_become_bytes, max_age: Optional[int]=None) -> bool: ...

class Serializer:
    default_serializer = ...  # type: _serializer
    default_signer = ...  # type: Callable[..., Signer]
    secret_key = ...  # type: Any
    salt = ...  # type: _can_become_bytes
    serializer = ...  # type: _serializer
    is_text_serializer = ...  # type: bool
    signer = ...  # type: Signer
    signer_kwargs = ...  # type: MutableMapping
    def __init__(self, secret_key: _can_become_bytes, salt: Optional[_can_become_bytes]=b'', serializer: _serializer=None, signer: Optional[Callable[..., Signer]]=None, signer_kwargs: Optional[MutableMapping]=None) -> None: ...
    def load_payload(self, payload: Any, serializer: _serializer=None) -> Any: ...
    def dump_payload(self, *args, **kwargs) -> bytes: ...
    def make_signer(self, salt: Optional[_can_become_bytes]=None) -> Signer: ...
    def dumps(self, obj: Any, salt: Optional[_can_become_bytes]=None) -> _str_like: ...
    def dump(self, obj: Any, f: IO, salt: Optional[_can_become_bytes]=None) -> None: ...
    def loads(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None) -> Any: ...
    def load(self, f: IO, salt: Optional[_can_become_bytes]=None): ...
    def loads_unsafe(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None) -> Tuple[bool, Any]: ...
    def load_unsafe(self, f: IO, *args, **kwargs) -> Tuple[bool, Any]: ...

class TimedSerializer(Serializer):
    default_signer = ...  # type: Callable[..., TimestampSigner]
    def loads(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None, max_age: Optional[int]=None, return_timestamp: bool=False) -> Any: ...
    def loads_unsafe(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None, max_age: Optional[int]=None) -> Tuple[bool, Any]: ...

class JSONWebSignatureSerializer(Serializer):
    jws_algorithms = ...  # type: MutableMapping[str, SigningAlgorithm]
    default_algorithm = ...  # type: str
    default_serializer = ...  # type: Any
    algorithm_name = ...  # type: str
    algorithm = ...  # type: Any
    def __init__(self, secret_key: _can_become_bytes, salt: Optional[_can_become_bytes]=None, serializer: _serializer=None, signer: Optional[Callable[..., Signer]]=None, signer_kwargs: Optional[MutableMapping]=None, algorithm_name: Optional[str]=None) -> None: ...
    def load_payload(self, payload: Any, serializer: _serializer = None, return_header: bool=False) -> Any: ...
    def dump_payload(self, *args, **kwargs) -> bytes: ...
    def make_algorithm(self, algorithm_name: str) -> SigningAlgorithm: ...
    def make_signer(self, salt: Optional[_can_become_bytes]=None, algorithm_name: Optional[str]=None) -> Signer: ...
    def make_header(self, header_fields=Optional[MutableMapping]) -> MutableMapping: ...
    def dumps(self, obj: Any, salt: Optional[_can_become_bytes]=None, header_fields: Optional[MutableMapping]=...) -> str: ...
    def loads(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None, return_header: bool=False) -> Any: ...
    def loads_unsafe(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None, return_header: bool=False) -> Tuple[bool, Any]: ...

class TimedJSONWebSignatureSerializer(JSONWebSignatureSerializer):
    DEFAULT_EXPIRES_IN = ...  # type: int
    expires_in = ...  # type: int
    def __init__(self, secret_key: _can_become_bytes, expires_in: Optional[int]=None, **kwargs) -> None: ...
    def make_header(self, header_fields=Optional[MutableMapping]) -> MutableMapping: ...
    def loads(self, s: _can_become_bytes, salt: Optional[_can_become_bytes]=None, return_header: bool=False) -> Any: ...
    def get_issue_date(self, header: MutableMapping) -> Optional[datetime]: ...
    def now(self) -> int: ...

class URLSafeSerializerMixin:
    def load_payload(self, payload: Any, serializer: Any = ..., **kwargs) -> Any: ...
    def dump_payload(self, *args, **kwargs) -> bytes: ...

class URLSafeSerializer(URLSafeSerializerMixin, Serializer):
    default_serializer = ...  # type: Any

class URLSafeTimedSerializer(URLSafeSerializerMixin, TimedSerializer):
    default_serializer = ...  # type: Any
