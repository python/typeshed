from _typeshed import Incomplete
from typing import Dict, List, Optional, Union

from sagemaker.workflow.pipeline_context import _ModelStepArguments
from sagemaker.workflow.retry import RetryPolicy
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import Step

class ModelStep(StepCollection):
    name: Incomplete
    step_args: Incomplete
    depends_on: Incomplete
    retry_policies: Incomplete
    display_name: Incomplete
    description: Incomplete
    steps: Incomplete
    def __init__(
        self,
        name: str,
        step_args: _ModelStepArguments,
        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
        retry_policies: Optional[Union[List[RetryPolicy], Dict[str, List[RetryPolicy]]]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None: ...
