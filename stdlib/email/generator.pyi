from _typeshed import SupportsWrite
from email.message import Message
from email.policy import Policy
from typing import Any
from typing_extensions import Self

__all__ = ["Generator", "DecodedGenerator", "BytesGenerator"]

class Generator:
    def clone(self, fp: SupportsWrite[str]) -> Self: ...
    def write(self, s: str) -> None: ...
    def __init__(
        self,
        outfp: SupportsWrite[str],
        mangle_from_: bool | None = None,
        maxheaderlen: int | None = None,
        *,
        policy: Policy[Any] | None = None,
    ) -> None: ...
    def flatten(self, msg: Message, unixfrom: bool = False, linesep: str | None = None) -> None: ...

class BytesGenerator(Generator):
    def __init__(
        self,
        outfp: SupportsWrite[bytes],
        mangle_from_: bool | None = None,
        maxheaderlen: int | None = None,
        *,
        policy: Policy[Any] | None = None,
    ) -> None: ...

class DecodedGenerator(Generator):
    def __init__(
        self,
        outfp: SupportsWrite[str],
        mangle_from_: bool | None = None,
        maxheaderlen: int | None = None,
        fmt: str | None = None,
        *,
        policy: Policy[Any] | None = None,
    ) -> None: ...
