from _typeshed import Incomplete
from datetime import datetime
from typing import Optional
from collections.abc import Iterator

from sagemaker.apiutils import _base_types
from sagemaker.lineage._api_types import ActionSource, ActionSummary
from sagemaker.lineage.artifact import Artifact
from sagemaker.lineage.query import LineageQueryDirectionEnum
from sagemaker.session import Session

class Action(_base_types.Record):
    action_arn: str
    action_name: str
    action_type: str
    description: str
    status: str
    source: ActionSource
    properties: dict
    properties_to_remove: list
    tags: list
    creation_time: datetime
    created_by: str
    last_modified_time: datetime
    last_modified_by: str
    def save(self) -> Action: ...
    def delete(self, disassociate: bool = False): ...
    @classmethod
    def load(cls, action_name: str, sagemaker_session: Incomplete | None = None) -> Action: ...
    def set_tag(self, tag: Incomplete | None = None): ...
    def set_tags(self, tags: Incomplete | None = None): ...
    @classmethod
    def create(
        cls,
        action_name: str | None = None,
        source_uri: str | None = None,
        source_type: str | None = None,
        action_type: str | None = None,
        description: str | None = None,
        status: str | None = None,
        properties: dict | None = None,
        tags: dict | None = None,
        sagemaker_session: Session | None = None,
    ) -> Action: ...
    @classmethod
    def list(
        cls,
        source_uri: str | None = None,
        action_type: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        sagemaker_session: Session | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
    ) -> Iterator[ActionSummary]: ...
    def artifacts(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...

class ModelPackageApprovalAction(Action):
    def datasets(self, direction: LineageQueryDirectionEnum = ...) -> list[Artifact]: ...
    def model_package(self): ...
    def endpoints(self, direction: LineageQueryDirectionEnum = ...) -> list: ...
