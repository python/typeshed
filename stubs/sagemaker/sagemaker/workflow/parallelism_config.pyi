from _typeshed import Incomplete

from sagemaker.workflow.entities import RequestType as RequestType

class ParallelismConfiguration:
    max_parallel_execution_steps: Incomplete
    def __init__(self, max_parallel_execution_steps: int) -> None: ...
    def to_request(self) -> RequestType: ...
