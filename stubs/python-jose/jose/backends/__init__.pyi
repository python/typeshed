from collections.abc import Callable

from .base import DIRKey as DIRKey

AESKey = Any
HMACKey = Any
RSAKey = Any
ECKey = Any
get_random_bytes: Callable[[int], bytes]
