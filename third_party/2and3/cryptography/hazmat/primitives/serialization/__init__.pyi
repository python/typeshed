from abc import ABCMeta
from enum import Enum
from typing import Optional

from cryptography.hazmat.backends.interfaces import DERSerializationBackend, PEMSerializationBackend

def load_pem_private_key(data: bytes, password: Optional[bytes], backend: Optional[PEMSerializationBackend] = ...): ...
def load_pem_public_key(data: bytes, backend: Optional[PEMSerializationBackend] = ...): ...
def load_der_private_key(data: bytes, password: Optional[bytes], backend: Optional[DERSerializationBackend] = ...): ...
def load_der_public_key(data: bytes, backend: Optional[DERSerializationBackend] = ...): ...
def load_ssh_public_key(data: bytes, backend): ...

class Encoding(Enum):
    PEM: Encoding
    DER: Encoding
    OpenSSH: Encoding
    Raw: Encoding
    X962: Encoding

class PrivateFormat(Enum):
    PKCS8: PrivateFormat
    TraditionalOpenSSL: PrivateFormat
    Raw: PrivateFormat

class PublicFormat(Enum):
    SubjectPublicKeyInfo: PublicFormat
    PKCS1: PublicFormat
    OpenSSH: PublicFormat
    Raw: PublicFormat
    CompressedPoint: PublicFormat
    UncompressedPoint: PublicFormat

class ParameterFormat(Enum):
    PKCS3: ParameterFormat

class KeySerializationEncryption(metaclass=ABCMeta): ...

class BestAvailableEncryption(KeySerializationEncryption):
    password: bytes
    def __init__(self, password: bytes) -> None: ...

class NoEncryption(KeySerializationEncryption): ...
