# Source: https://hg.python.org/cpython/file/2.7/Lib/dircache.py

from typing import List

def reset() -> None: ...
def listdir(path: str) -> List[str]: ...

opendir = listdir

def annotate(head: str, list: List[str]) -> None: ...
