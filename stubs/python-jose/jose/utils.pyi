from collections.abc import Iterable
from datetime import timedelta
from hashlib import _Hash
from typing import Any, Callable


def long_to_bytes(n: int, blocksize: int | None = ...) -> None: ...
def long_to_base64(data: int, size: int | None = ...) -> bytes: ...
def int_arr_to_long(arr: Iterable[Any]) -> int: ...
def base64_to_long(data: str | bytes) -> int: ...
def calculate_at_hash(access_token: str, hash_alg: Callable[[bytes], _Hash]) -> str: ...
def base64url_decode(input: bytes) -> bytes: ...
def base64url_encode(input: bytes) -> bytes: ...
def timedelta_total_seconds(delta: timedelta) -> int: ...
def ensure_binary(s: str | bytes) -> bytes: ...
