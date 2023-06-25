from _typeshed import Incomplete
from datetime import datetime
from typing import Optional
from collections.abc import Iterator

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
        cls, source_arn: str, destination_arn: str, association_type: str | None = None, sagemaker_session: Incomplete | None = None
    ) -> Association: ...
    @classmethod
    def list(
        cls,
        source_arn: str | None = None,
        destination_arn: str | None = None,
        source_type: str | None = None,
        destination_type: str | None = None,
        association_type: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> Iterator[AssociationSummary]: ...
