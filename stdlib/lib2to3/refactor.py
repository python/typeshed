from collections.abc import Container, Generator, Iterable, Mapping
from logging import Logger
from typing import Any, ClassVar, NoReturn

_Driver = Any  # really lib2to3.driver.Driver
_BottomMatcher = Any  # really lib2to3.btm_matcher.BottomMatcher


def get_all_fix_names(fixer_pkg: str, remove_prefix: bool = ...) -> list[str]:
    ...


def get_fixers_from_package(pkg_name: str) -> list[str]:
    ...


class FixerError(Exception):
    ...


class RefactoringTool:
    CLASS_PREFIX: ClassVar[str]
    FILE_PREFIX: ClassVar[str]
    fixers: Iterable[str]
    explicit: Container[str]
    options: dict[str, Any]
    grammar: Any
    write_unchanged_files: bool
    errors: list[Any]
    logger: Logger
    fixer_log: list[Any]
    wrote: bool
    driver: _Driver
    pre_order: Any
    post_order: Any
    files: list[Any]
    BM: _BottomMatcher
    bmi_pre_order: list[Any]
    bmi_post_order: list[Any]

    def __init__(
        self, fixer_names: Iterable[str], options: Mapping[str, Any] | None = ..., explicit: Container[str] | None = ...
    ) -> None:
        ...

    def get_fixers(self) -> tuple[list[Any], list[Any]]:
        ...

    def log_error(self, msg: str, *args: Any, **kwds: Any) -> NoReturn:
        ...

    def log_message(self, msg: str, *args: Any) -> None:
        ...

    def log_debug(self, msg: str, *args: Any) -> None:
        ...

    def print_output(self, old_text: str, new_text: str, filename: str, equal):
        ...

    def refactor(self, items: Iterable[str], write: bool = ..., doctests_only: bool = ...) -> None:
        ...

    def refactor_dir(self, dir_name: str, write: bool = ..., doctests_only: bool = ...) -> None:
        ...

    def refactor_file(self, filename: str, write: bool = ..., doctests_only: bool = ...) -> None:
        ...

    def refactor_string(self, data: str, name: str):
        ...

    def refactor_stdin(self, doctests_only: bool = ...) -> None:
        ...

    def refactor_tree(self, tree, name: str) -> bool:
        ...

    def traverse_by(self, fixers, traversal) -> None:
        ...

    def processed_file(
        self, new_text: str, filename: str, old_text: str | None = ..., write: bool = ..., encoding: str | None = ...
    ) -> None:
        ...

    def write_file(self, new_text: str, filename: str, old_text: str, encoding: str | None = ...) -> None:
        ...

    PS1: ClassVar[str]
    PS2: ClassVar[str]

    def refactor_docstring(self, input: str, filename: str) -> str:
        ...

    def refactor_doctest(self, block: list[str], lineno: int, indent: int, filename: str) -> list[str]:
        ...

    def summarize(self) -> None:
        ...

    def parse_block(self, block: Iterable[str], lineno: int, indent: int):
        ...

    def wrap_toks(
        self, block: Iterable[str], lineno: int, indent: int
    ) -> Generator[tuple[Any, Any, tuple[int, int], tuple[int, int], str], None, None]:
        ...

    def gen_lines(self, block: Iterable[str], indent: int) -> Generator[str, None, None]:
        ...


class MultiprocessingUnsupported(Exception):
    ...


class MultiprocessRefactoringTool(RefactoringTool):
    queue: Any | None
    output_lock: Any | None

    def refactor(self, items: Iterable[str], write: bool = ..., doctests_only: bool = ..., num_processes: int = ...) -> None:
        ...
