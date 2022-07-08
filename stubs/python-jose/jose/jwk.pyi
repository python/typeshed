from typing import Any

from .backends.base import Key as Key

def get_key(algorithm: str) -> type[Key] | None: ...
def register_key(algorithm: str, key_class: type[Key]) -> bool: ...
def construct(
    # explicitly checks for key_data as dict instance, instead of a Mapping
    key_data: str | bytes | dict[str, Any] | Key,
    algorithm: str | None = ...,
) -> Key: ...
