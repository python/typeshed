import sys
from asyncio.base_events import BaseEventLoop as BaseEventLoop
from asyncio.coroutines import coroutine as coroutine
from asyncio.coroutines import iscoroutine as iscoroutine
from asyncio.coroutines import iscoroutinefunction as iscoroutinefunction
from asyncio.events import AbstractEventLoop as AbstractEventLoop
from asyncio.events import AbstractEventLoopPolicy as AbstractEventLoopPolicy
from asyncio.events import AbstractServer as AbstractServer
from asyncio.events import Handle as Handle
from asyncio.events import TimerHandle as TimerHandle
from asyncio.events import get_child_watcher as get_child_watcher
from asyncio.events import get_event_loop as get_event_loop
from asyncio.events import get_event_loop_policy as get_event_loop_policy
from asyncio.events import new_event_loop as new_event_loop
from asyncio.events import set_child_watcher as set_child_watcher
from asyncio.events import set_event_loop as set_event_loop
from asyncio.events import set_event_loop_policy as set_event_loop_policy
from asyncio.futures import CancelledError as CancelledError
from asyncio.futures import Future as Future
from asyncio.futures import InvalidStateError as InvalidStateError
from asyncio.futures import TimeoutError as TimeoutError
from asyncio.futures import wrap_future as wrap_future
from asyncio.locks import BoundedSemaphore as BoundedSemaphore
from asyncio.locks import Condition as Condition
from asyncio.locks import Event as Event
from asyncio.locks import Lock as Lock
from asyncio.locks import Semaphore as Semaphore
from asyncio.protocols import BaseProtocol as BaseProtocol
from asyncio.protocols import DatagramProtocol as DatagramProtocol
from asyncio.protocols import Protocol as Protocol
from asyncio.protocols import SubprocessProtocol as SubprocessProtocol
from asyncio.queues import LifoQueue as LifoQueue
from asyncio.queues import PriorityQueue as PriorityQueue
from asyncio.queues import Queue as Queue
from asyncio.queues import QueueEmpty as QueueEmpty
from asyncio.queues import QueueFull as QueueFull
from asyncio.streams import IncompleteReadError as IncompleteReadError
from asyncio.streams import LimitOverrunError as LimitOverrunError
from asyncio.streams import StreamReader as StreamReader
from asyncio.streams import StreamReaderProtocol as StreamReaderProtocol
from asyncio.streams import StreamWriter as StreamWriter
from asyncio.streams import open_connection as open_connection
from asyncio.streams import start_server as start_server
from asyncio.subprocess import create_subprocess_exec as create_subprocess_exec
from asyncio.subprocess import create_subprocess_shell as create_subprocess_shell
from asyncio.tasks import ALL_COMPLETED as ALL_COMPLETED
from asyncio.tasks import FIRST_COMPLETED as FIRST_COMPLETED
from asyncio.tasks import FIRST_EXCEPTION as FIRST_EXCEPTION
from asyncio.tasks import Task as Task
from asyncio.tasks import as_completed as as_completed
from asyncio.tasks import ensure_future as ensure_future
from asyncio.tasks import gather as gather
from asyncio.tasks import run_coroutine_threadsafe as run_coroutine_threadsafe
from asyncio.tasks import shield as shield
from asyncio.tasks import sleep as sleep
from asyncio.tasks import wait as wait
from asyncio.tasks import wait_for as wait_for
from asyncio.transports import BaseTransport as BaseTransport
from asyncio.transports import DatagramTransport as DatagramTransport
from asyncio.transports import ReadTransport as ReadTransport
from asyncio.transports import SubprocessTransport as SubprocessTransport
from asyncio.transports import Transport as Transport
from asyncio.transports import WriteTransport as WriteTransport
from typing import List, Type

if sys.version_info < (3, 5):
    from asyncio.queues import JoinableQueue as JoinableQueue
else:
    from asyncio.futures import isfuture as isfuture
    from asyncio.events import (
        _set_running_loop as _set_running_loop,
        _get_running_loop as _get_running_loop,
    )
if sys.platform != 'win32':
    from asyncio.streams import (
        open_unix_connection as open_unix_connection,
        start_unix_server as start_unix_server,
    )

if sys.version_info >= (3, 7):
    from asyncio.events import (
        get_running_loop as get_running_loop,
    )
    from asyncio.tasks import (
        all_tasks as all_tasks,
        create_task as create_task,
        current_task as current_task,
    )
    from asyncio.runners import (
        run as run,
    )


# TODO: It should be possible to instantiate these classes, but mypy
# currently disallows this.
# See https://github.com/python/mypy/issues/1843
SelectorEventLoop: Type[AbstractEventLoop]
if sys.platform == 'win32':
    ProactorEventLoop: Type[AbstractEventLoop]
DefaultEventLoopPolicy: Type[AbstractEventLoopPolicy]

# TODO: AbstractChildWatcher (UNIX only)

__all__: List[str]
