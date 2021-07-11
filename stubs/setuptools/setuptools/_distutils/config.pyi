import abc
from distutils.cmd import Command
from typing import Any

DEFAULT_PYPIRC: str

class PyPIRCCommand(Command, metaclass=abc.ABCMeta):
    DEFAULT_REPOSITORY: str
    DEFAULT_REALM: str
    repository: Any
    realm: Any
    user_options: Any
    boolean_options: Any
    show_response: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
