from _typeshed import StrOrBytesPath

from metadata import version as version
from renderer import render as render

_OpenFile = StrOrBytesPath | int

def main(template: _OpenFile, data: _OpenFile | None = ..., **kwargs) -> str: ...
def cli_main() -> None: ...
