from _typeshed import Incomplete
from typing import List, Optional

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
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        num_topics: int | None = None,
        encoder_layers: list | None = None,
        epochs: int | None = None,
        encoder_layers_activation: str | None = None,
        optimizer: str | None = None,
        tolerance: float | None = None,
        num_patience_epochs: int | None = None,
        batch_norm: bool | None = None,
        rescale_gradient: float | None = None,
        clip_gradient: float | None = None,
        weight_decay: float | None = None,
        learning_rate: float | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class NTMPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class NTMModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        sagemaker_session: Session | None = None,
        **kwargs,
    ) -> None: ...
