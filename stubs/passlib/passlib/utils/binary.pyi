from _typeshed import Incomplete
from typing import Any

BASE64_CHARS: Any
AB64_CHARS: Any
HASH64_CHARS: Any
BCRYPT_CHARS: Any
PADDED_BASE64_CHARS: Any
HEX_CHARS: Any
UPPER_HEX_CHARS: Any
LOWER_HEX_CHARS: Any
ALL_BYTE_VALUES: Any

def compile_byte_translation(mapping, source: Incomplete | None = ...): ...
def b64s_encode(data): ...
def b64s_decode(data): ...
def ab64_encode(data): ...
def ab64_decode(data): ...
def b32encode(source): ...
def b32decode(source): ...

class Base64Engine:
    bytemap: Any
    big: Any
    def __init__(self, charmap, big: bool = ...) -> None: ...
    @property
    def charmap(self): ...
    def encode_bytes(self, source): ...
    def decode_bytes(self, source): ...
    def check_repair_unused(self, source): ...
    def repair_unused(self, source): ...
    def encode_transposed_bytes(self, source, offsets): ...
    def decode_transposed_bytes(self, source, offsets): ...
    def decode_int6(self, source): ...
    def decode_int12(self, source): ...
    def decode_int24(self, source): ...
    def decode_int30(self, source): ...
    def decode_int64(self, source): ...
    def encode_int6(self, value): ...
    def encode_int12(self, value): ...
    def encode_int24(self, value): ...
    def encode_int30(self, value): ...
    def encode_int64(self, value): ...

class LazyBase64Engine(Base64Engine):
    def __init__(self, *args, **kwds) -> None: ...
    def __getattribute__(self, attr: str): ...

h64: Any
h64big: Any
bcrypt64: Any