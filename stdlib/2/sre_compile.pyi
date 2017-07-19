# Source: https://hg.python.org/cpython/file/2.7/Lib/sre_compile.py

from sre_parse import SubPattern
from typing import Any, Pattern, Tuple, Type, Union

MAXCODE = ...  # type: int
STRING_TYPES = ...  # type: Union[Tuple[Type[str]], Tuple[Type[str], Type[unicode]]]

def isstring(obj: Any) -> int: ...
def compile(p: Union[str, SubPattern], flags: int = ...) -> Pattern: ...
