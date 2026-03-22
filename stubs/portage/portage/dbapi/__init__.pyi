from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Literal, TypeAlias

_MyListString: TypeAlias = Literal[
    "DEFINED_PHASES",
    "DEPEND",
    "EAPI",
    "HDEPEND",
    "HOMEPAGE",
    "INHERITED",
    "IUSE",
    "KEYWORDS",
    "LICENSE",
    "PDEPEND",
    "PROPERTIES",
    "PROVIDE",
    "RDEPEND",
    "REQUIRED_USE",
    "repository",
    "RESTRICT",
    "SRC_URI",
    "SLOT",
]

class dbapi:
    def aux_get(self, mycpv: str, mylist: Sequence[_MyListString], myrepo: str | None = None) -> list[str]: ...
    def match(self, origdep: str, use_cache: Literal[0, 1] = 1) -> list[str] | str: ...

def __getattr__(name: str) -> Incomplete: ...  # incomplete module
