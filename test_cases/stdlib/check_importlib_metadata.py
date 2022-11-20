import sys
from importlib.metadata._meta import SimplePath
from pathlib import Path

if sys.version_info >= (3, 9):
    from zipfile import Path as ZipPath

    _: SimplePath = Path()
    _ = ZipPath("")
