import sys


if sys.version_info >= (3, 9):
    __all__ = ["iskeyword", "issoftkeyword", "kwlist", "softkwlist"]
else:
    __all__ = ["iskeyword", "kwlist"]

def iskeyword(s: str) -> bool: ...

kwlist: list[str]

if sys.version_info >= (3, 9):
    def issoftkeyword(s: str) -> bool: ...
    softkwlist: list[str]
