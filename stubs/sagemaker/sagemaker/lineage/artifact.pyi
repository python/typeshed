from _typeshed import Incomplete
from collections.abc import Iterator
from datetime import datetime

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
    def upstream_trials(self) -> list: ...
    def set_tag(self, tag: Incomplete | None = None): ...
    def set_tags(self, tags: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        artifact_name: str | None = None,
        source_uri: str | None = None,
        source_types: list | None = None,
        artifact_type: str | None = None,
        properties: dict | None = None,
        tags: dict | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Artifact: ...
    @classmethod
    def list(
        cls,
        source_uri: str | None = None,
        artifact_type: str | None = None,
        created_before: datetime | None = None,
        created_after: datetime | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Iterator[ArtifactSummary]: ...
    def s3_uri_artifacts(self, s3_uri: str) -> dict: ...

class ModelArtifact(Artifact):
    def endpoints(self) -> list: ...
    def endpoint_contexts(self, direction: LineageQueryDirectionEnum = ...) -> list[Context]: ...
    def dataset_artifacts(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...
    def training_job_arns(self, direction: LineageQueryDirectionEnum = ...) -> list[str]: ...
    def pipeline_execution_arn(self, direction: LineageQueryDirectionEnum = ...) -> str: ...

class DatasetArtifact(Artifact):
    def trained_models(self) -> list[Association]: ...
    def endpoint_contexts(self, direction: LineageQueryDirectionEnum = ...) -> list[Context]: ...
    def upstream_datasets(self) -> list[Artifact]: ...
    def downstream_datasets(self) -> list[Artifact]: ...

class ImageArtifact(Artifact):
    def datasets(self, direction: LineageQueryDirectionEnum) -> list[Artifact]: ...
