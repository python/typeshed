from typing import Any

from . import jwk as jwk
from .backends import get_random_bytes as get_random_bytes
from .constants import ALGORITHMS as ALGORITHMS, ZIPS as ZIPS
from .exceptions import JWEError as JWEError, JWEParseError as JWEParseError
from .utils import base64url_decode as base64url_decode, base64url_encode as base64url_encode, ensure_binary as ensure_binary

def encrypt(
    plaintext: Any,
    key: dict[str, str],
    encryption=...,
    algorithm=...,
    zip: Any | None = ...,
    cty: Any | None = ...,
    kid: Any | None = ...,
): ...
def decrypt(jwe_str: str, key: str | dict[str, str]): ...
def get_unverified_header(jwe_str: str): ...
