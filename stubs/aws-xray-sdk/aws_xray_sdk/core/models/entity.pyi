from _typeshed import Incomplete
from logging import Logger
from traceback import StackSummary
from typing import Any

from ..exceptions.exceptions import AlreadyEndedException as AlreadyEndedException
from ..utils.compat import annotation_value_types as annotation_value_types, string_types as string_types
from ..utils.conversion import metadata_to_dict as metadata_to_dict
from . import http as http
from .throwable import Throwable as Throwable

log: Logger
ORIGIN_TRACE_HEADER_ATTR_KEY: str

class Entity:
    id: Any
    name: Any
    start_time: Any
    parent_id: Any
    sampled: bool
    in_progress: bool
    http: Any
    annotations: Any
    metadata: Any
    aws: Any
    cause: Any
    subsegments: Any
    end_time: Any
    def __init__(self, name, entity_id: Incomplete | None = ...) -> None: ...
    def close(self, end_time: Incomplete | None = ...) -> None: ...
    def add_subsegment(self, subsegment) -> None: ...
    def remove_subsegment(self, subsegment) -> None: ...
    def put_http_meta(self, key, value) -> None: ...
    def put_annotation(self, key, value) -> None: ...
    def put_metadata(self, key, value, namespace: str = ...) -> None: ...
    def set_aws(self, aws_meta) -> None: ...
    throttle: bool
    def add_throttle_flag(self) -> None: ...
    fault: bool
    def add_fault_flag(self) -> None: ...
    error: bool
    def add_error_flag(self) -> None: ...
    def apply_status_code(self, status_code) -> None: ...
    def add_exception(self, exception: Exception, stack: StackSummary, remote: bool = ...) -> None: ...
    def save_origin_trace_header(self, trace_header) -> None: ...
    def get_origin_trace_header(self): ...
    def serialize(self): ...
    def to_dict(self): ...