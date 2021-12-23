import sys
from typing import Callable, Sequence

class Error(Exception): ...

if sys.version_info >= (3, 7):
    def register(
        name: str, klass: Callable[[], BaseBrowser] | None, instance: BaseBrowser | None = ..., *, preferred: bool = ...
    ) -> None: ...

else:
    def register(
        name: str, klass: Callable[[], BaseBrowser] | None, instance: BaseBrowser | None = ..., update_tryorder: int = ...
    ) -> None: ...

def get(using: str | None = ...) -> BaseBrowser: ...
def open(url: str, new: int = ..., autoraise: bool = ...) -> bool: ...
def open_new(url: str) -> bool: ...
def open_new_tab(url: str) -> bool: ...

class BaseBrowser:
    args: list[str]
    name: str
    basename: str
    def __init__(self, name: str = ...) -> None: ...
    def open(self, url: str, new: int = ..., autoraise: bool = ...) -> bool: ...
    def open_new(self, url: str) -> bool: ...
    def open_new_tab(self, url: str) -> bool: ...

class GenericBrowser(BaseBrowser):
    def __init__(self, name: str | Sequence[str]) -> None: ...

class BackgroundBrowser(GenericBrowser): ...
class UnixBrowser(BaseBrowser):
    raise_opts: list[str] | None
    background: bool
    redirect_stdout: bool
    remote_args: list[str]
    remote_action: str
    remote_action_newwin: str
    remote_action_newtab: str

class Mozilla(UnixBrowser): ...
class Galeon(UnixBrowser):
    raise_opts: list[str]

class Chrome(UnixBrowser): ...
class Opera(UnixBrowser): ...
class Elinks(UnixBrowser): ...
class Konqueror(BaseBrowser): ...
class Grail(BaseBrowser): ...

if sys.platform == "win32":
    class WindowsDefault(BaseBrowser): ...

if sys.platform == "darwin":
    class MacOSX(BaseBrowser): ...
    class MacOSXOSAScript(BaseBrowser): ...  # In runtime this class does not have `name` and `basename`
