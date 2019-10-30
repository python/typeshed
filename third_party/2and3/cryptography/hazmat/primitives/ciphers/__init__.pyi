from abc import ABCMeta, abstractmethod

from cryptography.hazmat.backends.interfaces import CipherBackend
from cryptography.hazmat.primitives.ciphers.modes import Mode

class AEADCipherContext(metaclass=ABCMeta):
    @abstractmethod
    def authenticate_additional_data(self, data: bytes) -> None: ...

class AEADDecryptionContext(metaclass=ABCMeta):
    @abstractmethod
    def finalize_with_tag(self, tag: bytes) -> bytes: ...

class AEADEncryptionContext(metaclass=ABCMeta):
    tag: bytes

class BlockCipherAlgorithm(metaclass=ABCMeta):
    block_size: int

class Cipher(object):
    def __init__(self, algorithm: CipherAlgorithm, mode: Mode, backend: CipherBackend) -> None: ...
    def decryptor(self) -> CipherContext: ...
    def encryptor(self) -> CipherContext: ...

class CipherAlgorithm(metaclass=ABCMeta):
    key_size: int
    name: str

class CipherContext(metaclass=ABCMeta):
    @abstractmethod
    def finalize(self) -> bytes: ...
    @abstractmethod
    def update(self, data: bytes) -> bytes: ...
    @abstractmethod
    def update_into(self, data: bytes, buf) -> int: ...
