import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod

from sagemaker.workflow.steps import Step

PRIMITIVES: Incomplete
BINARY_CONDITION_TYPES: Incomplete

class LocalPipelineExecutor:
    sagemaker_session: Incomplete
    execution: Incomplete
    pipeline_dag: Incomplete
    local_sagemaker_client: Incomplete
    def __init__(self, execution, sagemaker_session) -> None: ...
    def execute(self): ...
    def evaluate_step_arguments(self, step): ...
    def evaluate_pipeline_variable(self, pipeline_variable, step_name): ...

class _StepExecutor(ABC, metaclass=abc.ABCMeta):
    pipline_executor: Incomplete
    step: Incomplete
    def __init__(self, pipeline_executor: LocalPipelineExecutor, step: Step) -> None: ...
    @abstractmethod
    def execute(self) -> dict: ...

class _TrainingStepExecutor(_StepExecutor):
    def execute(self): ...

class _ProcessingStepExecutor(_StepExecutor):
    def execute(self): ...

class _ConditionStepExecutor(_StepExecutor):
    def execute(self): ...

class _TransformStepExecutor(_StepExecutor):
    def execute(self): ...

class _CreateModelStepExecutor(_StepExecutor):
    def execute(self): ...

class _FailStepExecutor(_StepExecutor):
    def execute(self) -> None: ...

class _StepExecutorFactory:
    pipeline_executor: Incomplete
    def __init__(self, pipeline_executor: LocalPipelineExecutor) -> None: ...
    def get(self, step: Step) -> _StepExecutor: ...
