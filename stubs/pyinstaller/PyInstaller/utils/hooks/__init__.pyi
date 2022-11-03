# https://pyinstaller.org/en/stable/hooks.html

from _typeshed import StrOrBytesPath, StrPath, SupportsKeysAndGetItem
from collections.abc import Callable, Iterable, Mapping
from typing import Any
from typing_extensions import Literal, TypeAlias

import pkg_resources
from PyInstaller import HOMEPATH as HOMEPATH
from PyInstaller.depend.imphookapi import PostGraphAPI
from PyInstaller.utils.hooks.win32 import get_pywin32_module_file_attribute as get_pywin32_module_file_attribute

_Environ: TypeAlias = SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]] | Mapping[str, str]

PY_IGNORE_EXTENSIONS: set[str]
hook_variables: dict[str, str]

def exec_statement(statement: str) -> str | int: ...
def exec_statement_rc(statement: str) -> str | int: ...
def exec_script(script_filename: StrOrBytesPath, *args: str, env: _Environ | None = ...) -> str | int: ...
def exec_script_rc(script_filename: StrOrBytesPath, *args: str, env: _Environ | None = ...) -> str | int: ...
def eval_statement(statement: str) -> Any | Literal[""]: ...
def eval_script(script_filename: StrOrBytesPath, *args: str, env: _Environ | None = ...) -> Any | Literal[""]: ...
def get_pyextension_imports(module_name: str) -> list[str]: ...
def get_homebrew_path(formula: str = ...) -> str | None: ...
def remove_prefix(string: str, prefix: str) -> str: ...
def remove_suffix(string: str, suffix: str) -> str: ...
def remove_file_extension(filename: str) -> str: ...
def can_import_module(module_name: str) -> bool: ...
def get_module_attribute(module_name: str, attr_name: str) -> Any: ...
def get_module_file_attribute(package: str) -> str | None: ...
def is_module_satisfies(
    requirements: Iterable[str] | pkg_resources.Requirement,
    version: str | pkg_resources.Distribution | None = ...,
    version_attr: str = ...,
) -> bool: ...
def is_package(module_name: str) -> bool: ...
def get_all_package_paths(package: str) -> list[str]: ...
def package_base_path(package_path: str, package: str) -> str: ...
def get_package_paths(package: str) -> tuple[str, str]: ...
def collect_submodules(
    package: str, filter: Callable[[str], bool] = ..., on_error: Literal["ignore", "warn once", "warn", "raise"] = ...
) -> list[str]: ...
def is_module_or_submodule(name: str, mod_or_submod: str) -> bool: ...

PY_DYLIB_PATTERNS: list[str]

def collect_dynamic_libs(package: str, destdir: object = ...) -> list[tuple[str, str]]: ...
def collect_data_files(
    package: str,
    include_py_files: bool = ...,
    subdir: StrPath | None = ...,
    excludes: Iterable[str] | None = ...,
    includes: Iterable[str] | None = ...,
) -> list[tuple[str, str]]: ...
def collect_system_data_files(
    path: str, destdir: StrPath | None = ..., include_py_files: bool = ...
) -> list[tuple[str, str]]: ...
def copy_metadata(package_name: str, recursive: bool = ...) -> list[tuple[str, str]]: ...
def get_installer(module: str) -> str | None: ...
def requirements_for_package(package_name: str) -> list[str]: ...
def collect_all(
    package_name: str,
    include_py_files: bool = ...,
    filter_submodules: Callable[[str], bool] | None = ...,
    exclude_datas: Iterable[str] | None = ...,
    include_datas: Iterable[str] | None = ...,
    on_error: Literal["ignore", "warn once", "warn", "raise"] = ...,
) -> tuple[list[tuple[str, str]], list[tuple[str, str]], list[str]]: ...
def collect_entry_point(name: str) -> tuple[tuple[str, str], list[str]]: ...
def get_hook_config(hook_api: PostGraphAPI, module_name: str, key: str) -> None: ...
def include_or_exclude_file(
    filename: StrOrBytesPath,
    include_list: Iterable[StrOrBytesPath] | None = ...,
    exclude_list: Iterable[StrOrBytesPath] | None = ...,
) -> bool: ...
def collect_delvewheel_libs_directory(
    package_name: str,
    libdir_name: StrPath | None = ...,
    datas: list[tuple[str, str]] | None = ...,
    binaries: list[tuple[str, str]] | None = ...,
) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]: ...
