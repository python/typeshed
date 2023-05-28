# https://pyinstaller.org/en/stable/hooks.html

from _typeshed import StrOrBytesPath, StrPath
from collections.abc import Callable, Iterable
from typing import Any
from typing_extensions import Final, Literal

import pkg_resources
from PyInstaller import HOMEPATH as HOMEPATH
from PyInstaller.depend.imphookapi import PostGraphAPI
from PyInstaller.utils.hooks import conda
from PyInstaller.utils.hooks.win32 import get_pywin32_module_file_attribute as get_pywin32_module_file_attribute

conda_support = conda

PY_IGNORE_EXTENSIONS: Final[set[str]]
hook_variables: dict[str, str]

def exec_statement(statement: str) -> str | int: ...
def exec_statement_rc(statement: str) -> str | int: ...
def eval_statement(statement: str) -> Any | Literal[""]: ...
def get_pyextension_imports(module_name: str) -> list[str]: ...
def get_homebrew_path(formula: str = "") -> str | None: ...
def remove_prefix(string: str, prefix: str) -> str: ...
def remove_suffix(string: str, suffix: str) -> str: ...
def remove_file_extension(filename: str) -> str: ...
def can_import_module(module_name: str) -> bool: ...
def get_module_attribute(module_name: str, attr_name: str) -> Any: ...
def get_module_file_attribute(package: str) -> str | None: ...
def is_module_satisfies(
    requirements: Iterable[str] | pkg_resources.Requirement,
    version: str | pkg_resources.Distribution | None = None,
    version_attr: str = "__version__",
) -> bool: ...
def is_package(module_name: str) -> bool: ...
def get_all_package_paths(package: str) -> list[str]: ...
def package_base_path(package_path: str, package: str) -> str: ...
def get_package_paths(package: str) -> tuple[str, str]: ...
def collect_submodules(
    package: str, filter: Callable[[str], bool] = ..., on_error: Literal["ignore", "warn once", "warn", "raise"] = "warn once"
) -> list[str]: ...
def is_module_or_submodule(name: str, mod_or_submod: str) -> bool: ...

PY_DYLIB_PATTERNS: Final[list[str]]

def collect_dynamic_libs(
    package: str, destdir: object = None, search_patterns: Iterable[str] = ["*.dll", "*.dylib", "lib*.so"]
) -> list[tuple[str, str]]: ...
def collect_data_files(
    package: str,
    include_py_files: bool = False,
    subdir: StrPath | None = None,
    excludes: Iterable[str] | None = None,
    includes: Iterable[str] | None = None,
) -> list[tuple[str, str]]: ...
def collect_system_data_files(
    path: str, destdir: StrPath | None = None, include_py_files: bool = False
) -> list[tuple[str, str]]: ...
def copy_metadata(package_name: str, recursive: bool = False) -> list[tuple[str, str]]: ...
def get_installer(module: str) -> str | None: ...
def requirements_for_package(package_name: str) -> list[str]: ...
def collect_all(
    package_name: str,
    include_py_files: bool = True,
    filter_submodules: Callable[[str], bool] | None = None,
    exclude_datas: Iterable[str] | None = None,
    include_datas: Iterable[str] | None = None,
    on_error: Literal["ignore", "warn once", "warn", "raise"] = "warn once",
) -> tuple[list[tuple[str, str]], list[tuple[str, str]], list[str]]: ...
def collect_entry_point(name: str) -> tuple[tuple[str, str], list[str]]: ...
def get_hook_config(hook_api: PostGraphAPI, module_name: str, key: str) -> None: ...
def include_or_exclude_file(
    filename: StrOrBytesPath,
    include_list: Iterable[StrOrBytesPath] | None = None,
    exclude_list: Iterable[StrOrBytesPath] | None = None,
) -> bool: ...
def collect_delvewheel_libs_directory(
    package_name: str,
    libdir_name: StrPath | None = None,
    datas: list[tuple[str, str]] | None = None,
    binaries: list[tuple[str, str]] | None = None,
) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]: ...
