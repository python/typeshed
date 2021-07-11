from typing import Any

def make_tarball(
    base_name,
    base_dir,
    compress: str = ...,
    verbose: int = ...,
    dry_run: int = ...,
    owner: Any | None = ...,
    group: Any | None = ...,
): ...
def make_zipfile(base_name, base_dir, verbose: int = ..., dry_run: int = ...): ...

ARCHIVE_FORMATS: Any

def check_archive_formats(formats): ...
def make_archive(
    base_name,
    format,
    root_dir: Any | None = ...,
    base_dir: Any | None = ...,
    verbose: int = ...,
    dry_run: int = ...,
    owner: Any | None = ...,
    group: Any | None = ...,
): ...
