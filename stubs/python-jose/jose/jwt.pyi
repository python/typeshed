from typing import Any

from . import jws as jws
from .constants import ALGORITHMS as ALGORITHMS
from .exceptions import (
    ExpiredSignatureError as ExpiredSignatureError,
    JWSError as JWSError,
    JWTClaimsError as JWTClaimsError,
    JWTError as JWTError,
)
from .utils import calculate_at_hash as calculate_at_hash, timedelta_total_seconds as timedelta_total_seconds

def encode(claims, key, algorithm=..., headers: Any | None = ..., access_token: Any | None = ...): ...
def decode(
    token,
    key,
    algorithms: Any | None = ...,
    options: Any | None = ...,
    audience: Any | None = ...,
    issuer: Any | None = ...,
    subject: Any | None = ...,
    access_token: Any | None = ...,
): ...
def get_unverified_header(token): ...
def get_unverified_headers(token): ...
def get_unverified_claims(token): ...
