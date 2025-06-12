from typing import TypedDict, type_check_only
from typing_extensions import TypeAlias

_SourceReferenceID: TypeAlias = int

@type_check_only
class Source(TypedDict, total=False):
    name: str
    path: str
    sourceReference: _SourceReferenceID

@type_check_only
class _LoadSourcesResult(TypedDict):
    sources: list[Source]

@type_check_only
class _SourceResult(TypedDict):
    content: str

def make_source(fullname: str, filename: str | None) -> Source: ...
def decode_source(source: Source) -> _SourceReferenceID: ...
def loaded_sources(**extra) -> _LoadSourcesResult: ...  # extra argument is unused
def source(
    *, source: Source | None = None, sourceReference: _SourceReferenceID, **extra
) -> _SourceResult: ...  # extra argument is unused
