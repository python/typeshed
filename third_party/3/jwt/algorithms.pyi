import sys
from hashlib import _Hash
from typing import Any, ClassVar, Dict, Generic, Optional, Set, TypeVar, Union

requires_cryptography = Set[str]

def get_default_algorithms() -> Dict[str, Algorithm]: ...

_K = TypeVar("_K")

class Algorithm(Generic[_K]):
    def prepare_key(self, key: _K) -> _K: ...
    def sign(self, msg: bytes, key: _K) -> bytes: ...
    def verify(self, msg: bytes, key: _K, sig: bytes) -> bool: ...
    @staticmethod
    def to_jwk(key_obj: Any) -> str: ...  # should be key_obj: _K, see python/mypy#1337
    @staticmethod
    def from_jwk(jwk: str) -> Any: ...  # should return _K, see python/mypy#1337


class NoneAlgorithm(Algorithm[None]):
    def prepare_key(self, key: Optional[str]) -> None: ...

class _HashAlg:
    def __call__(self, arg: Union[bytes, bytearray, memoryview] = ...) -> _Hash: ...

if sys.version_info >= (3, 6):
    _LoadsString = Union[str, bytes, bytearray]
else:
    _LoadsString = str

class HMACAlgorithm(Algorithm[bytes]):
    SHA256: ClassVar[_HashAlg]
    SHA384: ClassVar[_HashAlg]
    SHA512: ClassVar[_HashAlg]
    hash_alg: _HashAlg
    def __init__(self, _HashAlg) -> None: ...
    def prepare_key(self, key: Union[str, bytes]) -> bytes: ...
    @staticmethod
    def to_jwk(key_obj: Union[str, bytes]) -> str: ...
    @staticmethod
    def from_jwk(jwk: _LoadsString) -> bytes: ...

# Only defined if cryptography is installed. Types should be tightened when
# cryptography gets type hints.
# See https://github.com/python/typeshed/issues/2542
class RSAAlgorithm(Algorithm):
    SHA256: ClassVar[Any]
    SHA384: ClassVar[Any]
    SHA512: ClassVar[Any]
    hash_alg: Any
    def __init__(self, hash_alg: Any) -> None: ...
    def prepare_key(self, key: Any) -> Any: ...
    @staticmethod
    def to_jwk(key_obj: Any) -> str: ...
    @staticmethod
    def from_jwk(jwk: _LoadsString) -> Any: ...
    def sign(self, msg: bytes, key: Any) -> bytes: ...
    def verify(self, msg: bytes, key: Any, sig: bytes) -> bool: ...

# Only defined if cryptography is installed. Types should be tightened when
# cryptography gets type hints.
# See https://github.com/python/typeshed/issues/2542
class ECAlgorithm(Algorithm):
    SHA256: ClassVar[Any]
    SHA384: ClassVar[Any]
    SHA512: ClassVar[Any]
    hash_alg: Any
    def __init__(self, hash_alg: Any) -> None: ...
    def prepare_key(self, key: Any) -> Any: ...
    @staticmethod
    def to_jwk(key_obj: Any) -> str: ...
    @staticmethod
    def from_jwk(jwk: _LoadsString) -> Any: ...
    def sign(self, msg: bytes, key: Any) -> bytes: ...
    def verify(self, msg: bytes, key: Any, sig: bytes) -> bool: ...

# Only defined if cryptography is installed. Types should be tightened when
# cryptography gets type hints.
# See https://github.com/python/typeshed/issues/2542
class RSAPSSAlgorithm(RSAAlgorithm):
    def sign(self, msg: bytes, key: Any) -> bytes: ...
    def verify(self, msg: bytes, key: Any, sig: bytes) -> bool: ...
