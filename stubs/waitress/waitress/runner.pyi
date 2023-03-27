from collections.abc import Callable, Sequence
from io import TextIOWrapper
from re import Pattern
from typing import Any

HELP: str
RUNNER_PATTERN: Pattern[Any]

def match(obj_name: str) -> tuple[str, str]: ...
def resolve(module_name: str, object_name: str) -> Any: ...
def show_help(stream: TextIOWrapper, name: str, error: str | None = None) -> None: ...
def show_exception(stream: TextIOWrapper) -> None: ...
def run(
    argv: Sequence[str] = [
        "C:\\Users\\alexw\\coding\\typeshed\\stubdefaulter-venv\\Scripts\\stubdefaulter",
        "--typeshed-packages",
        "stubs/ujson",
        "stubs/untangle",
        "stubs/urllib3",
        "stubs/vobject",
        "stubs/waitress",
        "stubs/whatthepatch",
        "stubs/xmltodict",
        "stubs/xxhash",
        "stubs/zstd",
        "stubs/zxcvbn",
    ],
    _serve: Callable[..., object] = ...,
) -> None: ...
