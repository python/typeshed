import datetime
from typing import Any, Dict, Sequence, Union

import pandas as pd
from sagemaker import Session
from sagemaker.feature_store.dataset_builder import DatasetBuilder
from sagemaker.feature_store.feature_group import FeatureGroup
from sagemaker.feature_store.inputs import Filter, Identifier, ResourceEnum, SearchOperatorEnum, SortOrderEnum

class FeatureStore:
    sagemaker_session: Session
    def create_dataset(
        self,
        base: Union[FeatureGroup, pd.DataFrame],
        output_path: str,
        record_identifier_feature_name: str = None,
        event_time_identifier_feature_name: str = None,
        included_feature_names: Sequence[str] = None,
        kms_key_id: str = None,
    ) -> DatasetBuilder: ...
    def list_feature_groups(
        self,
        name_contains: str = None,
        feature_group_status_equals: str = None,
        offline_store_status_equals: str = None,
        creation_time_after: datetime.datetime = None,
        creation_time_before: datetime.datetime = None,
        sort_order: str = None,
        sort_by: str = None,
        max_results: int = None,
        next_token: str = None,
    ) -> Dict[str, Any]: ...
    def batch_get_record(self, identifiers: Sequence[Identifier]) -> Dict[str, Any]: ...
    def search(
        self,
        resource: ResourceEnum,
        filters: Sequence[Filter] = None,
        operator: SearchOperatorEnum = None,
        sort_by: str = None,
        sort_order: SortOrderEnum = None,
        next_token: str = None,
        max_results: int = None,
    ) -> Dict[str, Any]: ...
    def __init__(self, sagemaker_session) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
