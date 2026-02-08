from typing import Any, Literal

from portage.dbapi.porttree import portdbapi

from .config import config

def doebuild(
    myebuild: str,
    mydo: Literal[
        "clean",
        "cleanrm",
        "compile",
        "config",
        "configure",
        "depend",
        "digest",
        "fetch",
        "fetchall",
        "help",
        "info",
        "install",
        "instprep",
        "manifest",
        "merge",
        "nofetch",
        "package",
        "postinst",
        "postrm",
        "preinst",
        "prepare",
        "prerm",
        "pretend",
        "qmerge",
        "rpm",
        "setup",
        "test",
        "unmerge",
        "unpack",
    ],
    settings: config | None = ...,
    debug: Literal[0, 1] = ...,
    listonly: Literal[0, 1] = ...,
    fetchonly: Literal[0, 1] = ...,
    cleanup: Literal[0, 1] = ...,
    use_cache: Literal[0, 1] = ...,
    fetchall: Literal[0, 1] = ...,
    tree: Literal["vartree", "porttree", "bintree"] = ...,
    mydbapi: portdbapi | None = ...,
    vartree: Any = ...,
    prev_mtimes: dict[str, Any] | None = ...,
    fd_pipes: dict[str, str] | None = ...,
    returnproc: int | bool = ...,
) -> Literal[0, 1] | bool | list[int]:  # Missing portage.process.MultiprocessingProcess
    ...
