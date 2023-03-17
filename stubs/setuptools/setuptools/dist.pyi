from collections.abc import Generator, Iterable, Mapping
from typing import Any

from setuptools import Command, SetuptoolsDeprecationWarning

from ._distutils.dist import Distribution as _Distribution

class Distribution(_Distribution):
    def patch_missing_pkg_info(self, attrs: Mapping[str, Any]) -> None: ...
    src_root: str | None
    dependency_links: list[str]
    setup_requires: list[str]
    def __init__(self, attrs: dict[str, Any] | None = ...) -> None: ...
    def warn_dash_deprecation(self, opt: str, section: str) -> str: ...
    def make_option_lowercase(self, opt: str, section: str) -> str: ...
    def parse_config_files(self, filenames: Iterable[str] | None = ..., ignore_option_errors: bool = ...) -> None: ...
    def fetch_build_eggs(self, requires: str | Iterable[str]): ...
    def get_egg_cache_dir(self) -> str: ...
    def fetch_build_egg(self, req): ...
    def get_command_class(self, command: str) -> type[Command]: ...
    def include(self, **attrs) -> None: ...
    def exclude_package(self, package: str) -> None: ...
    def has_contents_for(self, package: str) -> bool | None: ...
    def exclude(self, **attrs) -> None: ...
    def get_cmdline_options(self) -> dict[str, dict[str, str | None]]: ...
    def iter_distribution_names(self) -> Generator[str, None, None]: ...
    def handle_display_options(self, option_order): ...

class DistDeprecationWarning(SetuptoolsDeprecationWarning): ...
