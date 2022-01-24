from typing import Any

from passlib.utils import SequenceMixin

def lookup_hash(digest, return_unknown: bool = ..., required: bool = ...): ...
def norm_hash_name(name, format: str = ...): ...

class HashInfo(SequenceMixin):
    name: Any
    iana_name: Any
    aliases: Any
    const: Any
    digest_size: Any
    block_size: Any
    error_text: Any
    unknown: bool
    def __init__(self, const, names, required: bool = ...) -> None: ...
    def supported(self): ...
    def supported_by_fastpbkdf2(self): ...
    def supported_by_hashlib_pbkdf2(self): ...

def compile_hmac(digest, key, multipart: bool = ...): ...
def pbkdf1(digest, secret, salt, rounds, keylen: Any | None = ...): ...
def pbkdf2_hmac(digest, secret, salt, rounds, keylen: Any | None = ...): ...
