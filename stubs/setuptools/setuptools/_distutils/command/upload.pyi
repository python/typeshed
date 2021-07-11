from distutils.core import PyPIRCCommand
from typing import Any

class upload(PyPIRCCommand):
    description: str
    user_options: Any
    boolean_options: Any
    username: str
    password: str
    show_response: int
    sign: bool
    identity: Any
    def initialize_options(self) -> None: ...
    repository: Any
    realm: Any
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def upload_file(self, command, pyversion, filename) -> None: ...
