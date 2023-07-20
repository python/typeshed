from _typeshed import Incomplete, Unused
from typing import Any
from typing_extensions import Literal

def register(viewer, order: int = 1) -> None: ...
def show(image, title: Incomplete | None = None, **options): ...

class Viewer:
    def show(self, image, **options): ...
    format: Incomplete
    options: Incomplete
    def get_format(self, image): ...
    # Abstract method
    def get_command(self, file: str, **options: Any) -> str: ...
    def save_image(self, image): ...
    def show_image(self, image, **options): ...
    def show_file(self, path: str, **options: Any) -> Literal[1]: ...

class WindowsViewer(Viewer):
    format: str
    options: Incomplete
    def get_command(self, file: str, **options: Unused) -> str: ...

class MacViewer(Viewer):
    format: str
    options: Incomplete
    def get_command(self, file: str, **options: Unused) -> str: ...
    def show_file(self, path: str, **options: Unused) -> Literal[1]: ...

class UnixViewer(Viewer):
    format: str
    options: Incomplete
    # Unix viewer expects the following method to be implemented on all
    # subclasses, but it isn't defined on the base class.
    # def get_command_ex(self, file: str, **options: Any) -> tuple[str, str]: ...
    def get_command(self, file: str, **options: Any) -> str: ...

class XDGViewer(UnixViewer):
    def get_command_ex(self, file: str, **options: Unused) -> tuple[str, str]: ...
    def show_file(self, path: str, **options: Unused) -> Literal[1]: ...

class DisplayViewer(UnixViewer):
    def get_command_ex(self, file: str, title: str | None = None, **options: Unused) -> tuple[str, str]: ...
    def show_file(self, path: str, *, title: str | None = None, **options: Unused) -> Literal[1]: ...

class GmDisplayViewer(UnixViewer):
    def get_command_ex(self, file: str, **options: Unused) -> tuple[str, str]: ...
    def show_file(self, path: str, **options: Unused) -> Literal[1]: ...

class EogViewer(UnixViewer):
    def get_command_ex(self, file: str, **options: Unused) -> tuple[str, str]: ...
    def show_file(self, path: str, **options: Unused) -> Literal[1]: ...

class XVViewer(UnixViewer):
    def get_command_ex(self, file, title: str | None = None, **options: Unused) -> tuple[str, str]: ...
    def show_file(self, path: str, *, title: str | None = None, **options: Unused) -> Literal[1]: ...

class IPythonViewer(Viewer):
    def show_image(self, image, **options: Unused) -> Literal[1]: ...
