import sys
from importlib.resources import Package
from typing_extensions import TypeAlias

if sys.version_info >= (3, 13):
    Anchor: TypeAlias = Package
