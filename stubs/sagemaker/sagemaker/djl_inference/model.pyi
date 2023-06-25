from _typeshed import Incomplete
from enum import Enum
from typing import Any
from collections.abc import Callable
from sagemaker.base_predictor import Predictor

from sagemaker.deserializers import BaseDeserializer
from sagemaker.model import FrameworkModel
from sagemaker.serializers import BaseSerializer
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

logger: Incomplete

class DJLServingEngineEntryPointDefaults(Enum):
    DEEPSPEED: Incomplete
    HUGGINGFACE_ACCELERATE: Incomplete
    STABLE_DIFFUSION: Incomplete
    FASTER_TRANSFORMER: Incomplete

class DJLPredictor(Predictor):
    def __init__(
        self,
        endpoint_name: str,
        sagemaker_session: Session | None = None,
        serializer: BaseSerializer = ...,
        deserializer: BaseDeserializer = ...,
    ) -> None: ...

class DJLModel(FrameworkModel):
    def __new__(cls, model_id: str, *args, **kwargs): ...
    model_id: Incomplete
    djl_version: Incomplete
    task: Incomplete
    dtype: Incomplete
    number_of_partitions: Incomplete
    min_workers: Incomplete
    max_workers: Incomplete
    job_queue_size: Incomplete
    parallel_loading: Incomplete
    model_loading_timeout: Incomplete
    prediction_timeout: Incomplete
    sagemaker_session: Incomplete
    save_mp_checkpoint_path: Incomplete
    def __init__(
        self,
        model_id: str,
        role: str,
        djl_version: str | None = None,
        task: str | None = None,
        dtype: str = "fp32",
        number_of_partitions: int | None = None,
        min_workers: int | None = None,
        max_workers: int | None = None,
        job_queue_size: int | None = None,
        parallel_loading: bool = False,
        model_loading_timeout: int | None = None,
        prediction_timeout: int | None = None,
        entry_point: str | None = None,
        image_uri: str | PipelineVariable | None = None,
        predictor_cls: Callable[[str, Session], Predictor] | Predictor = ...,
        **kwargs,
    ) -> None: ...
    def package_for_edge(self, **_) -> None: ...
    def compile(self, **_) -> None: ...
    def transformer(self, **_) -> None: ...
    def right_size(self, **_) -> None: ...
    image_uri: Incomplete
    def partition(
        self,
        instance_type: str,
        s3_output_uri: str | None = None,
        job_name: str | None = None,
        volume_kms_key: str | None = None,
        output_kms_key: str | None = None,
        use_spot_instances: bool = False,
        max_wait: int | None = None,
        enable_network_isolation: bool = False,
    ): ...
    def deploy(
        self,
        instance_type,
        initial_instance_count: int = 1,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        wait: bool = True,
        data_capture_config: Incomplete | None = None,
        volume_size: Incomplete | None = None,
        model_data_download_timeout: Incomplete | None = None,
        container_startup_health_check_timeout: Incomplete | None = None,
    ): ...
    def prepare_container_def(
        self,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
    ): ...
    def generate_serving_properties(self, serving_properties: Incomplete | None = None) -> dict[str, str]: ...
    def serving_image_uri(self, region_name): ...

class DeepSpeedModel(DJLModel):
    number_of_partitions: Incomplete
    max_tokens: Incomplete
    low_cpu_mem_usage: Incomplete
    enable_cuda_graph: Incomplete
    triangular_masking: Incomplete
    return_tuple: Incomplete
    save_mp_checkpoint_path: Incomplete
    checkpoint: Incomplete
    def __init__(
        self,
        model_id: str,
        role: str,
        tensor_parallel_degree: int | None = None,
        max_tokens: int | None = None,
        low_cpu_mem_usage: bool = False,
        enable_cuda_graph: bool = False,
        triangular_masking: bool = True,
        return_tuple: bool = True,
        **kwargs,
    ) -> None: ...
    def generate_serving_properties(self, serving_properties: Incomplete | None = None) -> dict[str, Any]: ...
    def partition(
        self,
        instance_type: str,
        s3_output_uri: str | None = None,
        job_name: str | None = None,
        volume_kms_key: str | None = None,
        output_kms_key: str | None = None,
        use_spot_instances: bool = False,
        max_wait: int | None = None,
        enable_network_isolation: bool = False,
    ): ...

class HuggingFaceAccelerateModel(DJLModel):
    device_id: Incomplete
    device_map: Incomplete
    load_in_8bit: Incomplete
    low_cpu_mem_usage: Incomplete
    def __init__(
        self,
        model_id: str,
        role: str,
        number_of_partitions: int | None = None,
        device_id: int | None = None,
        device_map: str | dict[str, str] | None = None,
        load_in_8bit: bool = False,
        low_cpu_mem_usage: bool = False,
        **kwargs,
    ) -> None: ...
    def generate_serving_properties(self, serving_properties: Incomplete | None = None) -> dict[str, str]: ...
    def partition(
        self,
        instance_type: str,
        s3_output_uri: str | None = None,
        job_name: str | None = None,
        volume_kms_key: str | None = None,
        output_kms_key: str | None = None,
        use_spot_instances: bool = False,
        max_wait: int | None = None,
        enable_network_isolation: bool = False,
    ): ...

class FasterTransformerModel(DJLModel):
    number_of_partitions: Incomplete
    def __init__(self, model_id: str, role: str, tensor_parallel_degree: int | None = None, **kwargs) -> None: ...
