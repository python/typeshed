from _typeshed import Incomplete

from .xml_base import XmlBase

class CliFileItemBase(XmlBase):
    FILES_TAG: str
    FILEHASH_TAG: str
    files: Incomplete
    hashes: Incomplete
    def __init__(self) -> None: ...
