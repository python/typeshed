import sys
from _typeshed import ReadableBuffer
from collections.abc import Callable

from paramiko.kex_group1 import KexGroup1 as KexGroup1

from hashlib import _Hash

class KexGroup16SHA512(KexGroup1):
    name: str
    P: int
    G: int
    hash_algo: Callable[[ReadableBuffer], _Hash]
