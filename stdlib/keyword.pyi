from collections.abc import Sequence
import sys


def iskeyword(s: str) -> bool: ...

kwlist: Sequence[str]

if sys.version_info >= (3, 9):
    def issoftkeyword(s: str) -> bool: ...
    softkwlist: Sequence[str]
