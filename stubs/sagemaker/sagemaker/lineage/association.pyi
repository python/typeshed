from _typeshed import Incomplete
from datetime import datetime
from typing import Iterator, Optional

from sagemaker.apiutils import _base_types
from sagemaker.lineage._api_types import AssociationSummary

logger: Incomplete

class Association(_base_types.Record):
    source_arn: str
    destination_arn: str
    def delete(self) -> None: ...
    def set_tag(self, tag: Incomplete | None = None): ...
    def set_tags(self, tags: Incomplete | None = None): ...
    @classmethod
    def create(
        cls, source_arn: str, destination_arn: str, association_type: str = None, sagemaker_session: Incomplete | None = None
    ) -> Association: ...
    @classmethod
    def list(
        cls,
        source_arn: str = None,
        destination_arn: str = None,
        source_type: str = None,
        destination_type: str = None,
        association_type: str = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Iterator[AssociationSummary]: ...
