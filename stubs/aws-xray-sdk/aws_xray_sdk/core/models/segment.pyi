from types import TracebackType
from typing import Any, ParamSpecKwargs

from ..recorder import AWSXRayRecorder
from ..utils.atomic_counter import AtomicCounter
from .entity import Entity
from .subsegment import Subsegment

ORIGIN_TRACE_HEADER_ATTR_KEY: str

class SegmentContextManager:
    name: str
    segment_kwargs: dict[str, Any]
    recorder: AWSXRayRecorder
    segment: Segment | None
    def __init__(self, recorder: AWSXRayRecorder, name: str | None = None, **segment_kwargs: ParamSpecKwargs) -> None: ...
    def __enter__(self) -> segment: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class Segment(Entity):
    trace_id: str | None
    id: str | None
    in_progress: bool
    sampled: bool
    user: str | None
    ref_counter: AtomicCounter
    parent_id: str | None
    service: dict[str, str]
    def __init__(
        self, name, entityid: str | None = None, traceid: str | None = None, parent_id: str | None = None, sampled: bool = True
    ) -> None: ...
    def add_subsegment(self, subsegment: Subsegment) -> None: ...
    def increment(self) -> None: ...
    def decrement_ref_counter(self) -> None: ...
    def ready_to_send(self) -> bool: ...
    def get_total_subsegments_size(self) -> int: ...
    def decrement_subsegments_size(self): ...
    def remove_subsegment(self, subsegment: Subsegment) -> None: ...
    def set_user(self, user) -> None: ...
    def set_service(self, service_info) -> None: ...
    def set_rule_name(self, rule_name) -> None: ...
    def to_dict(self) -> dict: ...
