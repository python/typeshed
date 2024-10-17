from __future__ import annotations

import _threading_local
import threading
from typing import Any

loc = threading.local()
loc.foo = 42
del loc.foo
loc.baz = ["spam", "eggs"]
del loc.baz

l2 = _threading_local.local()
l2.asdfasdf = 56
del l2.asdfasdf


# Type-checking when we don't have key-word only arguments.
def my_func(a: int, b: int) -> int: ...


def no_arguements() -> None: ...


# Fine
threading.Thread(target=my_func, args=(1, 1)).start()
# Incorrect
threading.Thread(target=my_func, args=(1, "test")).start()  # type: ignore
# Incorrect # of arguments
threading.Thread(target=my_func, args=(1, 1, 1)).start()  # type: ignore

# When providing kwargs, the type errors should go away.
threading.Thread(target=my_func, kwargs={"a": 1, "b": 1}).start()
threading.Thread(None, my_func, None, (), {"a": 1, "b": 1}).start()


# With no arguments, the type errors should go away.
threading.Thread(target=no_arguements).start()
