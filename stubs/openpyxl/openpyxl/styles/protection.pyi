from openpyxl.descriptors.serialisable import Serialisable

class Protection(Serialisable):
    tagname: str
    locked: bool
    hidden: bool
    def __init__(self, locked: bool = ..., hidden: bool = ...) -> None: ...
