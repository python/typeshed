from typing import Literal

def make_archive(
    base_name: str,
    format: str,
    root_dir: str | None = ...,
    base_dir: str | None = ...,
    verbose: bool | Literal[0, 1] = 0,
    dry_run: bool | Literal[0, 1] = 0,
    owner: str | None = ...,
    group: str | None = ...,
) -> str: ...
def make_tarball(
    base_name: str,
    base_dir: str,
    compress: str | None = ...,
    verbose: bool | Literal[0, 1] = 0,
    dry_run: bool | Literal[0, 1] = 0,
    owner: str | None = ...,
    group: str | None = ...,
) -> str: ...
def make_zipfile(base_name: str, base_dir: str, verbose: bool | Literal[0, 1] = 0, dry_run: bool | Literal[0, 1] = 0) -> str: ...
