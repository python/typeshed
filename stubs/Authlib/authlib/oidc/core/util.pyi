from _typeshed import FloatInt, ReadableBuffer
from collections.abc import Iterable
from typing import SupportsBytes, SupportsIndex

def create_half_hash(
    s: str | bytes | FloatInt | Iterable[SupportsIndex] | SupportsIndex | SupportsBytes | ReadableBuffer, alg: str
) -> bytes | None: ...
