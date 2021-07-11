import distutils.command.sdist as orig
from typing import Any

from .py36compat import sdist_add_defaults as sdist_add_defaults

def walk_revctrl(dirname: str = ...) -> None: ...

class sdist(sdist_add_defaults, orig.sdist):
    user_options: Any
    negative_opt: Any
    README_EXTENSIONS: Any
    READMES: Any
    filelist: Any
    def run(self) -> None: ...
    def initialize_options(self) -> None: ...
    def make_distribution(self) -> None: ...
    def check_readme(self) -> None: ...
    def make_release_tree(self, base_dir, files) -> None: ...
    def read_manifest(self) -> None: ...
