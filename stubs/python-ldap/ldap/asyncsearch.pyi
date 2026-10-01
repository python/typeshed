from _typeshed import Incomplete
from collections.abc import Iterable, Sequence
from typing import Any, TextIO

import ldap.ldapobject
import ldif
from ldap._types import LDAPEntryDict as LDAPEntryDict, LDAPSearchResult as LDAPSearchResult
from ldap.controls import RequestControl as RequestControl
from ldap.pkginfo import __version__ as __version__

SEARCH_RESULT_TYPES: Incomplete
ENTRY_RESULT_TYPES: Incomplete

class WrongResultType(Exception):
    receivedResultType: Incomplete
    expectedResultTypes: Incomplete
    def __init__(self, receivedResultType: int | None, expectedResultTypes: Iterable[int]) -> None: ...

class AsyncSearchHandler:
    def __init__(self, l: ldap.ldapobject.LDAPObject) -> None: ...
    def startSearch(
        self,
        searchRoot: str,
        searchScope: int,
        filterStr: str,
        attrList: list[str] | None = None,
        attrsOnly: int = 0,
        timeout: int = -1,
        sizelimit: int = 0,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> None: ...
    def preProcessing(self) -> Any: ...
    def afterFirstResult(self) -> Any: ...
    def postProcessing(self) -> Any: ...
    beginResultsDropped: int
    endResultBreak: Incomplete
    def processResults(self, ignoreResultsNumber: int = 0, processResultsCount: int = 0, timeout: int = -1) -> int: ...

class List(AsyncSearchHandler):
    allResults: list[tuple[int, LDAPSearchResult]]
    def __init__(self, l: ldap.ldapobject.LDAPObject) -> None: ...

class Dict(AsyncSearchHandler):
    allEntries: dict[str, LDAPEntryDict]
    def __init__(self, l: ldap.ldapobject.LDAPObject) -> None: ...

class IndexedDict(Dict):
    indexed_attrs: Incomplete
    index: dict[str, dict[bytes, list[str]]]
    def __init__(self, l: ldap.ldapobject.LDAPObject, indexed_attrs: Sequence[str] | None = None) -> None: ...

class FileWriter(AsyncSearchHandler):
    headerStr: Incomplete
    footerStr: Incomplete
    def __init__(self, l: ldap.ldapobject.LDAPObject, f: TextIO, headerStr: str = "", footerStr: str = "") -> None: ...
    def preProcessing(self) -> None: ...
    def postProcessing(self) -> None: ...

class LDIFWriter(FileWriter):
    def __init__(
        self, l: ldap.ldapobject.LDAPObject, writer_obj: TextIO | ldif.LDIFWriter, headerStr: str = "", footerStr: str = ""
    ) -> None: ...
