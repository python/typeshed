from _typeshed import Incomplete
from typing import Optional

from sagemaker.workflow.entities import PipelineVariable

class MetadataProperties:
    commit_id: Incomplete
    repository: Incomplete
    generated_by: Incomplete
    project_id: Incomplete
    def __init__(
        self,
        commit_id: str | PipelineVariable | None = None,
        repository: str | PipelineVariable | None = None,
        generated_by: str | PipelineVariable | None = None,
        project_id: str | PipelineVariable | None = None,
    ) -> None: ...
