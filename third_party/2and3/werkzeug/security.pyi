from typing import Any, Optional

SALT_CHARS = ...  # type: Any
DEFAULT_PBKDF2_ITERATIONS = ...  # type: Any

def pbkdf2_hex(data, salt, iterations=..., keylen: Optional[Any] = ..., hashfunc: Optional[Any] = ...): ...
def pbkdf2_bin(data, salt, iterations=..., keylen: Optional[Any] = ..., hashfunc: Optional[Any] = ...): ...
def safe_str_cmp(a, b): ...
def gen_salt(length): ...
def generate_password_hash(password, method: str = ..., salt_length: int = ...): ...
def check_password_hash(pwhash, password): ...
def safe_join(directory, filename): ...
