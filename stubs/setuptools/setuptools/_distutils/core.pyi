from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Iterable, Mapping
from typing import Final, TypedDict, type_check_only
from typing_extensions import Unpack

from .cmd import Command as Command
from .dist import Distribution as Distribution
from .extension import Extension as Extension

@type_check_only
class _SetupArgs(TypedDict, total=False):  # total=False for custom Distributions that could accept more arguments
    name: str
    version: str
    description: str
    long_description: str
    author: str
    author_email: str
    maintainer: str
    maintainer_email: str
    url: str
    download_url: str
    packages: list[str]
    py_modules: list[str]
    scripts: list[str]
    ext_modules: list[Extension]
    classifiers: list[str]
    distclass: type[Distribution]
    script_name: str
    script_args: list[str]
    options: Mapping[str, Incomplete]
    license: str
    keywords: list[str] | str
    platforms: list[str] | str
    cmdclass: Mapping[str, type[Command]]
    data_files: list[tuple[str, list[str]]]
    package_dir: Mapping[str, str]
    obsoletes: list[str]
    provides: list[str]
    requires: list[str]
    command_packages: list[str]
    command_options: Mapping[str, Mapping[str, tuple[Incomplete, Incomplete]]]
    package_data: Mapping[str, list[str]]
    include_package_data: bool
    libraries: list[str]
    headers: list[str]
    ext_package: str
    include_dirs: list[str]
    password: str
    fullname: str

USAGE: Final[str]

def gen_usage(script_name: StrOrBytesPath) -> str: ...

setup_keywords: tuple[str, ...]
extension_keywords: tuple[str, ...]

def setup(**attrs: Unpack[_SetupArgs]) -> Distribution: ...
def run_setup(script_name: str, script_args: Iterable[str] | None = None, stop_after: str = "run") -> Distribution: ...
