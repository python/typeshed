import sys
from multiprocessing import context, reduction as reducer
from multiprocessing.context import (
    AuthenticationError as AuthenticationError,
    BufferTooShort as BufferTooShort,
    Process as Process,
    ProcessError as ProcessError,
    TimeoutError as TimeoutError,
)
from multiprocessing.process import active_children as active_children, current_process as current_process

# These are technically functions that return instances of these Queue classes.
# Using them as annotations is deprecated. Use imports from multiprocessing.queues instead.
# See #4266 for discussion.
from multiprocessing.queues import JoinableQueue as JoinableQueue, Queue as Queue, SimpleQueue as SimpleQueue
from multiprocessing.spawn import freeze_support as freeze_support

if sys.version_info >= (3, 8):
    from multiprocessing.process import parent_process as parent_process

__all__ = [
    "Array",
    "AuthenticationError",
    "Barrier",
    "BoundedSemaphore",
    "BufferTooShort",
    "Condition",
    "Event",
    "JoinableQueue",
    "Lock",
    "Manager",
    "Pipe",
    "Pool",
    "Process",
    "ProcessError",
    "Queue",
    "RLock",
    "RawArray",
    "RawValue",
    "Semaphore",
    "SimpleQueue",
    "TimeoutError",
    "Value",
    "active_children",
    "allow_connection_pickling",
    "cpu_count",
    "current_process",
    "freeze_support",
    "get_all_start_methods",
    "get_context",
    "get_logger",
    "get_start_method",
    "log_to_stderr",
    "reducer",
    "set_executable",
    "set_forkserver_preload",
    "set_start_method",
]

if sys.version_info >= (3, 8):
    __all__ += ["parent_process"]

# These functions (really bound methods)
# are all autogenerated at runtime here: https://github.com/python/cpython/blob/600c65c094b0b48704d8ec2416930648052ba715/Lib/multiprocessing/__init__.py#L23
RawValue = context._default_context.RawValue
RawArray = context._default_context.RawArray
Value = context._default_context.Value
Array = context._default_context.Array
Barrier = context._default_context.Barrier
BoundedSemaphore = context._default_context.BoundedSemaphore
Condition = context._default_context.Condition
Event = context._default_context.Event
Lock = context._default_context.Lock
RLock = context._default_context.RLock
Semaphore = context._default_context.Semaphore
Pipe = context._default_context.Pipe
Pool = context._default_context.Pool
allow_connection_pickling = context._default_context.allow_connection_pickling
cpu_count = context._default_context.cpu_count
get_logger = context._default_context.get_logger
log_to_stderr = context._default_context.log_to_stderr
Manager = context._default_context.Manager
set_executable = context._default_context.set_executable
set_forkserver_preload = context._default_context.set_forkserver_preload
get_all_start_methods = context._default_context.get_all_start_methods
get_start_method = context._default_context.get_start_method
set_start_method = context._default_context.set_start_method
get_context = context._default_context.get_context
