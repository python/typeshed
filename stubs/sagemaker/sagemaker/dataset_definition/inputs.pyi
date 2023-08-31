from _typeshed import Incomplete

from sagemaker.apiutils._base_types import ApiObject

class RedshiftDatasetDefinition(ApiObject):
    def __init__(
        self,
        cluster_id: Incomplete | None = None,
        database: Incomplete | None = None,
        db_user: Incomplete | None = None,
        query_string: Incomplete | None = None,
        cluster_role_arn: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        kms_key_id: Incomplete | None = None,
        output_format: Incomplete | None = None,
        output_compression: Incomplete | None = None,
    ) -> None: ...

class AthenaDatasetDefinition(ApiObject):
    def __init__(
        self,
        catalog: Incomplete | None = None,
        database: Incomplete | None = None,
        query_string: Incomplete | None = None,
        output_s3_uri: Incomplete | None = None,
        work_group: Incomplete | None = None,
        kms_key_id: Incomplete | None = None,
        output_format: Incomplete | None = None,
        output_compression: Incomplete | None = None,
    ) -> None: ...

class DatasetDefinition(ApiObject):
    def __init__(
        self,
        data_distribution_type: str = "ShardedByS3Key",
        input_mode: str = "File",
        local_path: Incomplete | None = None,
        redshift_dataset_definition: Incomplete | None = None,
        athena_dataset_definition: Incomplete | None = None,
    ) -> None: ...

class S3Input(ApiObject):
    def __init__(
        self,
        s3_uri: Incomplete | None = None,
        local_path: Incomplete | None = None,
        s3_data_type: str = "S3Prefix",
        s3_input_mode: str = "File",
        s3_data_distribution_type: str = "FullyReplicated",
        s3_compression_type: Incomplete | None = None,
    ) -> None: ...
