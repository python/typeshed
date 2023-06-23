from _typeshed import Incomplete
from typing import Union

from sagemaker.workflow.entities import Entity, Expression, RequestType as RequestType
from sagemaker.workflow.execution_variables import ExecutionVariable
from sagemaker.workflow.parameters import Parameter

class PipelineExperimentConfig(Entity):
    experiment_name: Incomplete
    trial_name: Incomplete
    def __init__(
        self,
        experiment_name: str | Parameter | ExecutionVariable | Expression,
        trial_name: str | Parameter | ExecutionVariable | Expression,
    ) -> None: ...
    def to_request(self) -> RequestType: ...

class PipelineExperimentConfigProperty(Expression):
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    @property
    def expr(self) -> RequestType: ...

class PipelineExperimentConfigProperties:
    EXPERIMENT_NAME: Incomplete
    TRIAL_NAME: Incomplete
