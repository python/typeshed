import sys
from hashlib import _Hash
from typing import Any, Set, Dict, Optional, ClassVar, Union, Generic, TypeVar

requires_cryptography = Set[str]

def get_default_algorithms() -> Dict[str, Algorithm]: ...

_K = TypeVar("_K")

class Algorithm(Generic[_K]):
    def prepare_key(self, key: _K) -> _K: ...
    def sign(self, msg: bytes, key: _K) -> bytes: ...
    def verify(self, msg: bytes, key: _K, sig: bytes) -> bool: ...
    @staticmethod
    def to_jwk(key_obj: _K) -> str: ...
    @staticmethod
    def from_jwk(jwk: str) -> _K: ...

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
    has_alg: _HashAlg
    def __init__(self, _HashAlg) -> None: ...
    def prepare_key(self, key: Union[str, bytes]) -> bytes: ...
    @staticmethod
    def to_jwk(key_obj: Union[str, bytes]) -> Any: ...
    @staticmethod
    def from_jwk(jwk: _LoadsString) -> bytes: ...

# If cryptography is installed, also has classes RSAAlgorithm and ECAlgorithm.
