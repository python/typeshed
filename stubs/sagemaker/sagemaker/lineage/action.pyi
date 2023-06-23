from _typeshed import Incomplete
from datetime import datetime
from typing import Iterator, List, Optional

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
        action_name: str = None,
        source_uri: str = None,
        source_type: str = None,
        action_type: str = None,
        description: str = None,
        status: str = None,
        properties: dict = None,
        tags: dict = None,
        sagemaker_session: Session = None,
    ) -> Action: ...
    @classmethod
    def list(
        cls,
        source_uri: Optional[str] = None,
        action_type: Optional[str] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        sagemaker_session: Session = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> Iterator[ActionSummary]: ...
    def artifacts(self, direction: LineageQueryDirectionEnum = ...) -> List[Artifact]: ...

class ModelPackageApprovalAction(Action):
    def datasets(self, direction: LineageQueryDirectionEnum = ...) -> List[Artifact]: ...
    def model_package(self): ...
    def endpoints(self, direction: LineageQueryDirectionEnum = ...) -> List: ...
