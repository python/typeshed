from _typeshed import Incomplete
from datetime import datetime
from typing import Iterator, List, Optional

from sagemaker.apiutils import _base_types
from sagemaker.lineage._api_types import ArtifactSource, ArtifactSummary
from sagemaker.lineage.association import Association
from sagemaker.lineage.context import Context
from sagemaker.lineage.query import LineageQueryDirectionEnum

LOGGER: Incomplete

class Artifact(_base_types.Record):
    artifact_arn: str
    artifact_name: str
    artifact_type: str
    source: ArtifactSource
    properties: dict
    tags: list
    creation_time: datetime
    created_by: str
    last_modified_time: datetime
    last_modified_by: str
    def save(self) -> Artifact: ...
    def delete(self, disassociate: bool = False): ...
    @classmethod
    def load(cls, artifact_arn: str, sagemaker_session: Incomplete | None = None) -> Artifact: ...
    def downstream_trials(self, sagemaker_session: Incomplete | None = None) -> list: ...
    def downstream_trials_v2(self) -> list: ...
    def upstream_trials(self) -> List: ...
    def set_tag(self, tag: Incomplete | None = None): ...
    def set_tags(self, tags: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        artifact_name: Optional[str] = None,
        source_uri: Optional[str] = None,
        source_types: Optional[list] = None,
        artifact_type: Optional[str] = None,
        properties: Optional[dict] = None,
        tags: Optional[dict] = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Artifact: ...
    @classmethod
    def list(
        cls,
        source_uri: Optional[str] = None,
        artifact_type: Optional[str] = None,
        created_before: Optional[datetime] = None,
        created_after: Optional[datetime] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Iterator[ArtifactSummary]: ...
    def s3_uri_artifacts(self, s3_uri: str) -> dict: ...

class ModelArtifact(Artifact):
    def endpoints(self) -> list: ...
    def endpoint_contexts(self, direction: LineageQueryDirectionEnum = ...) -> List[Context]: ...
    def dataset_artifacts(self, direction: LineageQueryDirectionEnum = ...) -> List[Artifact]: ...
    def training_job_arns(self, direction: LineageQueryDirectionEnum = ...) -> List[str]: ...
    def pipeline_execution_arn(self, direction: LineageQueryDirectionEnum = ...) -> str: ...

class DatasetArtifact(Artifact):
    def trained_models(self) -> List[Association]: ...
    def endpoint_contexts(self, direction: LineageQueryDirectionEnum = ...) -> List[Context]: ...
    def upstream_datasets(self) -> List[Artifact]: ...
    def downstream_datasets(self) -> List[Artifact]: ...

class ImageArtifact(Artifact):
    def datasets(self, direction: LineageQueryDirectionEnum) -> List[Artifact]: ...
