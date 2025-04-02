import sys
from _typeshed import Incomplete
from typing import ClassVar, Literal

from ..cmd import Command

if sys.platform == "win32":
    from msilib import Control, Dialog

    class PyDialog(Dialog):
        def __init__(self, *args, **kw) -> None: ...
        def title(self, title) -> None: ...
        def back(self, title, next, name: str = "Back", active: bool | Literal[0, 1] = 1) -> Control: ...
        def cancel(self, title, next, name: str = "Cancel", active: bool | Literal[0, 1] = 1) -> Control: ...
        def next(self, title, next, name: str = "Next", active: bool | Literal[0, 1] = 1) -> Control: ...
        def xbutton(self, name, title, next, xpos) -> Control: ...

    class bdist_msi(Command):
        description: str
        user_options: ClassVar[list[tuple[str, str | None, str]]]
        boolean_options: ClassVar[list[str]]
        all_versions: Incomplete
        other_version: str
        def __init__(self, *args, **kw) -> None: ...
        bdist_dir: Incomplete
        plat_name: Incomplete
        keep_temp: int
        no_target_compile: int
        no_target_optimize: int
        target_version: Incomplete
        dist_dir: Incomplete
        skip_build: Incomplete
        install_script: Incomplete
        pre_install_script: Incomplete
        versions: Incomplete
        def initialize_options(self) -> None: ...
        install_script_key: Incomplete
        def finalize_options(self) -> None: ...
        db: Incomplete
        def run(self) -> None: ...
        def add_files(self) -> None: ...
        def add_find_python(self) -> None: ...
        def add_scripts(self) -> None: ...
        def add_ui(self) -> None: ...
        def get_installer_filename(self, fullname): ...
