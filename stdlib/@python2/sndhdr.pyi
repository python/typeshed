from _typeshed import AnyPath
from typing import Optional, Tuple, Union

_SndHeaders = Tuple[str, int, int, int, Union[int, str]]

def what(filename: AnyPath) -> Optional[_SndHeaders]: ...
def whathdr(filename: AnyPath) -> Optional[_SndHeaders]: ...
