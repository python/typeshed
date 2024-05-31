from collections.abc import Callable
from typing_extensions import TypeAlias

_Algorithm: TypeAlias = Callable[[int], bytearray | list[int]]

def method(algorithm: _Algorithm, alphabet: str, size: int) -> str: ...
