from _typeshed import Incomplete
from typing import Dict, List, Optional

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
        depends_on: list[str | Step | StepCollection] | None = None,
        retry_policies: list[RetryPolicy, dict[str, list[RetryPolicy]]] | None = None,
        display_name: str | None = None,
        description: str | None = None,
    ) -> None: ...
