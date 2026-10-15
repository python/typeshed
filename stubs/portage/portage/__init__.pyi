from _typeshed import Incomplete
from collections.abc import Mapping
from typing import TypedDict, type_check_only

from .dbapi.porttree import portagetree
from .package.ebuild.config import config
from .package.ebuild.doebuild import doebuild

__all__ = ["config", "db", "doebuild", "root", "settings"]

@type_check_only
class _DBRootDict(TypedDict):
    bintree: Incomplete
    porttree: portagetree
    vartree: Incomplete
    virtuals: dict[str, Incomplete]

db: Mapping[str, _DBRootDict]
root: str
settings: config

def __getattr__(name: str) -> Incomplete: ...  # incomplete module
