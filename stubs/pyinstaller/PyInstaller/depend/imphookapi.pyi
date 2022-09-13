# https://pyinstaller.org/en/stable/hooks-config.html `hook_api` is a PostGraphAPI

from _typeshed import StrOrBytesPath
from collections.abc import Iterable

from PyInstaller.building.build_main import Analysis

class PostGraphAPI:
    @property
    def __path__(self) -> tuple[str, ...] | None: ...
    @property
    def analysis(self) -> Analysis: ...
    def add_datas(self, list_of_tuples: Iterable[tuple[StrOrBytesPath, StrOrBytesPath]]) -> None: ...
