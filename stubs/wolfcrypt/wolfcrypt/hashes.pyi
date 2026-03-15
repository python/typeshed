from typing import overload

class _Hash:
    def __init__(self, string: str|None=None) -> None: ...
    @classmethod
    def new(cls, string:str|None=None): ...
    def copy(self): ...
    def update(self, string: str|None) -> None: ...
    def digest(self)->bytes: ...
    def hexdigest(self)-> bytes: ...

class Sha(_Hash):
    digest_size: int

class Sha256(_Hash):
    digest_size: int

class Sha384(_Hash):
    digest_size: int

class Sha512(_Hash):
    digest_size: int

class Sha3(_Hash):
    SHA3_224_DIGEST_SIZE: int
    SHA3_256_DIGEST_SIZE: int
    SHA3_384_DIGEST_SIZE: int
    SHA3_512_DIGEST_SIZE: int
    digest_size: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, string: str, size=...) -> None: ...

class _Hmac(_Hash):
    digest_size: int
    def __init__(self, key:str|bytes, string:str|None=None) -> None: ...
    @classmethod
    def new(cls, key:str|bytes, string:str|None=None): ... # type: ignore[override]

class HmacSha(_Hmac):
    digest_size: int

class HmacSha256(_Hmac):
    digest_size: int

class HmacSha384(_Hmac):
    digest_size: int

class HmacSha512(_Hmac):
    digest_size: int

def hash_type_to_cls(hash_type: int)->type[_Hash]: ...
