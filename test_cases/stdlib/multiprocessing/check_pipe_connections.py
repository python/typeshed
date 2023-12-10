from __future__ import annotations

import sys
from multiprocessing.connection import Pipe

if sys.platform != "win32":
    from multiprocessing.connection import Connection
else:
    from multiprocessing.connection import PipeConnection as Connection


# Less type-safe, but no extra variable. User could mix up send and recv types.
# This should be improvable with PEP 695: Type Parameter Syntax in Python 3.12
a: Connection[str, int]
b: Connection[int, str]
a, b = Pipe()

# More type safe, but extra variable
connections_wrong: tuple[Connection[str, int], Connection[str, int]] = Pipe()  # pyright: ignore[reportGeneralTypeIssues]
connections_ok: tuple[Connection[str, int], Connection[int, str]] = Pipe()
a, b = connections_ok

a.send("test")
a.send(0)  # pyright: ignore[reportGeneralTypeIssues]
test1: str = b.recv()
test2: int = b.recv()  # pyright: ignore[reportGeneralTypeIssues]

b.send("test")  # pyright: ignore[reportGeneralTypeIssues]
b.send(0)
test3: str = a.recv()  # pyright: ignore[reportGeneralTypeIssues]
test4: int = a.recv()
