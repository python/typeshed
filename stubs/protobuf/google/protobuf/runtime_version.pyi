from enum import Enum
from typing import Final, Literal

class Domain(Enum):
    GOOGLE_INTERNAL = 1
    PUBLIC = 2

OSS_DOMAIN: Final[Literal[Domain.PUBLIC]]
OSS_MAJOR: Final = 5
OSS_MINOR: Final = 28
OSS_PATCH: Final = 3
OSS_SUFFIX: Final = ""
DOMAIN: Final[Literal[Domain.PUBLIC]]
MAJOR: Final = OSS_MAJOR
MINOR: Final = OSS_MINOR
PATCH: Final = OSS_PATCH
SUFFIX: Final = OSS_SUFFIX

class VersionError(Exception): ...

def ValidateProtobufRuntimeVersion(
    gen_domain: Domain, gen_major: int, gen_minor: int, gen_patch: int, gen_suffix: str, location: str
) -> None: ...
