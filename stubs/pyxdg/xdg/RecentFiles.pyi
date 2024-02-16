from _typeshed import Incomplete, StrOrBytesPath, StrPath
from collections.abc import Iterable

class RecentFiles:
    RecentFiles: list[RecentFile]
    filename: str
    def __init__(self) -> None: ...
    def parse(self, filename: StrPath | None = None) -> None: ...
    def write(self, filename: StrOrBytesPath | None = None) -> None: ...
    def getFiles(
        self, mimetypes: Iterable[str] | None = None, groups: Iterable[Incomplete] | None = None, limit: int = 0
    ) -> list[StrPath]: ...
    def addFile(
        self, item: StrPath, mimetype: str, groups: Iterable[Incomplete] | None = None, private: bool = False
    ) -> None: ...
    def deleteFile(self, item: RecentFile | StrPath) -> None: ...
    def sort(self) -> None: ...

class RecentFile:
    URI: str
    MimeType: str
    Timestamp: str
    Private: bool
    Groups: list[Incomplete]
    def __init__(self) -> None: ...
    def __cmp__(self, other: RecentFile) -> int: ...
    def __lt__(self, other: RecentFile) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
