import _win32typing

def LoadPerfCounterTextStrings() -> None: ...
def UnloadPerfCounterTextStrings() -> None: ...
def CounterDefinition() -> _win32typing.PyPERF_COUNTER_DEFINITION: ...
def ObjectType() -> _win32typing.PyPERF_OBJECT_TYPE: ...
def PerfMonManager(
    serviceName: str,
    seqPerfObTypes: list[_win32typing.PyPERF_OBJECT_TYPE],
    mappingName: str | None = ...,
    eventSourceName: str | None = ...,
) -> _win32typing.PyPerfMonManager: ...
