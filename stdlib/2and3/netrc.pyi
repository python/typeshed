from typing import Dict, Optional, Tuple, overload


class NetrcParseError(Exception):
    filename = ...  # type: Optional[str]
    lineno = ...  # type: Optional[int]
    msg = ''


# (login, account, password) tuple
_NetrcTuple = Tuple[str, Optional[str], Optional[str]]


class netrc:
    hosts = ...  # type: Dict[str, _NetrcTuple]
    macros = ...  # type: Dict[str, List[str]]

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, file) -> None: ...
    
    def authenticators(self, host: str) -> Optional[_NetrcTuple]: ...