from collections.abc import Mapping
from typing import Any, TypedDict, type_check_only

from .dbapi.porttree import portagetree
from .package.ebuild.config import config

@type_check_only
class _DBRootDict(TypedDict):
    bintree: Any
    porttree: portagetree
    virtuals: Any

db: Mapping[str, _DBRootDict]
root: str
settings: config
