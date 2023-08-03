import sys
from collections.abc import Callable, Mapping, Sequence
from types import ModuleType
from typing import Any, Protocol

from gevent.hub import Hub
from greenlet import greenlet as greenlet_t

# people that use mypy-zope and its mypy plugin should get correct type hints
# but for everyone else we shouldn't care whether or not we have type stubs
# it's not possible to correctly type hint Interface classes without a plugin
# for the interfaces needes by other modules we define an equivalent Protocol
# FIXME: unfortunately there does not seem to be any combination of error codes
# which will satisfy pyright, so we needed to use the sledge hammer approach
# of not specifying a error code at all...
from zope.interface import Interface, implementer  # type: ignore[import]  # pyright: ignore

# this is copied from types-psutil, it would be nice if we could just import this
# but it doesn't seem like we can...
if sys.platform == "linux":
    from psutil._pslinux import pmem
elif sys.platform == "darwin":
    from psutil._psosx import pmem
elif sys.platform == "win32":
    from psutil._pswindows import pmem
else:
    class pmem(Any): ...

subscribers: list[Callable[[Any], object]]

class _PeriodicMonitorThread(Protocol):
    def add_monitoring_function(self, function: Callable[[Hub], object], period: float | None) -> object: ...

class IPeriodicMonitorThread(Interface):  # pyright: ignore[reportUntypedBaseClass]
    def add_monitoring_function(function: Callable[[Hub], object], period: float | None) -> object: ...

class IPeriodicMonitorThreadStartedEvent(Interface):  # pyright: ignore[reportUntypedBaseClass]
    monitor: IPeriodicMonitorThread

@implementer(IPeriodicMonitorThread)  # pyright: ignore[reportUntypedClassDecorator]
class PeriodicMonitorThreadStartedEvent:
    ENTRY_POINT_NAME: str
    monitor: _PeriodicMonitorThread
    def __init__(self, monitor: _PeriodicMonitorThread) -> None: ...

class IEventLoopBlocked(Interface):  # pyright: ignore[reportUntypedBaseClass]
    greenlet: greenlet_t
    blocking_time: float
    info: Sequence[str]

@implementer(IEventLoopBlocked)  # pyright: ignore[reportUntypedClassDecorator]
class EventLoopBlocked:
    greenlet: greenlet_t
    blocking_time: float
    info: Sequence[str]
    def __init__(self, greenlet: greenlet_t, blocking_time: float, info: Sequence[str]) -> None: ...

class IMemoryUsageThresholdExceeded(Interface):  # pyright: ignore[reportUntypedBaseClass]
    mem_usage: int
    max_allowed: int
    memory_info: pmem

class _AbstractMemoryEvent:
    mem_usage: int
    max_allowed: int
    memory_info: pmem
    def __init__(self, mem_usage: int, max_allowed: int, memory_info: pmem) -> None: ...

@implementer(IMemoryUsageThresholdExceeded)  # pyright: ignore[reportUntypedClassDecorator]
class MemoryUsageThresholdExceeded(_AbstractMemoryEvent): ...

class IMemoryUsageUnderThreshold(Interface):  # pyright: ignore[reportUntypedBaseClass]
    mem_usage: int
    max_allowed: int
    max_memory_usage: int
    memory_info: pmem

@implementer(IMemoryUsageUnderThreshold)  # pyright: ignore[reportUntypedClassDecorator]
class MemoryUsageUnderThreshold(_AbstractMemoryEvent):
    max_memory_usage: int
    def __init__(self, mem_usage: int, max_allowed: int, memory_info: pmem, max_usage: int) -> None: ...

class IGeventPatchEvent(Interface):  # pyright: ignore[reportUntypedBaseClass]
    source: object
    target: object

@implementer(IGeventPatchEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventPatchEvent:
    source: object
    target: object
    def __init__(self, source: object, target: object) -> None: ...

class IGeventWillPatchEvent(IGeventPatchEvent): ...
class DoNotPatch(BaseException): ...

@implementer(IGeventWillPatchEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventWillPatchEvent(GeventPatchEvent): ...

class IGeventDidPatchEvent(IGeventPatchEvent): ...

@implementer(IGeventWillPatchEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventDidPatchEvent(GeventPatchEvent): ...

class IGeventWillPatchModuleEvent(IGeventWillPatchEvent):
    source: ModuleType
    target: ModuleType
    module_name: str
    target_item_names: list[str]

@implementer(IGeventWillPatchModuleEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventWillPatchModuleEvent(GeventWillPatchEvent):
    ENTRY_POINT_NAME: str
    source: ModuleType
    target: ModuleType
    module_name: str
    target_item_names: list[str]
    def __init__(self, module_name: str, source: ModuleType, target: ModuleType, items: list[str]) -> None: ...

class IGeventDidPatchModuleEvent(IGeventDidPatchEvent):
    source: ModuleType
    target: ModuleType
    module_name: str

@implementer(IGeventDidPatchModuleEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventDidPatchModuleEvent(GeventDidPatchEvent):
    ENTRY_POINT_NAME: str
    source: ModuleType
    target: ModuleType
    module_name: str
    def __init__(self, module_name: str, source: ModuleType, target: ModuleType) -> None: ...

class IGeventWillPatchAllEvent(IGeventWillPatchEvent):
    patch_all_arguments: Mapping[str, Any]
    patch_all_kwargs: Mapping[str, Any]
    def will_patch_module(module_name: str) -> bool: ...

class _PatchAllMixin:
    def __init__(self, patch_all_arguments: Mapping[str, Any], patch_all_kwargs: Mapping[str, Any]) -> None: ...
    @property
    def patch_all_arguments(self) -> dict[str, Any]: ...  # safe to mutate, it's a copy
    @property
    def patch_all_kwargs(self) -> dict[str, Any]: ...  # safe to mutate, it's a copy

@implementer(IGeventWillPatchAllEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventWillPatchAllEvent(_PatchAllMixin, GeventWillPatchEvent):
    ENTRY_POINT_NAME: str
    def will_patch_module(self, module_name: str) -> bool: ...

class IGeventDidPatchBuiltinModulesEvent(IGeventDidPatchEvent):
    patch_all_arguments: Mapping[str, Any]
    patch_all_kwargs: Mapping[str, Any]

@implementer(IGeventDidPatchBuiltinModulesEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventDidPatchBuiltinModulesEvent(_PatchAllMixin, GeventDidPatchEvent):
    ENTRY_POINT_NAME: str

class IGeventDidPatchAllEvent(IGeventDidPatchEvent): ...

@implementer(IGeventDidPatchAllEvent)  # pyright: ignore[reportUntypedClassDecorator]
class GeventDidPatchAllEvent(_PatchAllMixin, GeventDidPatchEvent):
    ENTRY_POINT_NAME: str
