from ctypes import Structure
from typing import Any

from .compat import text_type as text_type
from .util import preprocess_paths as preprocess_paths

kernel32: Any
GetShortPathNameW: Any
shell32: Any
SHFileOperationW: Any

class SHFILEOPSTRUCTW(Structure): ...

FO_MOVE: int
FO_COPY: int
FO_DELETE: int
FO_RENAME: int
FOF_MULTIDESTFILES: int
FOF_SILENT: int
FOF_NOCONFIRMATION: int
FOF_ALLOWUNDO: int
FOF_NOERRORUI: int

def prefix_and_path(path): ...
def get_awaited_path_from_prefix(prefix, path): ...
def get_short_path_name(long_name): ...
def send2trash(paths) -> None: ...
