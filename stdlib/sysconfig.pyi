import sys
from typing import IO, Any, Literal, overload
from typing_extensions import deprecated

__all__ = [
    "get_config_h_filename",
    "get_config_var",
    "get_config_vars",
    "get_makefile_filename",
    "get_path",
    "get_path_names",
    "get_paths",
    "get_platform",
    "get_python_version",
    "get_scheme_names",
    "parse_config_h",
]

@overload
@deprecated("SO is deprecated, use EXT_SUFFIX")
def get_config_var(name: Literal["SO"]) -> Any: ...
@overload
def get_config_var(name: str) -> Any: ...
@overload
def get_config_vars() -> dict[str, Any]: ...
@overload
def get_config_vars(*args: str) -> list[Any]: ...
def get_scheme_names() -> tuple[str, ...]: ...

if sys.version_info >= (3, 10):
    def get_default_scheme() -> str: ...
    def get_preferred_scheme(key: Literal["prefix", "home", "user"]) -> str: ...

def get_path_names() -> tuple[str, ...]: ...
def get_path(name: str, scheme: str = ..., vars: dict[str, Any] | None = None, expand: bool = True) -> str: ...
def get_paths(scheme: str = ..., vars: dict[str, Any] | None = None, expand: bool = True) -> dict[str, str]: ...
def get_python_version() -> str: ...
def get_platform() -> str: ...

if sys.version_info >= (3, 11):
    def is_python_build(check_home: object = None) -> bool: ...

else:
    def is_python_build(check_home: bool = False) -> bool: ...

def parse_config_h(fp: IO[Any], vars: dict[str, Any] | None = None) -> dict[str, Any]: ...
def get_config_h_filename() -> str: ...
def get_makefile_filename() -> str: ...
