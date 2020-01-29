from typing import Any

from . import rest_framework as rest_framework
from .filters import *
from .filterset import FilterSet as FilterSet

def parse_version(version: Any): ...

VERSION: Any
