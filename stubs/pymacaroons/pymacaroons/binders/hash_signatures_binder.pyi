from _typeshed import Incomplete, ReadableBuffer

from pymacaroons.binders.base_binder import BaseBinder

class HashSignaturesBinder(BaseBinder):
    key: bytes | bytearray
    def __init__(self, root: Incomplete, key: bytes | bytearray | None = None) -> None: ...
    def bind_signature(self, signature: str | ReadableBuffer) -> bytes: ...
