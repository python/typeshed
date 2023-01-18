from _typeshed import SupportsWrite
from email.message import Message
from email.policy import Policy

__all__ = ["Generator", "DecodedGenerator", "BytesGenerator"]

class Generator:
    def clone(self, fp: SupportsWrite[str]) -> Generator: ...
    def write(self, s: str) -> None: ...
    def __init__(
        self,
        outfp: SupportsWrite[str],
        mangle_from_: bool | None = None,
        maxheaderlen: int | None = None,
        *,
        policy: Policy | None = None,
    ) -> None: ...
    def flatten(self, msg: Message, unixfrom: bool = False, linesep: str | None = None) -> None: ...

class BytesGenerator:
    def clone(self, fp: SupportsWrite[bytes]) -> BytesGenerator: ...
    def write(self, s: str) -> None: ...
    def __init__(
        self,
        outfp: SupportsWrite[bytes],
        mangle_from_: bool | None = None,
        maxheaderlen: int | None = None,
        *,
        policy: Policy | None = None,
    ) -> None: ...
    def flatten(self, msg: Message, unixfrom: bool = False, linesep: str | None = None) -> None: ...

class DecodedGenerator(Generator):
    def __init__(
        self,
        outfp: SupportsWrite[str],
        mangle_from_: bool | None = None,
        maxheaderlen: int | None = None,
        fmt: str | None = None,
        *,
        policy: Policy | None = None,
    ) -> None: ...
