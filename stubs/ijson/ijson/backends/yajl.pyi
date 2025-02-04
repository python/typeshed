from _typeshed import Incomplete
from collections.abc import Generator
from ctypes import CDLL, Structure

yajl: CDLL

class Config(Structure): ...

def basic_parse_basecoro(
    target, allow_comments: bool = False, multiple_values: bool = False, use_float: bool = False
) -> Generator[None, bytes]: ...
