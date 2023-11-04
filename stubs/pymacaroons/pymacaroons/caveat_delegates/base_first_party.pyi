from abc import ABCMeta, abstractmethod
from typing import Any

from pymacaroons import Caveat, Macaroon, Verifier

class BaseFirstPartyCaveatDelegate(metaclass=ABCMeta):
    __metaclass__: type
    def __init__(self, *args, **kwargs) -> None: ...
    @abstractmethod
    def add_first_party_caveat(self, macaroon: Macaroon, predicate: str | bytes, **kwargs) -> Macaroon: ...

class BaseFirstPartyCaveatVerifierDelegate(metaclass=ABCMeta):
    __metaclass__: type
    def __init__(self, *args, **kwargs) -> None: ...
    @abstractmethod
    def verify_first_party_caveat(self, verifier: Verifier, caveat: Caveat, signature: Any) -> int: ...
    @abstractmethod
    def update_signature(self, signature: bytes | bytearray, caveat: Caveat) -> bytes: ...
