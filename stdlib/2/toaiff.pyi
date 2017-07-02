# Stubs for toaiff (Python 2)

# Source: https://hg.python.org/cpython/file/2.7/Lib/toaiff.py
from pipes import Template
from typing import Dict, List, Optional


class error(Exception): ...

table: Dict[str, Template]
t: Template
uncompress: Template
def toaiff(filename: str) -> Optional[str]: ...
def _toaiff(filename: str, temps: List[str]) -> str: ... 
