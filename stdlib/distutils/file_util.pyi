from collections.abc import Sequence
from typing import Literal

def copy_file(
    src: str,
    dst: str,
    preserve_mode: bool | Literal[0, 1] = 1,
    preserve_times: bool | Literal[0, 1] = 1,
    update: bool | Literal[0, 1] = 0,
    link: str | None = None,
    verbose: bool | Literal[0, 1] = 1,
    dry_run: bool | Literal[0, 1] = 0,
) -> tuple[str, str]: ...
def move_file(src: str, dst: str, verbose: bool | Literal[0, 1] = 0, dry_run: bool | Literal[0, 1] = 0) -> str: ...
def write_file(filename: str, contents: Sequence[str]) -> None: ...
