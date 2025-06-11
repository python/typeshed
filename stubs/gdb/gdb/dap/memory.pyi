from typing import TypedDict, type_check_only

@type_check_only
class _ReadMemoryResult(TypedDict):
    address: str
    data: str

def read_memory(
    *, memoryReference: str, offset: int = 0, count: int, **extra
) -> _ReadMemoryResult: ...  #  extra argument is unused
def write_memory(*, memoryReference: str, offset: int = 0, data: str, **extra): ...  #  extra argument is unused
