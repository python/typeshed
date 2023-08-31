from _typeshed import Incomplete

from sagemaker.workflow.conditions import Condition
from sagemaker.workflow.entities import RequestType as RequestType
from sagemaker.workflow.functions import JsonGet as NewJsonGet
from sagemaker.workflow.properties import PropertyFile
from sagemaker.workflow.step_collections import StepCollection
from sagemaker.workflow.steps import Step

class ConditionStep(Step):
    conditions: Incomplete
    if_steps: Incomplete
    else_steps: Incomplete
    def __init__(
        self,
        name: str,
        depends_on: list[str | Step | StepCollection] | None = None,
        display_name: str | None = None,
        description: str | None = None,
        conditions: list[Condition] | None = None,
        if_steps: list[Step | StepCollection] | None = None,
        else_steps: list[Step | StepCollection] | None = None,
    ) -> None: ...
    @property
    def arguments(self) -> RequestType: ...
    @property
    def step_only_arguments(self): ...
    @property
    def properties(self): ...

class JsonGet(NewJsonGet):
    def __init__(self, step: Step, property_file: PropertyFile | str, json_path: str) -> None: ...
