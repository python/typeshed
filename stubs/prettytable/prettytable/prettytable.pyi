from _typeshed import Incomplete
from html.parser import HTMLParser
from typing import Any

FRAME: int
ALL: int
NONE: int
HEADER: int
DEFAULT: int
MSWORD_FRIENDLY: int
PLAIN_COLUMNS: int
MARKDOWN: int
ORGMODE: int
RANDOM: int
SINGLE_BORDER: int
DOUBLE_BORDER: int
BASE_ALIGN_VALUE: str

class PrettyTable:
    encoding: Any
    def __init__(self, field_names: Any | None = ..., **kwargs): ...
    def __getattr__(self, name: str): ...
    def __getitem__(self, index): ...
    @property
    def field_names(self): ...
    @field_names.setter
    def field_names(self, val) -> None: ...
    @property
    def align(self): ...
    @align.setter
    def align(self, val) -> None: ...
    @property
    def valign(self): ...
    @valign.setter
    def valign(self, val) -> None: ...
    @property
    def max_width(self): ...
    @max_width.setter
    def max_width(self, val) -> None: ...
    @property
    def min_width(self): ...
    @min_width.setter
    def min_width(self, val) -> None: ...
    @property
    def min_table_width(self): ...
    @min_table_width.setter
    def min_table_width(self, val) -> None: ...
    @property
    def max_table_width(self): ...
    @max_table_width.setter
    def max_table_width(self, val) -> None: ...
    @property
    def fields(self): ...
    @fields.setter
    def fields(self, val) -> None: ...
    @property
    def title(self): ...
    @title.setter
    def title(self, val) -> None: ...
    @property
    def start(self): ...
    @start.setter
    def start(self, val) -> None: ...
    @property
    def end(self): ...
    @end.setter
    def end(self, val) -> None: ...
    @property
    def sortby(self): ...
    @sortby.setter
    def sortby(self, val) -> None: ...
    @property
    def reversesort(self): ...
    @reversesort.setter
    def reversesort(self, val) -> None: ...
    @property
    def sort_key(self): ...
    @sort_key.setter
    def sort_key(self, val) -> None: ...
    @property
    def header(self): ...
    @header.setter
    def header(self, val) -> None: ...
    @property
    def header_style(self): ...
    @header_style.setter
    def header_style(self, val) -> None: ...
    @property
    def border(self): ...
    @border.setter
    def border(self, val) -> None: ...
    @property
    def hrules(self): ...
    @hrules.setter
    def hrules(self, val) -> None: ...
    @property
    def vrules(self): ...
    @vrules.setter
    def vrules(self, val) -> None: ...
    @property
    def int_format(self): ...
    @int_format.setter
    def int_format(self, val) -> None: ...
    @property
    def float_format(self): ...
    @float_format.setter
    def float_format(self, val) -> None: ...
    @property
    def padding_width(self): ...
    @padding_width.setter
    def padding_width(self, val) -> None: ...
    @property
    def left_padding_width(self): ...
    @left_padding_width.setter
    def left_padding_width(self, val) -> None: ...
    @property
    def right_padding_width(self): ...
    @right_padding_width.setter
    def right_padding_width(self, val) -> None: ...
    @property
    def vertical_char(self): ...
    @vertical_char.setter
    def vertical_char(self, val) -> None: ...
    @property
    def horizontal_char(self): ...
    @horizontal_char.setter
    def horizontal_char(self, val) -> None: ...
    @property
    def junction_char(self): ...
    @junction_char.setter
    def junction_char(self, val) -> None: ...
    @property
    def format(self): ...
    @format.setter
    def format(self, val) -> None: ...
    @property
    def print_empty(self): ...
    @print_empty.setter
    def print_empty(self, val) -> None: ...
    @property
    def attributes(self): ...
    @attributes.setter
    def attributes(self, val) -> None: ...
    @property
    def oldsortslice(self): ...
    @oldsortslice.setter
    def oldsortslice(self, val) -> None: ...
    @property
    def bottom_junction_char(self): ...
    @bottom_junction_char.setter
    def bottom_junction_char(self, val) -> None: ...
    @property
    def bottom_left_junction_char(self): ...
    @bottom_left_junction_char.setter
    def bottom_left_junction_char(self, val) -> None: ...
    @property
    def bottom_right_junction_char(self): ...
    @bottom_right_junction_char.setter
    def bottom_right_junction_char(self, val) -> None: ...
    @property
    def custom_format(self): ...
    @custom_format.setter
    def custom_format(self, val) -> None: ...
    @property
    def horizontal_align_char(self): ...
    @horizontal_align_char.setter
    def horizontal_align_char(self, val) -> None: ...
    @property
    def left_junction_char(self): ...
    @left_junction_char.setter
    def left_junction_char(self, val) -> None: ...
    @property
    def none_format(self): ...
    @none_format.setter
    def none_format(self, val) -> None: ...
    @property
    def preserve_internal_border(self): ...
    @preserve_internal_border.setter
    def preserve_internal_border(self, val) -> None: ...
    @property
    def right_junction_char(self): ...
    @right_junction_char.setter
    def right_junction_char(self, val) -> None: ...
    @property
    def top_junction_char(self): ...
    @top_junction_char.setter
    def top_junction_char(self, val) -> None: ...
    @property
    def top_left_junction_char(self): ...
    @top_left_junction_char.setter
    def top_left_junction_char(self, val) -> None: ...
    @property
    def top_right_junction_char(self): ...
    @top_right_junction_char.setter
    def top_right_junction_char(self, val) -> None: ...
    @property
    def xhtml(self) -> bool: ...
    @xhtml.setter
    def xhtml(self, val: bool) -> None: ...
    @property
    def rows(self) -> list[Incomplete]: ...
    def add_autoindex(self, fieldname: str = ...): ...
    def get_latex_string(self, **kwargs) -> str: ...
    def set_style(self, style) -> None: ...
    def add_rows(self, rows) -> None: ...
    def add_row(self, row) -> None: ...
    def del_row(self, row_index) -> None: ...
    def add_column(self, fieldname, column, align: str = ..., valign: str = ...) -> None: ...
    def del_column(self, fieldname) -> None: ...
    def clear_rows(self) -> None: ...
    def clear(self) -> None: ...
    def copy(self): ...
    def get_string(self, **kwargs) -> str: ...
    def paginate(self, page_length: int = ..., line_break: str = ..., **kwargs): ...
    def get_csv_string(self, **kwargs) -> str: ...
    def get_json_string(self, **kwargs) -> str: ...
    def get_html_string(self, **kwargs) -> str: ...

def from_csv(fp, field_names: Any | None = ..., **kwargs): ...
def from_db_cursor(cursor, **kwargs): ...
def from_json(json_string, **kwargs): ...

class TableHandler(HTMLParser):
    kwargs: Any
    tables: Any
    last_row: Any
    rows: Any
    max_row_width: int
    active: Any
    last_content: str
    is_last_row_header: bool
    colspan: int
    def __init__(self, **kwargs) -> None: ...
    def handle_starttag(self, tag, attrs) -> None: ...
    def handle_endtag(self, tag) -> None: ...
    def handle_data(self, data) -> None: ...
    def generate_table(self, rows): ...
    def make_fields_unique(self, fields) -> None: ...

def from_html(html_code, **kwargs): ...
def from_html_one(html_code, **kwargs): ...
