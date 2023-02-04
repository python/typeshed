# See the README.md file in this directory for more information.

from dataclasses import Field
from typing import Any, ClassVar, Protocol

class DataclassInstance(Protocol):
    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]
