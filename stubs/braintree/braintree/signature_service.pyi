from _typeshed import Incomplete

from braintree.util.crypto import Crypto as Crypto

class SignatureService:
    private_key: Incomplete
    hmac_hash: Incomplete
    def __init__(self, private_key, hashfunc=...) -> None: ...
    def sign(self, data): ...
    def hash(self, data): ...
