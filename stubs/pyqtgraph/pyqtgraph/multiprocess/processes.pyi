import threading
from _typeshed import Incomplete

from .remoteproxy import ClosedError as ClosedError, NoResultError as NoResultError, RemoteEventHandler

__all__ = ["Process", "QtProcess", "ForkedProcess", "ClosedError", "NoResultError"]

class Process(RemoteEventHandler):
    debug: Incomplete
    proc: Incomplete
    def __init__(
        self,
        name=None,
        target=None,
        executable=None,
        copySysPath: bool = True,
        debug: bool = False,
        timeout: int = 20,
        wrapStdout=None,
        pyqtapis=None,
    ) -> None: ...
    def join(self, timeout: int = 10) -> None: ...
    def debugMsg(self, msg, *args) -> None: ...

class ForkedProcess(RemoteEventHandler):
    hasJoined: bool
    isParent: bool
    forkedProxies: Incomplete
    childPid: Incomplete
    def __init__(self, name=None, target: int = 0, preProxy=None, randomReseed: bool = True) -> None: ...
    def eventLoop(self) -> None: ...
    def join(self, timeout: int = 10) -> None: ...
    def kill(self) -> None: ...

class RemoteQtEventHandler(RemoteEventHandler):
    def __init__(self, *args, **kwds) -> None: ...
    timer: Incomplete
    def startEventTimer(self) -> None: ...
    def processRequests(self) -> None: ...

class QtProcess(Process):
    def __init__(self, **kwds) -> None: ...
    timer: Incomplete
    def startEventTimer(self) -> None: ...
    def startRequestProcessing(self, interval: float = 0.01) -> None: ...
    def stopRequestProcessing(self) -> None: ...
    def processRequests(self) -> None: ...

class FileForwarder(threading.Thread):
    input: Incomplete
    output: Incomplete
    lock: Incomplete
    daemon: bool
    color: Incomplete
    finish: Incomplete
    def __init__(self, input, output, color) -> None: ...
    def run(self) -> None: ...
