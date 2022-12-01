from _typeshed import Incomplete
from enum import Enum

class FileManagerType(Enum):
    regular: int
    select: int
    dir_only_uri: int
    show_item: int
    show_items: int
    win_select: int
    reveal: int
    dual_panel: int

class Platform(Enum):
    windows: int
    linux: int
    macos: int

single_file_only: Incomplete
cannot_open_uris: Incomplete
