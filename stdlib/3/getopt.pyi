# Stubs for getopt

# Based on http://docs.python.org/3.2/library/getopt.html

from typing import List, Tuple

def getopt(args: List[str], shortopts: str,
           longopts: List[str]=...) -> Tuple[List[Tuple[str, str]],
                                             List[str]]: ...

def gnu_getopt(args: List[str], shortopts: str,
               longopts: List[str]=...) -> Tuple[List[Tuple[str, str]],
                                                 List[str]]: ...

class GetoptError(Exception):
    msg = ...  # type: str
    opt = ...  # type: str
    def __init__(self, msg: str, opt: str=...) -> None: ...
    def __str__(self) -> str: ...

error = GetoptError
