from _typeshed import Incomplete
from enum import Enum
from typing import List

from sagemaker.workflow.entities import DefaultEnumMeta, Entity, RequestType as RequestType

DEFAULT_BACKOFF_RATE: float
DEFAULT_INTERVAL_SECONDS: int
MAX_ATTEMPTS_CAP: int
MAX_EXPIRE_AFTER_MIN: int

class StepExceptionTypeEnum(Enum, metaclass=DefaultEnumMeta):
    SERVICE_FAULT: str
    THROTTLING: str

class SageMakerJobExceptionTypeEnum(Enum, metaclass=DefaultEnumMeta):
    INTERNAL_ERROR: str
    CAPACITY_ERROR: str
    RESOURCE_LIMIT: str

class RetryPolicy(Entity):
    backoff_rate: float
    interval_seconds: int
    max_attempts: int
    expire_after_mins: int
    def validate_backoff_rate(self, _, value) -> None: ...
    def validate_interval_seconds(self, _, value) -> None: ...
    def validate_max_attempts(self, _, value) -> None: ...
    def validate_expire_after_mins(self, _, value) -> None: ...
    def to_request(self) -> RequestType: ...
    def __init__(self, backoff_rate, interval_seconds, max_attempts, expire_after_mins) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class StepRetryPolicy(RetryPolicy):
    exception_types: Incomplete
    def __init__(
        self,
        exception_types: List[StepExceptionTypeEnum],
        backoff_rate: float = 2.0,
        interval_seconds: int = 1,
        max_attempts: int = None,
        expire_after_mins: int = None,
    ) -> None: ...
    def to_request(self) -> RequestType: ...
    def __hash__(self): ...

class SageMakerJobStepRetryPolicy(RetryPolicy):
    exception_type_list: Incomplete
    def __init__(
        self,
        exception_types: List[SageMakerJobExceptionTypeEnum] = None,
        failure_reason_types: List[SageMakerJobExceptionTypeEnum] = None,
        backoff_rate: float = 2.0,
        interval_seconds: int = 1,
        max_attempts: int = None,
        expire_after_mins: int = None,
    ) -> None: ...
    def to_request(self) -> RequestType: ...
    def __hash__(self): ...
