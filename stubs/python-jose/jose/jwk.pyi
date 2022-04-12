from typing import Any

from .backends import AESKey as AESKey, DIRKey as DIRKey, ECKey as ECKey, HMACKey as HMACKey, RSAKey as RSAKey
from .backends.base import Key as Key
from .constants import ALGORITHMS as ALGORITHMS
from .exceptions import JWKError as JWKError

def get_key(algorithm): ...
def register_key(algorithm, key_class: Key): ...
def construct(key_data, algorithm: Any | None = ...): ...
