from typing import Any

from . import jwk as jwk
from .backends.base import Key as Key
from .constants import ALGORITHMS as ALGORITHMS
from .exceptions import JWSError as JWSError, JWSSignatureError as JWSSignatureError
from .utils import base64url_decode as base64url_decode, base64url_encode as base64url_encode

def sign(payload, key, headers: Any | None = ..., algorithm=...): ...
def verify(token, key, algorithms, verify: bool = ...): ...
def get_unverified_header(token): ...
def get_unverified_headers(token): ...
def get_unverified_claims(token): ...
