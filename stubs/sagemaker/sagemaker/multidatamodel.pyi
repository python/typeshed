from _typeshed import Incomplete
from collections.abc import Generator
from typing import Optional

from sagemaker.model import Model
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

MULTI_MODEL_CONTAINER_MODE: str

class MultiDataModel(Model):
    name: Incomplete
    model_data_prefix: Incomplete
    model: Incomplete
    container_mode: Incomplete
    sagemaker_session: Incomplete
    endpoint_name: Incomplete
    s3_client: Incomplete
    def __init__(
        self,
        name: str,
        model_data_prefix: str,
        model: Optional[Model] = None,
        image_uri: Optional[str | PipelineVariable] = None,
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
    def prepare_container_def(
        self,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        serverless_inference_config: Incomplete | None = None,
    ): ...
    def deploy(
        self,
        initial_instance_count,
        instance_type,
        serializer: Incomplete | None = None,
        deserializer: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        endpoint_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        wait: bool = True,
        data_capture_config: Incomplete | None = None,
        **kwargs,
    ): ...
    def add_model(self, model_data_source, model_data_path: Incomplete | None = None): ...
    def list_models(self) -> Generator[Incomplete, None, None]: ...
