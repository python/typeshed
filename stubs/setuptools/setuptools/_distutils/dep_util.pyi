from _typeshed import FileDescriptorOrPath, StrOrBytesPath, SupportsLenAndGetItem
from collections.abc import Iterable
from typing import Literal, TypeVar

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

def newer(source: StrOrBytesPath, target: FileDescriptorOrPath) -> bool: ...
def newer_pairwise(sources: SupportsLenAndGetItem[_T1], targets: SupportsLenAndGetItem[_T2]) -> tuple[list[_T1], list[_T2]]: ...
def newer_group(
    sources: Iterable[FileDescriptorOrPath], target: FileDescriptorOrPath, missing: Literal["error", "ignore", "newer"] = "error"
) -> bool: ...
