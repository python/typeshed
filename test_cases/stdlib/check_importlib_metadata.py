import sys
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 10):
    from importlib.metadata._meta import SimplePath
    from zipfile import Path as ZipPath

    if sys.version_info >= (3, 12):

        def takes_simple_path(p: SimplePath[Any]) -> None: ...

    else:

        def takes_simple_path(p: SimplePath) -> None: ...

    takes_simple_path(Path())
    takes_simple_path(ZipPath(""))
    takes_simple_path("some string")  # type: ignore
