import sys
from _typeshed import AnyPath
from typing import NamedTuple, Optional, Tuple, Union

class SndHeaders(NamedTuple):
    filetype: str
    framerate: int
    nchannels: int
    nframes: int
    sampwidth: Union[int, str]
_SndHeaders = SndHeaders
def what(filename: AnyPath) -> Optional[_SndHeaders]: ...
def whathdr(filename: AnyPath) -> Optional[_SndHeaders]: ...
