import sys
from pathlib import Path

if sys.version_info >= (3, 10):
    from importlib.metadata._meta import SimplePath
    from zipfile import Path as ZipPath

    _: SimplePath = Path()
    _ = ZipPath("")
