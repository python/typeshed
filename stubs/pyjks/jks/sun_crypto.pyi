SUN_JKS_ALGO_ID: tuple[int, ...]
SUN_JCE_ALGO_ID: tuple[int, ...]

def jks_pkey_encrypt(key: bytes | bytearray, password_str: str) -> bytes: ...
def jks_pkey_decrypt(data: bytes | bytearray, password_str: str) -> bytes: ...
def jce_pbe_decrypt(data: bytes | bytearray, password: str, salt: bytes, iteration_count: int) -> bytes: ...
