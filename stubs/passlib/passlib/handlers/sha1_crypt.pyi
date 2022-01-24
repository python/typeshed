from typing import Any

import passlib.utils.handlers as uh
from passlib.crypto.digest import compile_hmac as compile_hmac
from passlib.utils import safe_crypt as safe_crypt, test_crypt as test_crypt
from passlib.utils.binary import h64 as h64
from passlib.utils.compat import irange as irange, u as u, unicode as unicode

log: Any

class sha1_crypt(uh.HasManyBackends, uh.HasRounds, uh.HasSalt, uh.GenericHandler):
    name: str
    setting_kwds: Any
    ident: Any
    checksum_size: int
    checksum_chars: Any
    default_salt_size: int
    max_salt_size: int
    salt_chars: Any
    default_rounds: int
    min_rounds: int
    max_rounds: int
    rounds_cost: str
    @classmethod
    def from_string(cls, hash): ...
    def to_string(self, config: bool = ...): ...
    backends: Any
