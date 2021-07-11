from typing import Any

def copy_file(
    src,
    dst,
    preserve_mode: int = ...,
    preserve_times: int = ...,
    update: int = ...,
    link: Any | None = ...,
    verbose: int = ...,
    dry_run: int = ...,
): ...
def move_file(src, dst, verbose: int = ..., dry_run: int = ...): ...
def write_file(filename, contents) -> None: ...
