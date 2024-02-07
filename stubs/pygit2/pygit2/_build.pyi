from pathlib import Path
from typing import Any

__version__: str

def get_libgit2_paths() -> tuple[Path, dict[str, Any]]: ...
