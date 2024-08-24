from _typeshed import Incomplete
from collections.abc import Callable
from types import TracebackType
from typing import Any
from typing_extensions import ParamSpecKwargs

from .models.segment import SegmentContextManager
from .models.subsegment import SubsegmentContextManager, subsegment_decorator
from .recorder import AWSXRayRecorder

class AsyncSegmentContextManager(SegmentContextManager):
    async def __aenter__(self): ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class AsyncSubsegmentContextManager(SubsegmentContextManager):
    @subsegment_decorator
    async def __call__(self, wrapped: Callable, instance, args: list[Any], kwargs: dict[str, Any]): ...
    async def __aenter__(self): ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class AsyncAWSXRayRecorder(AWSXRayRecorder):
    def capture_async(self, name: str | None = None): ...
    def in_segment_async(self, name: str | None = None, **segment_kwargs: ParamSpecKwargs): ...
    def in_subsegment_async(self, name: Incomplete | None = None, **subsegment_kwargs: ParamSpecKwargs): ...
    async def record_subsegment_async(
        self,
        wrapped: Callable,
        instance,
        args: list[Any],
        kwargs: dict[str, Any],
        name: str,
        namespace,
        meta_processor: Callable | Incomplete,
    ): ...
