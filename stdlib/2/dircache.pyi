# Source: https://hg.python.org/cpython/file/2.7/Lib/dircache.py

from typing import List, Text

def reset() -> None: ...
def listdir(path: Text) -> List[Text]: ...

opendir = listdir

def annotate(head: Text, list: List[Text]) -> None: ...
