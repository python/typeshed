from _typeshed import Incomplete
from typing import List, Optional, Union

from sagemaker.workflow.entities import PipelineVariable, RequestType as RequestType
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import Step

class FailStep(Step):
    error_message: Incomplete
    def __init__(
        self,
        name: str,
        error_message: Union[str, PipelineVariable] = None,
        display_name: str = None,
        description: str = None,
        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def properties(self) -> None: ...
