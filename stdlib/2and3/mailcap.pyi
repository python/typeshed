
from typing import Sequence, Dict, List, Union, Tuple, Optional

_Cap = Dict[str, Union[str, int]]
_CapDict = Dict[str, List[_Cap]]

def findmatch(caps: _CapDict, MIMEtype: str, key: str = ..., filename: str = ..., plist: Sequence[str] = ...) -> Tuple[Optional[str], Optional[_Cap]]: ...
def getcaps() -> _CapDict: ...
