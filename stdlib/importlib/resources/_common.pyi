import sys
from types import ModuleType
from typing_extensions import TypeAlias

Package: TypeAlias = str | ModuleType

if sys.version_info >= (3, 13):
    Anchor: TypeAlias = Package
