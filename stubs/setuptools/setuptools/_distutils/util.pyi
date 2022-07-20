from _typeshed import StrPath
from collections.abc import Callable, Container, Iterable, Mapping
from typing import Any
from typing_extensions import Literal

def get_host_platform() -> str: ...
def get_platform() -> str: ...
def get_macosx_target_ver_from_syscfg(): ...
def get_macosx_target_ver(): ...
def split_version(s: str) -> list[int]: ...
def convert_path(pathname: str) -> str: ...
def change_root(new_root: str, pathname: str) -> str: ...
def check_environ() -> None: ...
def subst_vars(s: str, local_vars: Mapping[str, str]) -> None: ...
def grok_environment_error(exc: object, prefix: str = ...) -> str: ...
def split_quoted(s: str) -> list[str]: ...
def execute(
    func: Callable[..., object], args: tuple[Any, ...], msg: str | None = ..., verbose: bool = ..., dry_run: bool = ...
) -> None: ...
def strtobool(val: str) -> Literal[0, 1]: ...
def byte_compile(
    py_files: list[str],
    optimize: int = ...,
    force: bool = ...,
    prefix: str | None = ...,
    base_dir: str | None = ...,
    verbose: bool = ...,
    dry_run: bool = ...,
    direct: bool | None = ...,
) -> None: ...
def rfc822_escape(header: str) -> str: ...
