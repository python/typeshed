# Stubs for hashlib

import sys
from abc import abstractmethod, ABCMeta
from typing import AbstractSet, Optional, Union

_DataType = Union[bytes, bytearray, memoryview]

class Hash(metaclass=ABCMeta):
    digest_size = ...  # type: int
    block_size = ...  # type: int

    # [Python documentation note] Changed in version 3.4: The name attribute has
    # been present in CPython since its inception, but until Python 3.4 was not
    # formally specified, so may not exist on some platforms
    name = ...  # type: str

    @abstractmethod
    def update(self, arg: _DataType) -> None: ...
    @abstractmethod
    def digest(self) -> bytes: ...
    @abstractmethod
    def hexdigest(self) -> str: ...
    @abstractmethod
    def copy(self) -> 'Hash': ...

def md5(arg: _DataType = ...) -> Hash: ...
def sha1(arg: _DataType = ...) -> Hash: ...
def sha224(arg: _DataType = ...) -> Hash: ...
def sha256(arg: _DataType = ...) -> Hash: ...
def sha384(arg: _DataType = ...) -> Hash: ...
def sha512(arg: _DataType = ...) -> Hash: ...

def new(name: str, data: _DataType = ...) -> Hash: ...

# New in version 3.2
algorithms_guaranteed = ...  # type: AbstractSet[str]
algorithms_available = ...  # type: AbstractSet[str]

# New in version 3.4
if sys.version_info >= (3, 4):
    def pbkdf2_hmac(hash_name: str, password: _DataType, salt: _DataType, iterations: int, dklen: Optional[int] = ...) -> bytes: ...

if sys.version_info >= (3, 6):
    class _VarLenHash(metaclass=ABCMeta):
        digest_size = ...  # type: int
        block_size = ...  # type: int
        name = ...  # type: str

        @abstractmethod
        def digest(self, length: int) -> bytes: ...
        @abstractmethod
        def hexdigest(self, length: int) -> str: ...
        @abstractmethod
        def update(self, arg: _DataType) -> None: ...
        @abstractmethod
        def copy(self) -> VarLenHash: ...

    def sha3_224(arg: _DataType = ...) -> Hash: ...
    def sha3_256(arg: _DataType = ...) -> Hash: ...
    def sha3_384(arg: _DataType = ...) -> Hash: ...
    def sha3_512(arg: _DataType = ...) -> Hash: ...

    def shake_128(arg: _DataType = ...) -> _VarLenHash: ...
    def shake_256(arg: _DataType = ...) -> _VarLenHash: ...

    def scrypt(password: _DataType, *, salt: _DataType, n: int, r: int, p: int, maxmem: int = ..., dklen: int = ...) -> bytes: ...

    class _BlakeHash(Hash):
        MAX_DIGEST_SIZE = ...  # type: int
        MAX_KEY_SIZE = ...  # type: int
        PERSON_SIZE = ...  # type: int
        SALT_SIZE = ...  # type: int

        def __init__(self, data: _DataType, digest_size: int = ..., key: _DataType = ..., salt: _DataType = ..., person: _DataType = ..., fanout: int = ..., depth: int = ..., leaf_size: int = ..., node_offset: int = ..., node_depth: int = ..., inner_size: int = ..., last_node: bool = ...) -> None: ...

    blake2b = _BlakeHash
    blake2s = _BlakeHash
