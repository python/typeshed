import sys
from _typeshed import StrPath
from collections.abc import Sequence
from typing import IO

__all__ = [
    "knownfiles",
    "inited",
    "MimeTypes",
    "guess_type",
    "guess_all_extensions",
    "guess_extension",
    "add_type",
    "init",
    "read_mime_types",
    "suffix_map",
    "encodings_map",
    "types_map",
    "common_types",
]

if sys.version_info >= (3, 8):
    def guess_type(url: StrPath, strict: bool = True) -> tuple[str | None, str | None]: ...

else:
    def guess_type(url: str, strict: bool = True) -> tuple[str | None, str | None]: ...

def guess_all_extensions(type: str, strict: bool = True) -> list[str]: ...
def guess_extension(type: str, strict: bool = True) -> str | None: ...
def init(files: Sequence[str] | None = None) -> None: ...
def read_mime_types(file: str) -> dict[str, str] | None: ...
def add_type(type: str, ext: str, strict: bool = True) -> None: ...

inited: bool
knownfiles: list[str]
suffix_map: dict[str, str]
encodings_map: dict[str, str]
types_map: dict[str, str]
common_types: dict[str, str]

class MimeTypes:
    suffix_map: dict[str, str]
    encodings_map: dict[str, str]
    types_map: tuple[dict[str, str], dict[str, str]]
    types_map_inv: tuple[dict[str, str], dict[str, str]]
    def __init__(self, filenames: tuple[str, ...] = (), strict: bool = True) -> None: ...
    def guess_extension(self, type: str, strict: bool = True) -> str | None: ...
    if sys.version_info >= (3, 8):
        def guess_type(self, url: StrPath, strict: bool = True) -> tuple[str | None, str | None]: ...
    else:
        def guess_type(self, url: str, strict: bool = True) -> tuple[str | None, str | None]: ...

    def guess_all_extensions(self, type: str, strict: bool = True) -> list[str]: ...
    def read(self, filename: str, strict: bool = True) -> None: ...
    def readfp(self, fp: IO[str], strict: bool = True) -> None: ...
    if sys.platform == "win32":
        def read_windows_registry(self, strict: bool = True) -> None: ...
