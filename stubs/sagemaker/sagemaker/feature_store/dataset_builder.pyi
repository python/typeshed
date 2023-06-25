import datetime
from enum import Enum
from typing import List, Tuple

import pandas as pd
from sagemaker.feature_store.feature_group import FeatureDefinition, FeatureGroup

class TableType(Enum):
    FEATURE_GROUP: str
    DATA_FRAME: str
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class JoinTypeEnum(Enum):
    INNER_JOIN: str
    LEFT_JOIN: str
    RIGHT_JOIN: str
    FULL_JOIN: str
    CROSS_JOIN: str
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class JoinComparatorEnum(Enum):
    EQUALS: str
    GREATER_THAN: str
    GREATER_THAN_OR_EQUAL_TO: str
    LESS_THAN: str
    LESS_THAN_OR_EQUAL_TO: str
    NOT_EQUAL_TO: str
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class FeatureGroupToBeMerged:
    features: list[str]
    included_feature_names: list[str]
    projected_feature_names: list[str]
    catalog: str
    database: str
    table_name: str
    record_identifier_feature_name: str
    event_time_identifier_feature: FeatureDefinition
    target_feature_name_in_base: str
    table_type: TableType
    feature_name_in_target: str
    join_comparator: JoinComparatorEnum
    join_type: JoinTypeEnum
    def __init__(
        self,
        features,
        included_feature_names,
        projected_feature_names,
        catalog,
        database,
        table_name,
        record_identifier_feature_name,
        event_time_identifier_feature,
        target_feature_name_in_base,
        table_type,
        feature_name_in_target,
        join_comparator,
        join_type,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def construct_feature_group_to_be_merged(
    target_feature_group: FeatureGroup,
    included_feature_names: list[str],
    target_feature_name_in_base: str | None = None,
    feature_name_in_target: str | None = None,
    join_comparator: JoinComparatorEnum = ...,
    join_type: JoinTypeEnum = ...,
) -> FeatureGroupToBeMerged: ...

class DatasetBuilder:
    def with_feature_group(
        self,
        feature_group: FeatureGroup,
        target_feature_name_in_base: str | None = None,
        included_feature_names: list[str] | None = None,
        feature_name_in_target: str | None = None,
        join_comparator: JoinComparatorEnum = ...,
        join_type: JoinTypeEnum = ...,
    ): ...
    def point_in_time_accurate_join(self): ...
    def include_duplicated_records(self): ...
    def include_deleted_records(self): ...
    def with_number_of_recent_records_by_record_identifier(self, number_of_recent_records: int): ...
    def with_number_of_records_from_query_results(self, number_of_records: int): ...
    def as_of(self, timestamp: datetime.datetime): ...
    def with_event_time_range(self, starting_timestamp: datetime.datetime | None = None, ending_timestamp: datetime.datetime | None = None): ...
    def to_csv_file(self) -> tuple[str, str]: ...
    def to_dataframe(self) -> tuple[pd.DataFrame, str]: ...
    def __init__(
        self,
        sagemaker_session,
        base,
        output_path,
        record_identifier_feature_name,
        event_time_identifier_feature_name,
        included_feature_names,
        kms_key_id,
        point_in_time_accurate_join,
        include_duplicated_records,
        include_deleted_records,
        number_of_recent_records,
        number_of_records,
        write_time_ending_timestamp,
        event_time_starting_timestamp,
        event_time_ending_timestamp,
        feature_groups_to_be_merged,
        event_time_identifier_feature_type,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
