from _typeshed import Incomplete

from .cli_file_item_base import CliFileItemBase

class CliCopyright(CliFileItemBase):
    CONTENT_TAG: str
    text: str
    files: Incomplete
    hashes: Incomplete
    def __init__(self) -> None: ...
