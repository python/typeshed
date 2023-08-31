from _typeshed import Incomplete

from sagemaker.workflow.entities import PipelineVariable, RequestType as RequestType

class ExecutionVariable(PipelineVariable):
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def __eq__(self, other): ...
    def to_string(self) -> PipelineVariable: ...
    @property
    def expr(self) -> RequestType: ...

class ExecutionVariables:
    START_DATETIME: Incomplete
    CURRENT_DATETIME: Incomplete
    PIPELINE_NAME: Incomplete
    PIPELINE_ARN: Incomplete
    PIPELINE_EXECUTION_ID: Incomplete
    PIPELINE_EXECUTION_ARN: Incomplete
    TRAINING_JOB_NAME: Incomplete
    PROCESSING_JOB_NAME: Incomplete
