from _typeshed import AnyStr_co
from os import PathLike

from ._pygit2 import Oid
from .repository import BaseRepository

class PackBuilder:
    def __init__(self, repo: BaseRepository) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def add(self, oid: Oid) -> None: ...
    def add_recur(self, oid: Oid) -> None: ...
    def set_threads(self, n_threads: int) -> int: ...
    def write(self, path: PathLike[AnyStr_co] | bytes | str | None = None) -> None: ...
    @property
    def written_objects_count(self) -> int: ...
