from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any

from sagemaker.session import Session
from sagemaker.workflow.entities import Entity, RequestType as RequestType
from sagemaker.workflow.parallelism_config import ParallelismConfiguration
from sagemaker.workflow.parameters import Parameter
from sagemaker.workflow.pipeline_experiment_config import PipelineExperimentConfig
from sagemaker.workflow.selective_execution_config import SelectiveExecutionConfig
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import Step

logger: Incomplete

class Pipeline(Entity):
    name: Incomplete
    parameters: Incomplete
    pipeline_experiment_config: Incomplete
    steps: Incomplete
    sagemaker_session: Incomplete
    def __init__(
        self,
        name: str = "",
        parameters: Sequence[Parameter] | None = None,
        pipeline_experiment_config: PipelineExperimentConfig | None = ...,
        steps: Sequence[Step | StepCollection] | None = None,
        sagemaker_session: Session | None = None,
    ) -> None: ...
    def to_request(self) -> RequestType: ...
    def create(
        self,
        role_arn: str | None = None,
        description: str | None = None,
        tags: list[dict[str, str]] | None = None,
        parallelism_config: ParallelismConfiguration | None = None,
    ) -> dict[str, Any]: ...
    def describe(self) -> dict[str, Any]: ...
    def update(
        self,
        role_arn: str | None = None,
        description: str | None = None,
        parallelism_config: ParallelismConfiguration | None = None,
    ) -> dict[str, Any]: ...
    def upsert(
        self,
        role_arn: str | None = None,
        description: str | None = None,
        tags: list[dict[str, str]] | None = None,
        parallelism_config: ParallelismConfiguration | None = None,
    ) -> dict[str, Any]: ...
    def delete(self) -> dict[str, Any]: ...
    def start(
        self,
        parameters: dict[str, str | bool | float] | None = None,
        execution_display_name: str | None = None,
        execution_description: str | None = None,
        parallelism_config: ParallelismConfiguration | None = None,
        selective_execution_config: SelectiveExecutionConfig | None = None,
    ): ...
    def definition(self) -> str: ...
    def list_executions(
        self,
        sort_by: str | None = None,
        sort_order: str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
    ) -> dict[str, Any]: ...

def format_start_parameters(parameters: dict[str, Any]) -> list[dict[str, Any]]: ...
def interpolate(
    request_obj: RequestType, callback_output_to_step_map: dict[str, str], lambda_output_to_step_map: dict[str, str]
) -> RequestType: ...
def update_args(args: dict[str, Any], **kwargs): ...

class _PipelineExecution:
    arn: str
    sagemaker_session: Session
    def stop(self): ...
    def describe(self): ...
    def list_steps(self): ...
    def wait(self, delay: int = 30, max_attempts: int = 60) -> None: ...
    def __init__(self, arn, sagemaker_session) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class PipelineGraph:
    step_map: Incomplete
    adjacency_list: Incomplete
    def __init__(self, steps: Sequence[Step | StepCollection]) -> None: ...
    @classmethod
    def from_pipeline(cls, pipeline: Pipeline): ...
    def is_cyclic(self) -> bool: ...
    def get_steps_in_sub_dag(self, current_step: Step | StepCollection, sub_dag_steps: set[str] | None = None) -> set[str]: ...
    stack: Incomplete
    def __iter__(self): ...
    def __next__(self) -> Step: ...
