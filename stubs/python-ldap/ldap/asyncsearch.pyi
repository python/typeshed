from typing import Any
from ldap import __version__ as __version__

SEARCH_RESULT_TYPES: set[int]
ENTRY_RESULT_TYPES: set[int]

class WrongResultType(Exception):

    receivedResultType: Any
    expectedResultTypes: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class AsyncSearchHandler:

    beginResultsDropped: int
    endResultBreak: int
    def __init__(self, l: Any) -> None: ...
    def startSearch(
        self,
        searchRoot: Any,
        searchScope: Any,
        filterStr: Any,
        attrList: Any = ...,
        attrsOnly: int = 0,
        timeout: int = -1,
        sizelimit: int = 0,
        serverctrls: Any = ...,
        clientctrls: Any = ...,
    ) -> None: ...
    def preProcessing(self) -> None: ...
    def afterFirstResult(self) -> None: ...
    def postProcessing(self) -> None: ...
    def processResults(self, ignoreResultsNumber: int = 0, processResultsCount: int = 0, timeout: int = -1) -> bool: ...

class List(AsyncSearchHandler):

    allResults: list[Any]
    def __init__(self, l: Any) -> None: ...

class Dict(AsyncSearchHandler):

    allEntries: dict[Any, Any]
    def __init__(self, l: Any) -> None: ...

class IndexedDict(Dict):

    indexed_attrs: Any
    index: Any
    def __init__(self, l: Any, indexed_attrs: Any = ...) -> None: ...

class FileWriter(AsyncSearchHandler):

    headerStr: str
    footerStr: str
    def __init__(self, l: Any, f: Any, headerStr: str = "", footerStr: str = "") -> None: ...
    def preProcessing(self) -> None: ...
    def postProcessing(self) -> None: ...

class LDIFWriter(FileWriter):
    def __init__(self, l: Any, writer_obj: Any, headerStr: str = "", footerStr: str = "") -> None: ...
