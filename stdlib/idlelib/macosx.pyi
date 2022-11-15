from typing import Any
from tkinter import Tk
from idlelib.filelist import FileList

def isAquaTk() -> bool: ...
def isCarbonTk() -> bool: ...
def isCocoaTk() -> bool: ...
def isXQuartz() -> bool: ...
def readSystemPreferences() -> dict[str, Any] | None: ...
def preferTabsPreferenceWarning() -> str | None: ...
def addOpenEventSupport(root: Tk, flist: FileList) -> None: ...
def hideTkConsole(root: Tk) -> None: ...
def overrideRootMenu(root: Tk, flist: FileList) -> None: ...
def fixb2context(root: Tk) -> None: ...
def setupApp(root: Tk, flist: FileList) -> None: ...
