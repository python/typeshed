from typing import List, Tuple

class GetoptError(Exception):
    opt = ... # type: str
    msg = ... # type: str
    def __init__(self, msg: str, opt: str=...) -> None: ...
    def __str__(self) -> str: ...

error = GetoptError

def getopt(args: List[str], shortopts: str,
           longopts: List[str]=...) -> Tuple[List[Tuple[str, str]],
                                             List[str]]: ...

def gnu_getopt(args: List[str], shortopts: str,
           longopts: List[str]=...) -> Tuple[List[Tuple[str,str]],
                                             List[str]]: ...

def do_longs(opts: List[Tuple[str,str]], opt: str,
             longopts: List[str], args: str): ...

def long_has_args(opt: str, longopts: List[str]) -> Tuple[bool,str]: ...

def do_short(opts: Tuple[List[Tuple[str,str]],List[str]],
             optstring: str, shortopts: str, args: List[str]): ...

def short_has_arg(opt: str, shortopts: str): ...
