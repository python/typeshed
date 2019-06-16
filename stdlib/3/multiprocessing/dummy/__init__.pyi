import array
import sys
import threading
import weakref
from queue import Queue
from threading import Barrier, BoundedSemaphore, Condition, Event, Lock, RLock, Semaphore
from typing import Any, List, Optional, Type

from .connection import Pipe

JoinableQueue = Queue


class DummyProcess(threading.Thread):
    _children: weakref.WeakKeyDictionary
    _parent: threading.Thread
    _pid: None
    _start_called: int
    exitcode: Optional[int]
    def __init__(self, group=..., target=..., name=..., args=..., kwargs=...) -> None: ...

Process = DummyProcess

class Namespace(object):
    def __init__(self, **kwds) -> None: ...

class Value(object):
    _typecode: Any
    _value: Any
    value: Any
    def __init__(self, typecode, value, lock=...) -> None: ...


def Array(typecode, sequence, lock=...) -> array.array: ...
def Manager() -> Any: ...
def Pool(processes=..., initializer=..., initargs=...) -> Any: ...
def active_children() -> List: ...
def current_process() -> threading.Thread: ...
def freeze_support() -> None: ...
def shutdown() -> None: ...
