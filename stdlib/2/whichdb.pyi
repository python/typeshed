# Source: https://hg.python.org/cpython/file/2.7/Lib/whichdb.py

from types import ModuleType
from typing import Optional, Text

dbm = ...  # type: Optional[ModuleType]

def whichdb(filename: Text) -> Optional[str]: ...
