from _typeshed import Incomplete

winterm: Incomplete

def winset(reset: bool = False, fore=None, back=None, style=None, stderr: bool = False) -> None: ...

ANSI: Incomplete
WIN: Incomplete
color: Incomplete
RESET: int

def cprint(stream, *args, **kwds) -> None: ...
def cout(*args) -> None: ...
def cerr(*args) -> None: ...
