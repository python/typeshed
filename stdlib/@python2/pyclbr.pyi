from typing import Dict, List, Optional, Sequence, Union

class Class:
    module: str
    name: str
    super: Optional[List[Union[Class, str]]]
    methods: Dict[str, int]
    file: int
    lineno: int
    def __init__(self, module: str, name: str, super: Optional[List[Union[Class, str]]], file: str, lineno: int) -> None: ...

class Function:
    module: str
    name: str
    file: int
    lineno: int
    def __init__(self, module: str, name: str, file: str, lineno: int) -> None: ...

def readmodule(module: str, path: Sequence[str] | None = ...) -> Dict[str, Class]: ...
def readmodule_ex(module: str, path: Sequence[str] | None = ...) -> Dict[str, Class | Function | List[str]]: ...
