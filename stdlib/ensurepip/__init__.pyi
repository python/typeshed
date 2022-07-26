__all__ = ["version", "bootstrap"]

from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from typing import NamedTuple

_PACKAGE_NAMES: tuple[str, str] = ...
_SETUPTOOLS_VERSION: str = ...
_PIP_VERSION: str = ...
_PROJECTS: list[tuple[str, str, str]] = ...

class _Package(NamedTuple):
    version: str
    wheel_name: str | None
    wheel_path: str | None

_WHEEL_PKG_DIR: str | None = ...

def _find_packages(path: StrOrBytesPath | int) -> dict[str, _Package]: ...
def _get_packages() -> dict[str, _Package]: ...
def _run_pip(args: object, additional_paths: list[StrOrBytesPath] | None = ...) -> int: ...
def _disable_pip_configuration_settings() -> None: ...
def version() -> str: ...
def bootstrap(
    *,
    root: str | None = ...,
    upgrade: bool = ...,
    user: bool = ...,
    altinstall: bool = ...,
    default_pip: bool = ...,
    verbosity: int = ...,
) -> None: ...
def _bootstrap(
    *,
    root: str | None = ...,
    upgrade: bool = ...,
    user: bool = ...,
    altinstall: bool = ...,
    default_pip: bool = ...,
    verbosity: int = ...,
) -> int: ...
def _uninstall_helper(*, verbosity: int = ...) -> int | None: ...
def _main(argv: Sequence[str] | None) -> int: ...
