from typing import Any

class ModeDescriptor:
    mode: Any
    bands: Any
    basemode: Any
    basetype: Any
    def __init__(self, mode, bands, basemode, basetype, typestr) -> None: ...

def getmode(mode): ...
