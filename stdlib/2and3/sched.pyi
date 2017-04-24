# Stub for sched (Python 2 and 3)

import sys
from typing import Any, Callable, Dict, List, NamedTuple, Text, Tuple

class Event(NamedTuple):
    time: float
    priority: Any
    action: Callable[..., Any]
    argument: Tuple[Any, ...]
    kwargs: Dict[Text, Any]

class scheduler:
    if sys.version_info >= (3, 3):
        def __init__(self, timefunc: Callable[[], float] = ..., delayfunc: Callable[[float], None] = ...) -> None: ...
        def enterabs(self, time: float, priority: Any, action: Callable[..., Any], argument: Tuple[Any, ...] = ..., kwargs: Dict[str, Any] = ...) -> Event: ...
        def enter(self, delay: float, priority: Any, action: Callable[..., Any], argument: Tuple[Any, ...] = ..., kwargs: Dict[str, Any] = ...) -> Event: ...
        def run(self, blocking: bool = ...) -> float: ...
    else:
        def __init__(self, timefunc: Callable[[], float], delayfunc: Callable[[float], None]) -> None: ...
        def enterabs(self, time: float, priority: Any, action: Callable[..., Any], argument: Tuple[Any, ...]) -> Event: ...
        def enter(self, delay: float, priority: Any, action: Callable[..., Any], argument: Tuple[Any, ...]) -> Event: ...
        def run(self) -> float: ...

    def cancel(self, event: Event) -> None: ...
    def empty(self) -> bool: ...
    @property
    def queue(self) -> List[Event]: ...
