from _typeshed import Incomplete

from . import internals as internals

PYSIDE: str
PYSIDE2: str
PYSIDE6: str
PYQT4: str
PYQT5: str
PYQT6: str
QT_LIB: Incomplete
libOrder: Incomplete
QT_LIB = lib
qt: Incomplete
QT_LIB = lib

class FailedImport:
    err: Incomplete
    def __init__(self, err) -> None: ...
    def __getattr__(self, attr) -> None: ...

class _StringIO:
    data: Incomplete
    def __init__(self) -> None: ...
    def write(self, data) -> None: ...
    def getvalue(self): ...

VERSION_INFO: Incomplete
module: Incomplete
module_whitelist: Incomplete
attr: Incomplete
QtVersion: Incomplete
loadUiType: Incomplete
isQObjectAlive: Incomplete

@staticmethod
def qWait(msec) -> None: ...

sys_excepthook: Incomplete

def pyqt_qabort_override(*args, **kwds): ...

versionReq: Incomplete
m: Incomplete
App: Incomplete
QAPP: Incomplete

def mkQApp(name=None): ...
def exec_(): ...
