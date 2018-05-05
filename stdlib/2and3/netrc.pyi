from typing import Dict, List, Optional, Tuple, overload


class NetrcParseError(Exception):
    filename = ...  # type: Optional[str]
    lineno = ...  # type: Optional[int]
    msg = ...  # type: str


# (login, account, password) tuple
_NetrcTuple = Tuple[str, Optional[str], Optional[str]]


class netrc:
    hosts = ...  # type: Dict[str, _NetrcTuple]
    macros = ...  # type: Dict[str, List[str]]

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, file: str) -> None: ...

    def authenticators(self, host: str) -> Optional[_NetrcTuple]: ...
