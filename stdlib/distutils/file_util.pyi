from collections.abc import Sequence

def copy_file(
    src: str,
    dst: str,
    preserve_mode: bool = 1,
    preserve_times: bool = 1,
    update: bool = 0,
    link: str | None = None,
    verbose: bool = 1,
    dry_run: bool = 0,
) -> tuple[str, str]: ...
def move_file(src: str, dst: str, verbose: bool = 1, dry_run: bool = 0) -> str: ...
def write_file(filename: str, contents: Sequence[str]) -> None: ...
