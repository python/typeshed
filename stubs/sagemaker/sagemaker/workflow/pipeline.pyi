from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Sequence, Set, Union

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
        parameters: Optional[Sequence[Parameter]] = None,
        pipeline_experiment_config: Optional[PipelineExperimentConfig] = ...,
        steps: Optional[Sequence[Union[Step, StepCollection]]] = None,
        sagemaker_session: Optional[Session] = None,
    ) -> None: ...
    def to_request(self) -> RequestType: ...
    def create(
        self,
        role_arn: str = None,
        description: str = None,
        tags: List[Dict[str, str]] = None,
        parallelism_config: ParallelismConfiguration = None,
    ) -> Dict[str, Any]: ...
    def describe(self) -> Dict[str, Any]: ...
    def update(
        self, role_arn: str = None, description: str = None, parallelism_config: ParallelismConfiguration = None
    ) -> Dict[str, Any]: ...
    def upsert(
        self,
        role_arn: str = None,
        description: str = None,
        tags: List[Dict[str, str]] = None,
        parallelism_config: ParallelismConfiguration = None,
    ) -> Dict[str, Any]: ...
    def delete(self) -> Dict[str, Any]: ...
    def start(
        self,
        parameters: Dict[str, Union[str, bool, int, float]] = None,
        execution_display_name: str = None,
        execution_description: str = None,
        parallelism_config: ParallelismConfiguration = None,
        selective_execution_config: SelectiveExecutionConfig = None,
    ): ...
    def definition(self) -> str: ...
    def list_executions(
        self, sort_by: str = None, sort_order: str = None, max_results: int = None, next_token: str = None
    ) -> Dict[str, Any]: ...

def format_start_parameters(parameters: Dict[str, Any]) -> List[Dict[str, Any]]: ...
def interpolate(
    request_obj: RequestType, callback_output_to_step_map: Dict[str, str], lambda_output_to_step_map: Dict[str, str]
) -> RequestType: ...
def update_args(args: Dict[str, Any], **kwargs): ...

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
    def __init__(self, steps: Sequence[Union[Step, StepCollection]]) -> None: ...
    @classmethod
    def from_pipeline(cls, pipeline: Pipeline): ...
    def is_cyclic(self) -> bool: ...
    def get_steps_in_sub_dag(self, current_step: Union[Step, StepCollection], sub_dag_steps: Set[str] = None) -> Set[str]: ...
    stack: Incomplete
    def __iter__(self): ...
    def __next__(self) -> Step: ...
