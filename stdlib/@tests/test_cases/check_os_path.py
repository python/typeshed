from __future__ import annotations
from _typeshed import StrOrBytesPath
from os import PathLike
from os.path import abspath, expanduser, expandvars
from typing_extensions import assert_type
from typing import Union


def test_str_path(str_path: StrOrBytesPath) -> None:
    # Ensures that these methods still work with a StrOrBytesPath
    # They were overloaded to work around python/mypy#3644
    # But removing the overloads workaround still breaks usage

    assert_type(abspath(str_path), Union[str, bytes])
    assert_type(expanduser(str_path), Union[str, bytes])
    assert_type(expandvars(str_path), Union[str, bytes])


class MyPath(PathLike):
    def __init__(self, path: str | bytes):
        super().__init__()
        self.path = path

    def __fspath__(self) -> str | bytes:
        return self.path


abspath(MyPath("."))
