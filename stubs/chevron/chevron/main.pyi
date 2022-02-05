from _typeshed import StrOrBytesPath
from typing import Any

from metadata import version as version
from renderer import render as render

_OpenFile = StrOrBytesPath | int

def main(template: _OpenFile, data: _OpenFile | None = ..., **kwargs: Any) -> str: ...
def cli_main() -> None: ...
