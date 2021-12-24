from collections.abc import Iterator
from typing import Any

from cryptography.x509 import GeneralName, ObjectIdentifier

class Extension:
    value: Any = ...

class GeneralNames:
    def __iter__(self) -> Iterator[GeneralName]: ...

class DistributionPoint:
    full_name: GeneralNames = ...

class CRLDistributionPoints:
    def __iter__(self) -> Iterator[DistributionPoint]: ...

class AccessDescription:
    access_method: ObjectIdentifier = ...
    access_location: GeneralName = ...

class AuthorityInformationAccess:
    def __iter__(self) -> Iterator[AccessDescription]: ...
