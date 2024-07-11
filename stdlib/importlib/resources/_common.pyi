import sys
from types import ModuleType
from typing import TypeAlias

Package: TypeAlias = str | ModuleType

if sys.version_info >= (3, 13):
    Anchor: TypeAlias = Package
