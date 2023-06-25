import abc
from _typeshed import Incomplete
from typing import Any, Tuple

from sagemaker.deserializers import StreamDeserializer as StreamDeserializer, StringDeserializer as StringDeserializer

class PredictorBase(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def predict(self, *args, **kwargs) -> Any: ...
    @abc.abstractmethod
    def delete_predictor(self, *args, **kwargs) -> None: ...
    @property
    @abc.abstractmethod
    def content_type(self) -> str: ...
    @property
    @abc.abstractmethod
    def accept(self) -> tuple[str]: ...

class Predictor(PredictorBase):
    endpoint_name: Incomplete
    sagemaker_session: Incomplete
    serializer: Incomplete
    deserializer: Incomplete
    def __init__(
        self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=..., **kwargs
    ) -> None: ...
    def predict(
        self,
        data,
        initial_args: Incomplete | None = None,
        target_model: Incomplete | None = None,
        target_variant: Incomplete | None = None,
        inference_id: Incomplete | None = None,
    ): ...
    def update_endpoint(
        self,
        initial_instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        model_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        data_capture_config_dict: Incomplete | None = None,
        wait: bool = True,
    ) -> None: ...
    def delete_endpoint(self, delete_endpoint_config: bool = True) -> None: ...
    delete_predictor = delete_endpoint
    def delete_model(self) -> None: ...
    def enable_data_capture(self) -> None: ...
    def disable_data_capture(self) -> None: ...
    def update_data_capture_config(self, data_capture_config) -> None: ...
    def list_monitors(self): ...
    def endpoint_context(self): ...
    @property
    def content_type(self): ...
    @property
    def accept(self): ...
    @content_type.setter
    def content_type(self, val: str): ...
    @accept.setter
    def accept(self, val: str): ...
    @property
    def endpoint(self): ...

csv_serializer: Incomplete
json_serializer: Incomplete
npy_serializer: Incomplete
csv_deserializer: Incomplete
json_deserializer: Incomplete
numpy_deserializer: Incomplete
RealTimePredictor: Incomplete
