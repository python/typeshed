import collections
from _typeshed import Incomplete
from types import TracebackType
from typing import Any
from typing_extensions import Literal

def encode_text(s: str) -> bytes: ...

PDFDocEncoding: dict[int, str]

def decode_text(b: bytes) -> str: ...

class PdfFormatError(RuntimeError): ...

def check_format_condition(condition, error_message) -> None: ...

class IndirectReference:
    def __bytes__(self) -> bytes: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...

class IndirectObjectDef(IndirectReference): ...

class XrefTable:
    existing_entries: Any
    new_entries: Any
    deleted_entries: Any
    reading_finished: bool
    def __init__(self) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key): ...
    def __len__(self) -> int: ...
    def keys(self): ...
    def write(self, f): ...

class PdfName:
    name: Any
    def __init__(self, name) -> None: ...
    def name_as_str(self): ...
    def __eq__(self, other): ...
    def __hash__(self) -> int: ...
    @classmethod
    def from_pdf_stream(cls, data): ...
    allowed_chars: Any
    def __bytes__(self) -> bytes: ...

class PdfArray(list[Any]):
    def __bytes__(self) -> bytes: ...

class PdfDict(collections.UserDict[bytes, Any]):
    def __setattr__(self, key: str, value) -> None: ...
    def __getattr__(self, key: str): ...
    def __bytes__(self) -> bytes: ...

class PdfBinary:
    data: Any
    def __init__(self, data) -> None: ...
    def __bytes__(self) -> bytes: ...

class PdfStream:
    dictionary: Any
    buf: Any
    def __init__(self, dictionary, buf) -> None: ...
    def decode(self): ...

def pdf_repr(x: Any) -> bytes: ...

class PdfParser:
    filename: Any
    buf: Any
    f: Any
    start_offset: Any
    should_close_buf: bool
    should_close_file: bool
    cached_objects: Any
    file_size_total: int
    root: Any
    root_ref: Any
    info: Any
    info_ref: Any
    page_tree_root: Any
    pages: Any
    orig_pages: Any
    pages_ref: Any
    last_xref_section_offset: Any
    trailer_dict: Any
    xref_table: Any
    def __init__(
        self,
        filename: Incomplete | None = None,
        f: Incomplete | None = None,
        buf: Incomplete | None = None,
        start_offset: int = 0,
        mode: str = 'rb',
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> Literal[False]: ...
    def start_writing(self) -> None: ...
    def close_buf(self) -> None: ...
    def close(self) -> None: ...
    def seek_end(self) -> None: ...
    def write_header(self) -> None: ...
    def write_comment(self, s) -> None: ...
    def write_catalog(self): ...
    def rewrite_pages(self) -> None: ...
    def write_xref_and_trailer(self, new_root_ref: Incomplete | None = None) -> None: ...
    def write_page(self, ref, *objs, **dict_obj): ...
    def write_obj(self, ref, *objs, **dict_obj): ...
    def del_root(self) -> None: ...
    @staticmethod
    def get_buf_from_file(f): ...
    file_size_this: Any
    def read_pdf_info(self) -> None: ...
    def next_object_id(self, offset: Incomplete | None = None): ...
    delimiter: bytes
    delimiter_or_ws: bytes
    whitespace: bytes
    whitespace_or_hex: bytes
    whitespace_optional: Any
    whitespace_mandatory: Any
    whitespace_optional_no_nl: bytes
    newline_only: bytes
    newline: Any
    re_trailer_end: Any
    re_trailer_prev: Any
    def read_trailer(self) -> None: ...
    def read_prev_trailer(self, xref_section_offset) -> None: ...
    re_whitespace_optional: Any
    re_name: Any
    re_dict_start: Any
    re_dict_end: Any
    @classmethod
    def interpret_trailer(cls, trailer_data): ...
    re_hashes_in_name: Any
    @classmethod
    def interpret_name(cls, raw, as_text: bool = False): ...
    re_null: Any
    re_true: Any
    re_false: Any
    re_int: Any
    re_real: Any
    re_array_start: Any
    re_array_end: Any
    re_string_hex: Any
    re_string_lit: Any
    re_indirect_reference: Any
    re_indirect_def_start: Any
    re_indirect_def_end: Any
    re_comment: Any
    re_stream_start: Any
    re_stream_end: Any
    @classmethod
    def get_value(cls, data, offset, expect_indirect: Incomplete | None = None, max_nesting: int = -1): ...
    re_lit_str_token: Any
    escaped_chars: Any
    @classmethod
    def get_literal_string(cls, data, offset): ...
    re_xref_section_start: Any
    re_xref_subsection_start: Any
    re_xref_entry: Any
    def read_xref_table(self, xref_section_offset): ...
    def read_indirect(self, ref, max_nesting: int = -1): ...
    def linearize_page_tree(self, node: Incomplete | None = None): ...
