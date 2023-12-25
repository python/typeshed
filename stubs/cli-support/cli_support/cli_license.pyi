from _typeshed import Incomplete

from .cli_file_item_base import CliFileItemBase

class CliLicense(CliFileItemBase):
    CONTENT_TAG: str
    ACKNOWLEDGEMENTS_TAG: str
    TAGS_TAG: str
    license_text: str
    type: str
    name: str
    spdx_identifier: str
    acknowledgements: Incomplete
    tags: Incomplete
    files: Incomplete
    hashes: Incomplete
    def __init__(self) -> None: ...
