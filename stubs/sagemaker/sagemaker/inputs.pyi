from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.workflow.entities import PipelineVariable

FILE_SYSTEM_TYPES: Incomplete
FILE_SYSTEM_ACCESS_MODES: Incomplete

class TrainingInput:
    config: Incomplete
    def __init__(
        self,
        s3_data: str | PipelineVariable,
        distribution: str | PipelineVariable | None = None,
        compression: str | PipelineVariable | None = None,
        content_type: str | PipelineVariable | None = None,
        record_wrapping: str | PipelineVariable | None = None,
        s3_data_type: str | PipelineVariable = "S3Prefix",
        instance_groups: list[str | PipelineVariable] | None = None,
        input_mode: str | PipelineVariable | None = None,
        attribute_names: list[str | PipelineVariable] | None = None,
        target_attribute_name: str | PipelineVariable | None = None,
        shuffle_config: Optional["ShuffleConfig"] = None,
    ) -> None: ...

class ShuffleConfig:
    seed: Incomplete
    def __init__(self, seed) -> None: ...

class CreateModelInput:
    instance_type: str
    accelerator_type: str
    def __init__(self, instance_type, accelerator_type) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class TransformInput:
    data: str
    data_type: str
    content_type: str
    compression_type: str
    split_type: str
    input_filter: str
    output_filter: str
    join_source: str
    model_client_config: dict
    batch_data_capture_config: dict
    def __init__(
        self,
        data,
        data_type,
        content_type,
        compression_type,
        split_type,
        input_filter,
        output_filter,
        join_source,
        model_client_config,
        batch_data_capture_config,
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class FileSystemInput:
    config: Incomplete
    def __init__(
        self,
        file_system_id,
        file_system_type,
        directory_path,
        file_system_access_mode: str = "ro",
        content_type: Incomplete | None = None,
    ) -> None: ...

class BatchDataCaptureConfig:
    destination_s3_uri: Incomplete
    kms_key_id: Incomplete
    generate_inference_id: Incomplete
    def __init__(self, destination_s3_uri: str, kms_key_id: str | None = None, generate_inference_id: bool | None = None) -> None: ...
