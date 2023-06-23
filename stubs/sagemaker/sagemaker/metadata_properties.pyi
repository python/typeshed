from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.workflow.entities import PipelineVariable

class MetadataProperties:
    commit_id: Incomplete
    repository: Incomplete
    generated_by: Incomplete
    project_id: Incomplete
    def __init__(
        self,
        commit_id: Optional[Union[str, PipelineVariable]] = None,
        repository: Optional[Union[str, PipelineVariable]] = None,
        generated_by: Optional[Union[str, PipelineVariable]] = None,
        project_id: Optional[Union[str, PipelineVariable]] = None,
    ) -> None: ...
