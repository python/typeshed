from _typeshed import Incomplete
from typing import Literal

class dbapi:
    def aux_get(
        self,
        mycpv: str,
        mylist: list[
            Literal[
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
        ],
        mytree: str | None = None,
        myrepo: str | None = None,
    ) -> list[str]: ...
    def match(self, mydep: str, use_cache: Literal[0, 1] = 1) -> list[str] | str: ...

def __getattr__(name: str) -> Incomplete: ...  # incomplete module
