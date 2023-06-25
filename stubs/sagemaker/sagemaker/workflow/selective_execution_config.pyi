from _typeshed import Incomplete

from sagemaker.workflow.entities import RequestType as RequestType

class SelectiveExecutionConfig:
    source_pipeline_execution_arn: Incomplete
    selected_steps: Incomplete
    def __init__(self, selected_steps: list[str], source_pipeline_execution_arn: str | None = None) -> None: ...
    def to_request(self) -> RequestType: ...
