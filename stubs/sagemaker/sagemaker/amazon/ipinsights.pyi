from _typeshed import Incomplete
from typing import Optional, Union

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class IPInsights(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    MINI_BATCH_SIZE: int
    num_entity_vectors: hp
    vector_dim: hp
    batch_metrics_publish_interval: hp
    epochs: hp
    learning_rate: hp
    num_ip_encoder_layers: hp
    random_negative_sampling_rate: hp
    shuffled_negative_sampling_rate: hp
    weight_decay: hp
    def __init__(
        self,
        role: Optional[str | PipelineVariable] = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        num_entity_vectors: Optional[int] = None,
        vector_dim: Optional[int] = None,
        batch_metrics_publish_interval: Optional[int] = None,
        epochs: Optional[int] = None,
        learning_rate: Optional[float] = None,
        num_ip_encoder_layers: Optional[int] = None,
        random_negative_sampling_rate: Optional[int] = None,
        shuffled_negative_sampling_rate: Optional[int] = None,
        weight_decay: Optional[float] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class IPInsightsPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class IPInsightsModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
