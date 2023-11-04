from collections.abc import Iterable
from typing import Literal

from pymacaroons import Caveat, Macaroon, Verifier

from .base_third_party import BaseThirdPartyCaveatDelegate, BaseThirdPartyCaveatVerifierDelegate

class ThirdPartyCaveatDelegate(BaseThirdPartyCaveatDelegate):
    def __init__(self, *args, **kwargs) -> None: ...
    def add_third_party_caveat(
        self, macaroon: Macaroon, location: str | bytes | None, key: str | bytes | None, key_id: str | bytes | None, **kwargs
    ) -> Macaroon: ...

class ThirdPartyCaveatVerifierDelegate(BaseThirdPartyCaveatVerifierDelegate):
    def __init__(self, *args, **kwargs) -> None: ...
    def verify_third_party_caveat(
        self,
        verifier: Verifier,
        caveat: Caveat,
        root: Macaroon,
        macaroon: Macaroon,
        discharge_macaroons: Iterable[Macaroon],
        signature: bytes,
    ) -> Literal[True]: ...
    def update_signature(self, signature: str, caveat: Caveat) -> bytes: ...
