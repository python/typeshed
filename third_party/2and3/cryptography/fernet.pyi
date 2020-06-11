from typing import List, Optional, Text, Union

class InvalidToken(Exception): ...

class Fernet(object):
    def __init__(self, key: Union[bytes, Text]) -> None: ...
    def decrypt(self, token: bytes, ttl: Optional[int] = ...) -> bytes: ...
    def encrypt(self, data: bytes) -> bytes: ...
    def extract_timestamp(self, token: bytes) -> int: ...
    @classmethod
    def generate_key(cls) -> bytes: ...

class MultiFernet(object):
    def __init__(self, fernets: List[Fernet]) -> None: ...
    def decrypt(self, token: bytes, ttl: Optional[int] = ...) -> bytes: ...
    def encrypt(self, data: bytes) -> bytes: ...
    def rotate(self, msg: bytes) -> bytes: ...
