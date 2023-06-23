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
        commit_id: Optional[str | PipelineVariable] = None,
        repository: Optional[str | PipelineVariable] = None,
        generated_by: Optional[str | PipelineVariable] = None,
        project_id: Optional[str | PipelineVariable] = None,
    ) -> None: ...
