from collections.abc import Mapping, Sequence
from distutils.cmd import Command as Command
from distutils.dist import Distribution as Distribution
from distutils.extension import Extension as Extension
from typing import Any

def setup(
    *,
    name: str = ...,
    version: str = ...,
    description: str = ...,
    long_description: str = ...,
    author: str = ...,
    author_email: str = ...,
    maintainer: str = ...,
    maintainer_email: str = ...,
    url: str = ...,
    download_url: str = ...,
    packages: list[str] = ...,
    py_modules: list[str] = ...,
    scripts: list[str] = ...,
    ext_modules: Sequence[Extension] = ...,
    classifiers: list[str] = ...,
    distclass: type[Distribution] = ...,
    script_name: str = ...,
    script_args: list[str] = ...,
    options: Mapping[str, Any] = ...,
    license: str = ...,
    keywords: list[str] | str = ...,
    platforms: list[str] | str = ...,
    cmdclass: Mapping[str, type[Command]] = ...,
    data_files: list[tuple[str, list[str]]] = ...,
    package_dir: Mapping[str, str] = ...,
    obsoletes: list[str] = ...,
    provides: list[str] = ...,
    requires: list[str] = ...,
    command_packages: list[str] = ...,
    command_options: Mapping[str, Mapping[str, tuple[Any, Any]]] = ...,
    package_data: Mapping[str, list[str]] = ...,
    include_package_data: bool = ...,
    libraries: list[str] = ...,
    headers: list[str] = ...,
    ext_package: str = ...,
    include_dirs: list[str] = ...,
    password: str = ...,
    fullname: str = ...,
    **attrs: Any,
) -> Distribution: ...
def run_setup(script_name: str, script_args: list[str] | None = ..., stop_after: str = ...) -> Distribution: ...
