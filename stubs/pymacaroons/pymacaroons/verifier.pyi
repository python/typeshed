from collections.abc import Callable, Iterable
from typing import Any
from typing_extensions import Literal

from pymacaroons import Macaroon
from pymacaroons.caveat_delegates import FirstPartyCaveatVerifierDelegate, ThirdPartyCaveatVerifierDelegate

class Verifier:
    predicates: list[str]
    callbacks: list[Callable[[Any], bool]]
    calculated_signature: bytes | None
    first_party_caveat_verifier_delegate: FirstPartyCaveatVerifierDelegate
    third_party_caveat_verifier_delegate: ThirdPartyCaveatVerifierDelegate
    def __init__(self) -> None: ...
    def satisfy_exact(self, predicate: str | bytes | None) -> None: ...
    def satisfy_general(self, func: Callable[[Any], bool]) -> None: ...
    def verify_exact(self, predicate: str) -> bool: ...
    def verify(
        self, macaroon: Macaroon, key: bytes | bytearray, discharge_macaroons: Iterable[Macaroon] | None = None
    ) -> Literal[True]: ...
    def verify_discharge(
        self, root: Macaroon, discharge: Macaroon, key: bytes | bytearray, discharge_macaroons: Iterable[Macaroon] | None = None
    ) -> Literal[True]: ...
