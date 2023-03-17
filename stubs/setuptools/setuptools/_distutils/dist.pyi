from _typeshed import FileDescriptorOrPath, Incomplete, SupportsWrite
from collections.abc import Iterable, Mapping
from re import Pattern
from typing import IO, Any, ClassVar

from .cmd import Command

command_re: Pattern[str]

_OptionsList = list[tuple[str, str | None, str, int] | tuple[str, str | None, str]]

class DistributionMetadata:
    def __init__(self, path: FileDescriptorOrPath | None = None) -> None: ...
    name: str | None
    version: str | None
    author: str | None
    author_email: str | None
    maintainer: str | None
    maintainer_email: str | None
    url: str | None
    license: str | None
    description: str | None
    long_description: str | None
    keywords: str | list[str] | None
    platforms: str | list[str] | None
    classifiers: str | list[str] | None
    download_url: str | None
    provides: list[str] | None
    requires: list[str] | None
    obsoletes: list[str] | None
    def read_pkg_file(self, file: IO[str]) -> None: ...
    def write_pkg_info(self, base_dir: str) -> None: ...
    def write_pkg_file(self, file: SupportsWrite[str]) -> None: ...
    def get_name(self) -> str: ...
    def get_version(self) -> str: ...
    def get_fullname(self) -> str: ...
    def get_author(self) -> str: ...
    def get_author_email(self) -> str: ...
    def get_maintainer(self) -> str: ...
    def get_maintainer_email(self) -> str: ...
    def get_contact(self) -> str: ...
    def get_contact_email(self) -> str: ...
    def get_url(self) -> str: ...
    def get_license(self) -> str: ...
    def get_licence(self) -> str: ...
    def get_description(self) -> str: ...
    def get_long_description(self) -> str: ...
    def get_keywords(self) -> str | list[str]: ...
    def get_platforms(self) -> str | list[str]: ...
    def get_classifiers(self) -> str | list[str]: ...
    def get_download_url(self) -> str: ...
    def get_requires(self) -> list[str]: ...
    def set_requires(self, value: Iterable[str]) -> None: ...
    def get_provides(self) -> list[str]: ...
    def set_provides(self, value: Iterable[str]) -> None: ...
    def get_obsoletes(self) -> list[str]: ...
    def set_obsoletes(self, value: Iterable[str]) -> None: ...

class Distribution:
    cmdclass: dict[str, type[Command]]
    metadata: DistributionMetadata
    def __init__(self, attrs: Mapping[str, Any] | None = None) -> None: ...
    def get_option_dict(self, command: str) -> dict[str, tuple[str, str]]: ...
    def parse_config_files(self, filenames: Iterable[str] | None = None) -> None: ...
    def get_command_obj(self, command: str, create: bool = True) -> Command | None: ...
    global_options: ClassVar[_OptionsList]
    common_usage: ClassVar[str]
    display_options: ClassVar[_OptionsList]
    display_option_names: ClassVar[list[str]]
    negative_opt: ClassVar[dict[str, str]]
    verbose: int
    dry_run: int
    help: int
    command_packages: list[str] | None
    script_name: str | None
    script_args: list[str] | None
    command_options: dict[str, dict[str, tuple[str, str]]]
    dist_files: list[tuple[str, str, str]]
    packages: Incomplete
    package_data: dict[str, list[str]]
    package_dir: Incomplete
    py_modules: Incomplete
    libraries: Incomplete
    headers: Incomplete
    ext_modules: Incomplete
    ext_package: Incomplete
    include_dirs: Incomplete
    extra_path: Incomplete
    scripts: Incomplete
    data_files: Incomplete
    password: str
    command_obj: Incomplete
    have_run: Incomplete
    want_user_cfg: bool
    def dump_option_dicts(
        self, header: Incomplete | None = None, commands: Incomplete | None = None, indent: str = ""
    ) -> None: ...
    def find_config_files(self): ...
    commands: Incomplete
    def parse_command_line(self): ...
    def finalize_options(self) -> None: ...
    def handle_display_options(self, option_order): ...
    def print_command_list(self, commands, header, max_length) -> None: ...
    def print_commands(self) -> None: ...
    def get_command_list(self): ...
    def get_command_packages(self): ...
    def get_command_class(self, command: str | Command) -> type[Command]: ...
    def reinitialize_command(self, command: str | Command, reinit_subcommands: int = 0) -> Command: ...
    def announce(self, msg, level: int = ...) -> None: ...
    def run_commands(self) -> None: ...
    def run_command(self, command: str | Command) -> None: ...
    def has_pure_modules(self) -> bool: ...
    def has_ext_modules(self) -> bool: ...
    def has_c_libraries(self) -> bool: ...
    def has_modules(self) -> bool: ...
    def has_headers(self) -> bool: ...
    def has_scripts(self) -> bool: ...
    def has_data_files(self) -> bool: ...
    def is_pure(self) -> bool: ...

    # Getter methods generated in __init__
    def get_name(self) -> str: ...
    def get_version(self) -> str: ...
    def get_fullname(self) -> str: ...
    def get_author(self) -> str: ...
    def get_author_email(self) -> str: ...
    def get_maintainer(self) -> str: ...
    def get_maintainer_email(self) -> str: ...
    def get_contact(self) -> str: ...
    def get_contact_email(self) -> str: ...
    def get_url(self) -> str: ...
    def get_license(self) -> str: ...
    def get_licence(self) -> str: ...
    def get_description(self) -> str: ...
    def get_long_description(self) -> str: ...
    def get_keywords(self) -> str | list[str]: ...
    def get_platforms(self) -> str | list[str]: ...
    def get_classifiers(self) -> str | list[str]: ...
    def get_download_url(self) -> str: ...
    def get_requires(self) -> list[str]: ...
    def get_provides(self) -> list[str]: ...
    def get_obsoletes(self) -> list[str]: ...
