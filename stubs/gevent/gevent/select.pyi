import sys
from collections.abc import Collection
from select import error as error
from typing import Any

# this implementation is slightly more strict because it reuses the lists, so it can't
# just be any iterable, this is a little bit dangerous in terms of interoperability with
# the stdlib select module. link to github issue: https://github.com/gevent/gevent/issues/1979
def select(
    rlist: Collection[Any], wlist: Collection[Any], xlist: Collection[Any], timeout: float | None = None
) -> tuple[list[Any], list[Any], list[Any]]: ...

if sys.platform != "win32":
    from select import poll as poll

    __all__ = ["error", "poll", "select"]
else:
    __all__ = ["error", "select"]
