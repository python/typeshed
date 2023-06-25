from _typeshed import Incomplete
from collections.abc import Iterator
from datetime import datetime

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
        context_name: str | None = None,
        source_uri: str | None = None,
        source_type: str | None = None,
        context_type: str | None = None,
        description: str | None = None,
        properties: dict | None = None,
        tags: dict | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Context: ...
    @classmethod
    def list(
        cls,
        source_uri: str | None = None,
        context_type: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Iterator[ContextSummary]: ...
    def actions(self, direction: LineageQueryDirectionEnum) -> list[Action]: ...

class EndpointContext(Context):
    def models(self) -> list[association.Association]: ...
    def models_v2(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...
    def dataset_artifacts(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...
    def training_job_arns(self, direction: LineageQueryDirectionEnum = ...) -> list[str]: ...
    def processing_jobs(self, direction: LineageQueryDirectionEnum = ...) -> list[LineageTrialComponent]: ...
    def transform_jobs(self, direction: LineageQueryDirectionEnum = ...) -> list[LineageTrialComponent]: ...
    def trial_components(self, direction: LineageQueryDirectionEnum = ...) -> list[LineageTrialComponent]: ...
    def pipeline_execution_arn(self, direction: LineageQueryDirectionEnum = ...) -> str: ...

class ModelPackageGroup(Context):
    def pipeline_execution_arn(self) -> str: ...
