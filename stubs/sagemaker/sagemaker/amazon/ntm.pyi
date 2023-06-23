from _typeshed import Incomplete
from typing import List, Optional, Union

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class NTM(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    num_topics: hp
    encoder_layers: hp
    epochs: hp
    encoder_layers_activation: hp
    optimizer: hp
    tolerance: hp
    num_patience_epochs: hp
    batch_norm: hp
    rescale_gradient: hp
    clip_gradient: hp
    weight_decay: hp
    learning_rate: hp
    def __init__(
        self,
        role: Optional[Union[str, PipelineVariable]] = None,
        instance_count: Optional[Union[int, PipelineVariable]] = None,
        instance_type: Optional[Union[str, PipelineVariable]] = None,
        num_topics: Optional[int] = None,
        encoder_layers: Optional[List] = None,
        epochs: Optional[int] = None,
        encoder_layers_activation: Optional[str] = None,
        optimizer: Optional[str] = None,
        tolerance: Optional[float] = None,
        num_patience_epochs: Optional[int] = None,
        batch_norm: Optional[bool] = None,
        rescale_gradient: Optional[float] = None,
        clip_gradient: Optional[float] = None,
        weight_decay: Optional[float] = None,
        learning_rate: Optional[float] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class NTMPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class NTMModel(Model):
    def __init__(
        self,
        model_data: Union[str, PipelineVariable],
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
