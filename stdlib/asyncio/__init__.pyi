import sys
from collections.abc import Awaitable, Coroutine, Generator
from typing import Any, TypeVar
from typing_extensions import TypeAlias

# As at runtime, this depends on all submodules defining __all__ accurately.
from .base_events import *
from .coroutines import *
from .events import *
from .exceptions import *
from .futures import *
from .locks import *
from .protocols import *
from .queues import *
from .runners import *
from .streams import *
from .subprocess import *
from .tasks import *
from .transports import *

__all__: tuple[str, ...] = (
    "BaseEventLoop",  # from base_events
    "iscoroutinefunction",  # from coroutines
    "iscoroutine",  # from coroutines
    "AbstractEventLoopPolicy",  # from events
    "AbstractEventLoop",  # from events
    "AbstractServer",  # from events
    "Handle",  # from events
    "TimerHandle",  # from events
    "get_event_loop_policy",  # from events
    "set_event_loop_policy",  # from events
    "get_event_loop",  # from events
    "set_event_loop",  # from events
    "new_event_loop",  # from events
    "_set_running_loop",  # from events
    "get_running_loop",  # from events
    "_get_running_loop",  # from events
    "CancelledError",  # from exceptions
    "InvalidStateError",  # from exceptions
    "TimeoutError",  # from exceptions
    "IncompleteReadError",  # from exceptions
    "LimitOverrunError",  # from exceptions
    "SendfileNotAvailableError",  # from exceptions
    "Future",  # from futures
    "wrap_future",  # from futures
    "isfuture",  # from futures
    "Lock",  # from locks
    "Event",  # from locks
    "Condition",  # from locks
    "Semaphore",  # from locks
    "BoundedSemaphore",  # from locks
    "BaseProtocol",  # from protocols
    "Protocol",  # from protocols
    "DatagramProtocol",  # from protocols
    "SubprocessProtocol",  # from protocols
    "BufferedProtocol",  # from protocols
    "run",  # from runners
    "Queue",  # from queues
    "PriorityQueue",  # from queues
    "LifoQueue",  # from queues
    "QueueFull",  # from queues
    "QueueEmpty",  # from queues
    "StreamReader",  # from streams
    "StreamWriter",  # from streams
    "StreamReaderProtocol",  # from streams
    "open_connection",  # from streams
    "start_server",  # from streams
    "create_subprocess_exec",  # from subprocess
    "create_subprocess_shell",  # from subprocess
    "Task",  # from tasks
    "create_task",  # from tasks
    "FIRST_COMPLETED",  # from tasks
    "FIRST_EXCEPTION",  # from tasks
    "ALL_COMPLETED",  # from tasks
    "wait",  # from tasks
    "wait_for",  # from tasks
    "as_completed",  # from tasks
    "sleep",  # from tasks
    "gather",  # from tasks
    "shield",  # from tasks
    "ensure_future",  # from tasks
    "run_coroutine_threadsafe",  # from tasks
    "current_task",  # from tasks
    "all_tasks",  # from tasks
    "_register_task",  # from tasks
    "_unregister_task",  # from tasks
    "_enter_task",  # from tasks
    "_leave_task",  # from tasks
    "BaseTransport",  # from transports
    "ReadTransport",  # from transports
    "WriteTransport",  # from transports
    "Transport",  # from transports
    "DatagramTransport",  # from transports
    "SubprocessTransport",  # from transports
)

if sys.version_info >= (3, 9):
    from .threads import *

    __all__ += ("Server", "to_thread")  # from base_events  # from threads

if sys.version_info >= (3, 11):
    from .taskgroups import *
    from .timeouts import *

    __all__ += (
        "BrokenBarrierError",  # from exceptions
        "Barrier",  # from locks
        "Runner",  # from runners
        "Timeout",  # from timeouts
        "timeout",  # from timeouts
        "timeout_at",  # from timeouts
    )
else:
    __all__ += ("coroutine",)  # from coroutines

if sys.version_info >= (3, 12):
    __all__ += ("create_eager_task_factory", "eager_task_factory")  # from tasks
    __all__ += ("TaskGroup",)  # from taskgroups

if sys.version_info >= (3, 13):
    __all__ += ("QueueShutDown",)  # from queues

if sys.version_info < (3, 14):
    __all__ += ("get_child_watcher", "set_child_watcher")  # from events

if sys.platform == "win32":
    from .windows_events import *

    __all__ += (
        "SelectorEventLoop",  # from windows_events
        "ProactorEventLoop",  # from windows_events
        "IocpProactor",  # from windows_events
        "DefaultEventLoopPolicy",  # from windows_events
        "WindowsSelectorEventLoopPolicy",  # from windows_events
        "WindowsProactorEventLoopPolicy",  # from windows_events
    )
    if sys.version_info >= (3, 13):
        __all__ += ("EventLoop",)  # from windows_events

else:
    from .unix_events import *

    __all__ += (
        "open_unix_connection",  # from streams
        "start_unix_server",  # from streams
        "SelectorEventLoop",  # from unix_events
        "DefaultEventLoopPolicy",  # from unix_events
    )
    if sys.version_info >= (3, 13):
        __all__ += ("EventLoop",)  # from unix_events

    if sys.version_info < (3, 14):
        __all__ += (
            "AbstractChildWatcher",  # from unix_events
            "SafeChildWatcher",  # from unix_events
            "FastChildWatcher",  # from unix_events
            "MultiLoopChildWatcher",  # from unix_events
            "ThreadedChildWatcher",  # from unix_events
        )
        if sys.version_info >= (3, 9):
            __all__ += ("PidfdChildWatcher",)  # from unix_events

_T_co = TypeVar("_T_co", covariant=True)

# Aliases imported by multiple submodules in typeshed
if sys.version_info >= (3, 12):
    _AwaitableLike: TypeAlias = Awaitable[_T_co]  # noqa: Y047
    _CoroutineLike: TypeAlias = Coroutine[Any, Any, _T_co]  # noqa: Y047
else:
    _AwaitableLike: TypeAlias = Generator[Any, None, _T_co] | Awaitable[_T_co]
    _CoroutineLike: TypeAlias = Generator[Any, None, _T_co] | Coroutine[Any, Any, _T_co]
