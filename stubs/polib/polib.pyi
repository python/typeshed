from collections.abc import Callable
from typing import IO, Any, Generic, SupportsIndex, TypeVar, overload, Literal

_TB = TypeVar("_TB", bound=_BaseEntry)
_TP = TypeVar("_TP", bound=POFile)
_TM = TypeVar("_TM", bound=MOFile)

default_encoding: str

# wrapwidth: int
# encoding: str
# check_for_duplicates: bool
@overload
def pofile(pofile: str, *, klass: type[_TP], **kwargs: Any) -> _TP: ...
@overload
def pofile(pofile: str, **kwargs: Any) -> POFile: ...
@overload
def mofile(mofile: str, *, klass: type[_TM], **kwargs: Any) -> _TM: ...
@overload
def mofile(mofile: str, **kwargs: Any) -> MOFile: ...
def detect_encoding(file: bytes | str, binary_mode: bool = ...) -> str: ...
def escape(st: str) -> str: ...
def unescape(st: str) -> str: ...

class _BaseFile(list[_TB]):
    fpath: str
    wrapwidth: int
    encoding: str
    check_for_duplicates: bool
    header: str
    metadata: dict[str, str]
    metadata_is_fuzzy: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __unicode__(self) -> str: ...
    def __contains__(self, entry: _TB) -> bool: ...  # type: ignore[override]  # AttributeError otherwise
    def __eq__(self, other: object) -> bool: ...
    def append(self, entry: _TB) -> None: ...
    def insert(self, index: SupportsIndex, entry: _TB) -> None: ...
    def metadata_as_entry(self) -> POEntry: ...
    def save(self, fpath: str | None = ..., repr_method: str = ..., newline: str | None = ...) -> None: ...
    def find(self, st: str, by: str = ..., include_obsolete_entries: bool = ..., msgctxt: str | Literal[False] = ...) -> _TB | None: ...
    def ordered_metadata(self) -> list[tuple[str, str]]: ...
    def to_binary(self) -> bytes: ...

class POFile(_BaseFile[POEntry]):
    def __unicode__(self) -> str: ...
    def save_as_mofile(self, fpath: str) -> None: ...
    def percent_translated(self) -> int: ...
    def translated_entries(self) -> list[POEntry]: ...
    def untranslated_entries(self) -> list[POEntry]: ...
    def fuzzy_entries(self) -> list[POEntry]: ...
    def obsolete_entries(self) -> list[POEntry]: ...
    def merge(self, refpot: POFile) -> None: ...

class MOFile(_BaseFile[MOEntry]):
    MAGIC: int
    MAGIC_SWAPPED: int
    magic_number: int | None
    version: int
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save_as_pofile(self, fpath: str) -> None: ...
    def save(self, fpath: str | None = ...) -> None: ...  # type: ignore[override]  # binary file does not allow argument repr_method
    def percent_translated(self) -> int: ...
    def translated_entries(self) -> list[MOEntry]: ...
    def untranslated_entries(self) -> list[MOEntry]: ...
    def fuzzy_entries(self) -> list[MOEntry]: ...
    def obsolete_entries(self) -> list[MOEntry]: ...

class _BaseEntry:
    msgid: str
    msgstr: str
    msgid_plural: str
    msgstr_plural: dict[int, str]
    msgctxt: str
    obsolete: bool
    encoding: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __unicode__(self, wrapwidth: int = ...) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def msgid_with_context(self) -> str: ...

class POEntry(_BaseEntry):
    comment: str
    tcomment: str
    occurrences: list[tuple[str, str]]
    flags: list[str]
    previous_msgctxt: str | None
    previous_msgid: str | None
    previous_msgid_plural: str | None
    linenum: int | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __unicode__(self, wrapwidth: int = ...) -> str: ...
    def __cmp__(self, other: POEntry) -> int: ...
    def __gt__(self, other: POEntry) -> bool: ...
    def __lt__(self, other: POEntry) -> bool: ...
    def __ge__(self, other: POEntry) -> bool: ...
    def __le__(self, other: POEntry) -> bool: ...
    def __eq__(self, other: POEntry) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: POEntry) -> bool: ...  # type: ignore[override]
    def translated(self) -> bool: ...
    def merge(self, other: POEntry) -> None: ...
    @property
    def fuzzy(self) -> bool: ...
    @property
    def msgid_with_context(self) -> str: ...
    def __hash__(self) -> int: ...

class MOEntry(_BaseEntry):
    comment: str
    tcomment: str
    occurrences: list[tuple[str, str]]
    flags: list[str]
    previous_msgctxt: str | None
    previous_msgid: str | None
    previous_msgid_plural: str | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __hash__(self) -> int: ...

class _POFileParser(Generic[_TP]):
    fhandle: IO[str]
    instance: _TP
    transitions: dict[tuple[str, str], tuple[Callable[[], bool], str]]
    current_line: int
    current_entry: POEntry
    current_state: str
    current_token: str | None
    msgstr_index: int
    entry_obsolete: int
    def __init__(self, pofile: str, *args: Any, **kwargs: Any) -> None: ...
    def parse(self) -> _TP: ...
    def add(self, symbol: str, states: list[str], next_state: str) -> None: ...
    def process(self, symbol: str) -> None: ...
    def handle_he(self) -> bool: ...
    def handle_tc(self) -> bool: ...
    def handle_gc(self) -> bool: ...
    def handle_oc(self) -> bool: ...
    def handle_fl(self) -> bool: ...
    def handle_pp(self) -> bool: ...
    def handle_pm(self) -> bool: ...
    def handle_pc(self) -> bool: ...
    def handle_ct(self) -> bool: ...
    def handle_mi(self) -> bool: ...
    def handle_mp(self) -> bool: ...
    def handle_ms(self) -> bool: ...
    def handle_mx(self) -> bool: ...
    def handle_mc(self) -> bool: ...

class _MOFileParser(Generic[_TM]):
    fhandle: IO[bytes]
    instance: _TM
    def __init__(self, mofile: str, *args: Any, **kwargs: Any) -> None: ...
    def __del__(self) -> None: ...
    def parse(self) -> _TM: ...
