from collections.abc import Callable
from typing import Any, ClassVar

from ..config import PyPIRCCommand

class register(PyPIRCCommand):
    description: str
    # Any to work around variance issues
    sub_commands: ClassVar[list[tuple[str, Callable[[Any], bool] | None]]]
    list_classifiers: int
    strict: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_metadata(self) -> None: ...
    def classifiers(self) -> None: ...
    def verify_metadata(self) -> None: ...
    def send_metadata(self) -> None: ...
    def build_post_data(self, action): ...
    def post_to_server(self, data, auth: Any | None = None): ...
