# Stubs for tempfile
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.3/library/tempfile.html

from typing import Tuple, BinaryIO
from contextlib import ContextManager

# global variables
tempdir = ...  # type: str
template = ...  # type: str

# TODO text files

# function stubs
def TemporaryFile(
            mode: str = ..., buffering: int = ..., encoding: str = ...,
            newline: str = ..., suffix: str = ..., prefix: str = ...,
            dir: str = ...) -> BinaryIO:
    ...
def NamedTemporaryFile(
            mode: str = ..., buffering: int = ..., encoding: str = ...,
            newline: str = ..., suffix: str = ..., prefix: str = ...,
            dir: str = ..., delete: bool =...) -> BinaryIO:
    ...
def SpooledTemporaryFile(
            max_size: int = ..., mode: str = ..., buffering: int = ...,
            encoding: str = ..., newline: str = ..., suffix: str = ...,
            prefix: str = ..., dir: str = ...) -> BinaryIO:
    ...

class TemporaryDirectory(ContextManager):
    name = ...  # type: str
    def __init__(self, suffix: str = ..., prefix: str = ...,
                 dir: str = ...) -> None: ...
    def cleanup(self) -> None: ...

def mkstemp(suffix: str = ..., prefix: str = ..., dir: str = ...,
            text: bool = ...) -> Tuple[int, str]: ...
def mkdtemp(suffix: str = ..., prefix: str = ...,
            dir: str = ...) -> str: ...
def mktemp(suffix: str = ..., prefix: str = ..., dir: str = ...) -> str: ...
def gettempdir() -> str: ...
def gettempprefix() -> str: ...
