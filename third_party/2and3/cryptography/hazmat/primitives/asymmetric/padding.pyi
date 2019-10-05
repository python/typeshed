from typing import Optional

from cryptography.hazmat.primitives.hashes import HashAlgorithm

class AsymmetricPadding:
    name: str

class MGF1:
    def __init__(self, algorithm: HashAlgorithm): ...

class OAEP(AsymmetricPadding):
    def __init__(self, mgf: MGF1, algorithm: HashAlgorithm, label: Optional[bytes]): ...

class PKCS1v15(AsymmetricPadding): ...

class PSS(AsymmetricPadding):
    MAX_LENGTH: int
    def __init__(self, mgf: MGF1, salt_length: int): ...
