from collections.abc import Iterator
from typing import Any, NamedTuple

from . import exceptions as exceptions
from .snippets import findall_regex as findall_regex, split_by_regex as split_by_regex

class header(NamedTuple):
    index_path: str | None
    old_path: str
    old_version: str | None
    new_path: str
    new_version: str | None

class diffobj(NamedTuple):
    header: header | None
    changes: list[Change] | None
    text: str

class Change(NamedTuple):
    old: int | None
    new: int | None
    line: int | None
    hunk: int

file_timestamp_str: str
diffcmd_header: Any
unified_header_index: Any
unified_header_old_line: Any
unified_header_new_line: Any
unified_hunk_start: Any
unified_change: Any
context_header_old_line: Any
context_header_new_line: Any
context_hunk_start: Any
context_hunk_old: Any
context_hunk_new: Any
context_change: Any
ed_hunk_start: Any
ed_hunk_end: Any
rcs_ed_hunk_start: Any
default_hunk_start: Any
default_hunk_mid: Any
default_change: Any
git_diffcmd_header: Any
git_header_index: Any
git_header_old_line: Any
git_header_new_line: Any
git_header_file_mode: Any
git_header_binary_file: Any
bzr_header_index: Any
bzr_header_old_line: Any
bzr_header_new_line: Any
svn_header_index: Any
svn_header_timestamp_version: Any
svn_header_timestamp: Any
cvs_header_index: Any
cvs_header_rcs: Any
cvs_header_timestamp: Any
cvs_header_timestamp_colon: Any
old_cvs_diffcmd_header: Any

def parse_patch(text: str) -> Iterator[diffobj]: ...
def parse_header(text: str) -> header | None: ...
def parse_scm_header(text: str) -> header | None: ...
def parse_diff_header(text: str) -> header | None: ...
def parse_diff(text: str) -> list[Change] | None: ...
def parse_git_header(text: str) -> header | None: ...
def parse_svn_header(text: str) -> header | None: ...
def parse_cvs_header(text: str) -> header | None: ...
def parse_diffcmd_header(text: str) -> header | None: ...
def parse_unified_header(text: str) -> header | None: ...
def parse_context_header(text: str) -> header | None: ...
def parse_default_diff(text: str) -> list[Change] | None: ...
def parse_unified_diff(text: str) -> list[Change] | None: ...
def parse_context_diff(text: str) -> list[Change] | None: ...
def parse_ed_diff(text: str) -> list[Change] | None: ...
def parse_rcs_ed_diff(text: str) -> list[Change] | None: ...
