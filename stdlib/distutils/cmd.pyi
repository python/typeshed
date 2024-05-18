from _typeshed import BytesPath, FileDescriptorOrPath, Incomplete, StrPath, Unused
from abc import abstractmethod
from collections.abc import Callable, Iterable
from distutils.dist import Distribution
from distutils.file_util import _BytesPathT, _StrPathT
from typing import Any, Literal, overload

class Command:
    distribution: Distribution
    sub_commands: list[tuple[str, Callable[[Command], bool] | None]]
    def __init__(self, dist: Distribution) -> None: ...
    @abstractmethod
    def initialize_options(self) -> None: ...
    @abstractmethod
    def finalize_options(self) -> None: ...
    @abstractmethod
    def run(self) -> None: ...
    def announce(self, msg: str, level: int = 1) -> None: ...
    def debug_print(self, msg: str) -> None: ...
    def ensure_string(self, option: str, default: str | None = None) -> None: ...
    def ensure_string_list(self, option: str | list[str]) -> None: ...
    def ensure_filename(self, option: str) -> None: ...
    def ensure_dirname(self, option: str) -> None: ...
    def get_command_name(self) -> str: ...
    def set_undefined_options(self, src_cmd: str, *option_pairs: tuple[str, str]) -> None: ...
    def get_finalized_command(self, command: str, create: bool | Literal[0, 1] = 1) -> Command: ...
    def reinitialize_command(self, command: Command | str, reinit_subcommands: bool | Literal[0, 1] = 0) -> Command: ...
    def run_command(self, command: str) -> None: ...
    def get_sub_commands(self) -> list[str]: ...
    def warn(self, msg: str) -> None: ...
    def execute(self, func: Callable[..., object], args: Iterable[Any], msg: str | None = None, level: int = 1) -> None: ...
    def mkpath(self, name: str, mode: int = 0o777) -> None: ...
    @overload
    def copy_file(
        self,
        infile: StrPath,
        outfile: _StrPathT,
        preserve_mode: bool | Literal[0, 1] = 1,
        preserve_times: bool | Literal[0, 1] = 1,
        link: str | None = None,
        level: Unused = 1,
    ) -> tuple[_StrPathT | str, bool]: ...
    @overload
    def copy_file(
        self,
        infile: BytesPath,
        outfile: _BytesPathT,
        preserve_mode: bool | Literal[0, 1] = 1,
        preserve_times: bool | Literal[0, 1] = 1,
        link: str | None = None,
        level: Unused = 1,
    ) -> tuple[_BytesPathT | bytes, bool]: ...
    def copy_tree(
        self,
        infile: StrPath,
        outfile: str,
        preserve_mode: bool | Literal[0, 1] = 1,
        preserve_times: bool | Literal[0, 1] = 1,
        preserve_symlinks: bool | Literal[0, 1] = 0,
        level: Unused = 1,
    ) -> list[str]: ...
    @overload
    def move_file(src: StrPath, dst: _StrPathT, level: Unused = 1) -> _StrPathT | str: ...
    @overload
    def move_file(src: BytesPath, dst: _BytesPathT, level: Unused = 1) -> _BytesPathT | bytes: ...
    def spawn(self, cmd: Iterable[str], search_path: bool | Literal[0, 1] = 1, level: Unused = 1) -> None: ...
    @overload
    def make_archive(
        self,
        base_name: str,
        format: str,
        root_dir: FileDescriptorOrPath | None = None,
        base_dir: str | None = None,
        owner: str | None = None,
        group: str | None = None,
    ) -> str: ...
    @overload
    def make_archive(
        self,
        base_name: StrPath,
        format: str,
        root_dir: FileDescriptorOrPath,
        base_dir: str | None = None,
        owner: str | None = None,
        group: str | None = None,
    ) -> str: ...
    def make_file(
        self,
        infiles: str | list[str] | tuple[str, ...],
        outfile: FileDescriptorOrPath,
        func: Callable[..., object],
        args: list[Any],
        exec_msg: str | None = None,
        skip_msg: str | None = None,
        level: Unused = 1,
    ) -> None: ...
    def ensure_finalized(self) -> None: ...
    def dump_options(self, header: Incomplete | None = None, indent: str = "") -> None: ...
