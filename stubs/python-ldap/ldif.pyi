from typing import IO, Any

__all__ = ["ldif_pattern", "CreateLDIF", "ParseLDIF", "LDIFWriter", "LDIFParser", "LDIFRecordList", "LDIFCopy"]

ldif_pattern: str

class LDIFWriter:

    records_written: int
    def __init__(self, output_file: IO[str], base64_attrs: Any | None = None, cols: int = 76, line_sep: str = "\n") -> None: ...
    def unparse(self, dn: str, record: dict[str, list[bytes]] | list[Any]) -> None: ...
    def unparseChangeRecords(self, records: Any) -> None: ...

def CreateLDIF(dn: str, record: dict[str, list[bytes]] | list[Any], base64_attrs: Any | None = None, cols: int = 76) -> str: ...

class LDIFParser:

    version: int | None
    line_counter: int
    byte_counter: int
    records_read: int
    changetype_counter: dict[str, int]
    def __init__(
        self,
        input_file: IO[str],
        ignored_attr_types: Any | None = None,
        max_entries: int = 0,
        process_url_schemes: Any | None = None,
        line_sep: str = "\n",
    ) -> None: ...
    def handle(self, dn: str, entry: dict[str, list[bytes]]) -> None: ...
    def parse_entry_records(self) -> None: ...
    def parse(self) -> None: ...
    def handle_modify(self, dn: str, modops: list[tuple[int, str, list[bytes]]], controls: Any | None = None) -> None: ...
    def parse_change_records(self) -> None: ...

class LDIFRecordList(LDIFParser):

    all_records: list[tuple[str, dict[str, list[bytes]]]]
    all_modify_changes: list[tuple[str, list[tuple[int, str, list[bytes]]], Any]]
    def __init__(
        self,
        input_file: IO[str],
        ignored_attr_types: Any | None = None,
        max_entries: int = 0,
        process_url_schemes: Any | None = None,
    ) -> None: ...
    def handle(self, dn: str, entry: dict[str, list[bytes]]) -> None: ...
    def handle_modify(self, dn: str, modops: list[tuple[int, str, list[bytes]]], controls: Any | None = None) -> None: ...

class LDIFCopy(LDIFParser):
    def __init__(
        self,
        input_file: IO[str],
        output_file: IO[str],
        ignored_attr_types: Any | None = None,
        max_entries: int = 0,
        process_url_schemes: Any | None = None,
        base64_attrs: Any | None = None,
        cols: int = 76,
        line_sep: str = "\n",
    ) -> None: ...
    def handle(self, dn: str, entry: dict[str, list[bytes]]) -> None: ...

def ParseLDIF(f: IO[str], ignore_attrs: Any | None = None, maxentries: int = 0) -> list[tuple[str, dict[str, list[bytes]]]]: ...
