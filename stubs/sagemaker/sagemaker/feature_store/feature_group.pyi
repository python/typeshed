from _typeshed import Incomplete
from collections.abc import Sequence
from multiprocessing.pool import AsyncResult as AsyncResult
from typing import Any

from botocore.config import Config as Config
from pandas import DataFrame as DataFrame
from sagemaker.feature_store.feature_definition import FeatureDefinition, FeatureTypeEnum
from sagemaker.feature_store.inputs import DataCatalogConfig, DeletionModeEnum, FeatureParameter, FeatureValue, TableFormatEnum
from sagemaker.session import Session

logger: Incomplete

class AthenaQuery:
    catalog: str
    database: str
    table_name: str
    sagemaker_session: Session
    def run(self, query_string: str, output_location: str, kms_key: str | None = None, workgroup: str | None = None) -> str: ...
    def wait(self) -> None: ...
    def get_query_execution(self) -> dict[str, Any]: ...
    def as_dataframe(self) -> DataFrame: ...
    def __init__(
        self, catalog, database, table_name, sagemaker_session, current_query_execution_id, result_bucket, result_file_prefix
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class IngestionManagerPandas:
    feature_group_name: str
    sagemaker_fs_runtime_client_config: Config
    sagemaker_session: Session
    max_workers: int
    max_processes: int
    profile_name: str
    @property
    def failed_rows(self) -> list[int]: ...
    def wait(self, timeout: Incomplete | None = None) -> None: ...
    def run(self, data_frame: DataFrame, wait: bool = True, timeout: Incomplete | None = None): ...
    def __init__(
        self,
        feature_group_name,
        sagemaker_fs_runtime_client_config,
        sagemaker_session,
        max_workers,
        max_processes,
        profile_name,
        async_result,
        processing_pool,
        failed_indices,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class IngestionError(Exception):
    failed_rows: Incomplete
    message: Incomplete
    def __init__(self, failed_rows, message) -> None: ...

class FeatureGroup:
    name: str
    sagemaker_session: Session
    feature_definitions: Sequence[FeatureDefinition]
    DTYPE_TO_FEATURE_DEFINITION_CLS_MAP: dict[str, FeatureTypeEnum]
    def create(
        self,
        s3_uri: str | bool,
        record_identifier_name: str,
        event_time_feature_name: str,
        role_arn: str | None = None,
        online_store_kms_key_id: str | None = None,
        enable_online_store: bool = False,
        offline_store_kms_key_id: str | None = None,
        disable_glue_table_creation: bool = False,
        data_catalog_config: DataCatalogConfig | None = None,
        description: str | None = None,
        tags: list[dict[str, str]] | None = None,
        table_format: TableFormatEnum | None = None,
    ) -> dict[str, Any]: ...
    def delete(self) -> None: ...
    def describe(self, next_token: str | None = None) -> dict[str, Any]: ...
    def update(self, feature_additions: Sequence[FeatureDefinition]) -> dict[str, Any]: ...
    def update_feature_metadata(
        self,
        feature_name: str,
        description: str | None = None,
        parameter_additions: Sequence[FeatureParameter] | None = None,
        parameter_removals: Sequence[str] | None = None,
    ) -> dict[str, Any]: ...
    def describe_feature_metadata(self, feature_name: str) -> dict[str, Any]: ...
    def list_tags(self) -> Sequence[dict[str, str]]: ...
    def list_parameters_for_feature_metadata(self, feature_name: str) -> Sequence[dict[str, str]]: ...
    def load_feature_definitions(self, data_frame: DataFrame) -> Sequence[FeatureDefinition]: ...
    def get_record(
        self, record_identifier_value_as_string: str, feature_names: Sequence[str] | None = None
    ) -> Sequence[dict[str, str]]: ...
    def put_record(self, record: Sequence[FeatureValue]): ...
    def delete_record(self, record_identifier_value_as_string: str, event_time: str, deletion_mode: DeletionModeEnum = ...): ...
    def ingest(
        self,
        data_frame: DataFrame,
        max_workers: int = 1,
        max_processes: int = 1,
        wait: bool = True,
        timeout: float | None = None,
        profile_name: str | None = None,
    ) -> IngestionManagerPandas: ...
    def athena_query(self) -> AthenaQuery: ...
    def as_hive_ddl(self, database: str = "sagemaker_featurestore", table_name: str | None = None) -> str: ...
    def __init__(self, name, sagemaker_session, feature_definitions) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
