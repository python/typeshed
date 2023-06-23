from _typeshed import Incomplete
from typing import List

from sagemaker.workflow.entities import RequestType as RequestType

class SelectiveExecutionConfig:
    source_pipeline_execution_arn: Incomplete
    selected_steps: Incomplete
    def __init__(self, selected_steps: List[str], source_pipeline_execution_arn: str = None) -> None: ...
    def to_request(self) -> RequestType: ...
