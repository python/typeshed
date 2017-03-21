# Stubs for zipapp (Python 3.5+)

from pathlib import Path
from typing import BinaryIO, Optional, Union

_Path = Union[str, Path]

class ZipAppError(Exception): ...

def create_archive(source: Union[_Path, BinaryIO], target: Union[_Path, BinaryIO, None] = ..., interpreter: Optional[str] = ..., main: Optional[str] = ...) -> None: ...
def get_interpreter(archive: Union[_Path, BinaryIO]) -> str: ...
