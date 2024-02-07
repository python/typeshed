from pathlib import Path
from typing import Any

from cffi import FFI

dir_path: Path
h_files: list[str]
h_source: list[str]
h_file: Path
f: Any
C_HEADER_SRC: str
C_PREAMBLE: str
_: Path
libgit2_kw: dict[str, Any]
ffi: FFI
