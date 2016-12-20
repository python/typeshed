# Stubs for Crypto.PublicKey.ElGamal (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from Crypto.PublicKey.pubkey import *

class error(Exception): ...

def generate(bits, randfunc, progress_func: Optional[Any] = ...): ...
def construct(tup): ...

class ElGamalobj(pubkey):
    keydata = ...  # type: Any
    def encrypt(self, plaintext, K): ...
    def decrypt(self, ciphertext): ...
    def sign(self, M, K): ...
    def verify(self, M, signature): ...
    def size(self): ...
    def has_private(self): ...
    def publickey(self): ...
