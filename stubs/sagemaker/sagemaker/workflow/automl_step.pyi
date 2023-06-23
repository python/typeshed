from _typeshed import Incomplete
from typing import List, Optional, Union

from sagemaker.workflow.entities import RequestType as RequestType
from sagemaker.workflow.pipeline_context import _JobStepArguments
from sagemaker.workflow.retry import RetryPolicy
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import CacheConfig, ConfigurableRetryStep, Step

class AutoMLStep(ConfigurableRetryStep):
    step_args: Incomplete
    cache_config: Incomplete
    def __init__(
        self,
        name: str,
        step_args: _JobStepArguments,
        display_name: str = None,
        description: str = None,
        cache_config: CacheConfig = None,
        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
        retry_policies: List[RetryPolicy] = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self): ...
    def to_request(self) -> RequestType: ...
    def get_best_auto_ml_model(self, role, sagemaker_session: Incomplete | None = None): ...
