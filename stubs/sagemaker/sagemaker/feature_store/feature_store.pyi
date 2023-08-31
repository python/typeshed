import datetime
from collections.abc import Sequence
from typing import Any

import pandas as pd
from sagemaker import Session
from sagemaker.feature_store.dataset_builder import DatasetBuilder
from sagemaker.feature_store.feature_group import FeatureGroup
from sagemaker.feature_store.inputs import Filter, Identifier, ResourceEnum, SearchOperatorEnum, SortOrderEnum

class FeatureStore:
    sagemaker_session: Session
    def create_dataset(
        self,
        base: FeatureGroup | pd.DataFrame,
        output_path: str,
        record_identifier_feature_name: str | None = None,
        event_time_identifier_feature_name: str | None = None,
        included_feature_names: Sequence[str] | None = None,
        kms_key_id: str | None = None,
    ) -> DatasetBuilder: ...
    def list_feature_groups(
        self,
        name_contains: str | None = None,
        feature_group_status_equals: str | None = None,
        offline_store_status_equals: str | None = None,
        creation_time_after: datetime.datetime | None = None,
        creation_time_before: datetime.datetime | None = None,
        sort_order: str | None = None,
        sort_by: str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
    ) -> dict[str, Any]: ...
    def batch_get_record(self, identifiers: Sequence[Identifier]) -> dict[str, Any]: ...
    def search(
        self,
        resource: ResourceEnum,
        filters: Sequence[Filter] | None = None,
        operator: SearchOperatorEnum | None = None,
        sort_by: str | None = None,
        sort_order: SortOrderEnum | None = None,
        next_token: str | None = None,
        max_results: int | None = None,
    ) -> dict[str, Any]: ...
    def __init__(self, sagemaker_session) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
