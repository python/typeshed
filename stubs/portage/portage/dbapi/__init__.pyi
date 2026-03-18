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
        mytree: str | None = ...,
        myrepo: str | None = ...,
    ) -> list[str]: ...
    def match(self, mydep: str, use_cache: Literal[0, 1] = ...) -> list[str] | str: ...
