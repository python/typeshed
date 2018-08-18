from typing import Any, Optional
from enum import Enum

def load_pem_private_key(data: bytes, password: Optional[bytes], backend): ...
def load_pem_public_key(data: bytes, backend): ...
def load_der_private_key(data: bytes, password: Optional[bytes], backend): ...
def load_der_public_key(data: bytes, backend): ...
def load_ssh_public_key(data: bytes, backend): ...

class Encoding(Enum):
    PEM = ...  # type: str
    DER = ...  # type: str
    OpenSSH = ...  # type: str

class PrivateFormat(Enum):
    PKCS8 = ...  # type: str
    TraditionalOpenSSL = ...  # type: str

class PublicFormat(Enum):
    SubjectPublicKeyInfo = ...  # type: str
    PKCS1 = ...  # type: str
    OpenSSH = ...  # type: str

class ParameterFormat(Enum):
    PKCS3 = ...  # type: str

class KeySerializationEncryption: ...

class BestAvailableEncryption(KeySerializationEncryption):
    password = ...  # type: Any
    def __init__(self, password) -> None: ...

class NoEncryption(KeySerializationEncryption): ...
