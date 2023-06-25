from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.workflow.entities import PipelineVariable, RequestType as RequestType
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import Step

class FailStep(Step):
    error_message: Incomplete
    def __init__(
        self,
        name: str,
        error_message: str | PipelineVariable | None = None,
        display_name: str | None = None,
        description: str | None = None,
        depends_on: list[str | Step | StepCollection] | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self) -> None: ...
