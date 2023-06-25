import abc
from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Optional

from sagemaker.estimator import EstimatorBase
from sagemaker.inputs import CreateModelInput, FileSystemInput, TrainingInput, TransformInput
from sagemaker.model import Model
from sagemaker.pipeline import PipelineModel
from sagemaker.processing import ProcessingInput, ProcessingOutput, Processor
from sagemaker.transformer import Transformer
from sagemaker.tuner import HyperparameterTuner
from sagemaker.workflow.entities import DefaultEnumMeta, Entity, RequestType as RequestType
from sagemaker.workflow.functions import Join
from sagemaker.workflow.pipeline_context import _JobStepArguments
from sagemaker.workflow.properties import PropertyFile
from sagemaker.workflow.retry import RetryPolicy

class StepTypeEnum(Enum, metaclass=DefaultEnumMeta):
    CONDITION: str
    CREATE_MODEL: str
    PROCESSING: str
    REGISTER_MODEL: str
    TRAINING: str
    TRANSFORM: str
    CALLBACK: str
    TUNING: str
    LAMBDA: str
    QUALITY_CHECK: str
    CLARIFY_CHECK: str
    EMR: str
    FAIL: str
    AUTOML: str

class Step(Entity, metaclass=abc.ABCMeta):
    name: str
    display_name: str | None
    description: str | None
    step_type: StepTypeEnum
    depends_on: list[str | "Step" | "StepCollection"] | None
    @property
    @abc.abstractmethod
    def arguments(self) -> RequestType: ...
    @property
    def step_only_arguments(self) -> RequestType: ...
    @property
    @abc.abstractmethod
    def properties(self): ...
    def to_request(self) -> RequestType: ...
    def add_depends_on(self, step_names: list[str | "Step" | "StepCollection"]): ...
    @property
    def ref(self) -> dict[str, str]: ...
    def __init__(self, name, display_name, description, step_type, depends_on) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class CacheConfig:
    enable_caching: bool
    expire_after: Incomplete
    @property
    def config(self): ...
    def __init__(self, enable_caching, expire_after) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ConfigurableRetryStep(Step, metaclass=abc.ABCMeta):
    retry_policies: Incomplete
    def __init__(
        self,
        name: str,
        step_type: StepTypeEnum,
        display_name: str | None = None,
        description: str | None = None,
        depends_on: list[str | Step | "StepCollection"] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
    ) -> None: ...
    def add_retry_policy(self, retry_policy: RetryPolicy): ...
    def to_request(self) -> RequestType: ...

class TrainingStep(ConfigurableRetryStep):
    step_args: Incomplete
    estimator: Incomplete
    inputs: Incomplete
    cache_config: Incomplete
    job_name: Incomplete
    def __init__(
        self,
        name: str,
        step_args: _JobStepArguments | None = None,
        estimator: EstimatorBase | None = None,
        display_name: str | None = None,
        description: str | None = None,
        inputs: TrainingInput | dict | str | FileSystemInput | None = None,
        cache_config: CacheConfig | None = None,
        depends_on: list[str | Step | "StepCollection"] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...

class CreateModelStep(ConfigurableRetryStep):
    step_args: Incomplete
    model: Incomplete
    inputs: Incomplete
    def __init__(
        self,
        name: str,
        step_args: dict | None = None,
        model: Model | PipelineModel | None = None,
        inputs: CreateModelInput | None = None,
        depends_on: list[str | Step | "StepCollection"] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
        display_name: str | None = None,
        description: str | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...

class TransformStep(ConfigurableRetryStep):
    step_args: Incomplete
    transformer: Incomplete
    inputs: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        step_args: _JobStepArguments | None = None,
        transformer: Transformer | None = None,
        inputs: TransformInput | None = None,
        display_name: str | None = None,
        description: str | None = None,
        cache_config: CacheConfig | None = None,
        depends_on: list[str | Step | "StepCollection"] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...

class ProcessingStep(ConfigurableRetryStep):
    step_args: Incomplete
    processor: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    job_arguments: Incomplete
    code: Incomplete
    property_files: Incomplete
    job_name: Incomplete
    kms_key: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        step_args: _JobStepArguments | None = None,
        processor: Processor | None = None,
        display_name: str | None = None,
        description: str | None = None,
        inputs: list[ProcessingInput] | None = None,
        outputs: list[ProcessingOutput] | None = None,
        job_arguments: list[str] | None = None,
        code: str | None = None,
        property_files: list[PropertyFile] | None = None,
        cache_config: CacheConfig | None = None,
        depends_on: list[str | Step | "StepCollection"] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
        kms_key: Incomplete | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...

class TuningStep(ConfigurableRetryStep):
    step_args: Incomplete
    tuner: Incomplete
    inputs: Incomplete
    job_arguments: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        step_args: _JobStepArguments | None = None,
        tuner: HyperparameterTuner | None = None,
        display_name: str | None = None,
        description: str | None = None,
        inputs: Incomplete | None = None,
        job_arguments: list[str] | None = None,
        cache_config: CacheConfig | None = None,
        depends_on: list[str | Step | "StepCollection"] | None = None,
        retry_policies: list[RetryPolicy] | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...
    def get_top_model_s3_uri(self, top_k: int, s3_bucket: str, prefix: str = "") -> Join: ...
