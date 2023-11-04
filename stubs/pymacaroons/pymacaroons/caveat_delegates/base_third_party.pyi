from abc import abstractmethod, ABCMeta
from typing import Iterable, Literal

from pymacaroons import Caveat, Macaroon, Verifier

class BaseThirdPartyCaveatDelegate(metaclass=ABCMeta):
    __metaclass__: type
    def __init__(self, *args, **kwargs) -> None: ...
    @abstractmethod
    def add_third_party_caveat(
        self, macaroon: Macaroon, location: str | bytes | None, key: str | bytes | None, key_id: str | bytes | None, **kwargs
    ) -> Macaroon: ...

class BaseThirdPartyCaveatVerifierDelegate(metaclass=ABCMeta):
    __metaclass__: type
    def __init__(self, *args, **kwargs) -> None: ...
    @abstractmethod
    def verify_third_party_caveat(
        self,
        verifier: Verifier,
        caveat: Caveat,
        root: Macaroon,
        macaroon: Macaroon,
        discharge_macaroons: Iterable[Macaroon],
        signature: bytes,
    ) -> Literal[True]: ...
    @abstractmethod
    def update_signature(self, signature: str, caveat: Caveat) -> bytes: ...
