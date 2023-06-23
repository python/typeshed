from _typeshed import Incomplete
from datetime import datetime
from typing import Iterator, List, Optional

from sagemaker.apiutils import _base_types
from sagemaker.lineage import association
from sagemaker.lineage._api_types import ContextSummary
from sagemaker.lineage.action import Action
from sagemaker.lineage.artifact import Artifact
from sagemaker.lineage.lineage_trial_component import LineageTrialComponent
from sagemaker.lineage.query import LineageQueryDirectionEnum

class Context(_base_types.Record):
    context_arn: str
    context_name: str
    context_type: str
    properties: dict
    tags: list
    creation_time: datetime
    created_by: str
    last_modified_time: datetime
    last_modified_by: str
    def save(self) -> Context: ...
    def delete(self, disassociate: bool = False): ...
    def set_tag(self, tag: Incomplete | None = None): ...
    def set_tags(self, tags: Incomplete | None = None): ...
    @classmethod
    def load(cls, context_name: str, sagemaker_session: Incomplete | None = None) -> Context: ...
    @classmethod
    def create(
        cls,
        context_name: str = None,
        source_uri: str = None,
        source_type: str = None,
        context_type: str = None,
        description: str = None,
        properties: dict = None,
        tags: dict = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Context: ...
    @classmethod
    def list(
        cls,
        source_uri: Optional[str] = None,
        context_type: Optional[str] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Iterator[ContextSummary]: ...
    def actions(self, direction: LineageQueryDirectionEnum) -> List[Action]: ...

class EndpointContext(Context):
    def models(self) -> List[association.Association]: ...
    def models_v2(self, direction: LineageQueryDirectionEnum = ...) -> List[Artifact]: ...
    def dataset_artifacts(self, direction: LineageQueryDirectionEnum = ...) -> List[Artifact]: ...
    def training_job_arns(self, direction: LineageQueryDirectionEnum = ...) -> List[str]: ...
    def processing_jobs(self, direction: LineageQueryDirectionEnum = ...) -> List[LineageTrialComponent]: ...
    def transform_jobs(self, direction: LineageQueryDirectionEnum = ...) -> List[LineageTrialComponent]: ...
    def trial_components(self, direction: LineageQueryDirectionEnum = ...) -> List[LineageTrialComponent]: ...
    def pipeline_execution_arn(self, direction: LineageQueryDirectionEnum = ...) -> str: ...

class ModelPackageGroup(Context):
    def pipeline_execution_arn(self) -> str: ...
