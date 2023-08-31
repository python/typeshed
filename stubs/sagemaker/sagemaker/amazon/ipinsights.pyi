from _typeshed import Incomplete

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
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        num_entity_vectors: int | None = None,
        vector_dim: int | None = None,
        batch_metrics_publish_interval: int | None = None,
        epochs: int | None = None,
        learning_rate: float | None = None,
        num_ip_encoder_layers: int | None = None,
        random_negative_sampling_rate: int | None = None,
        shuffled_negative_sampling_rate: int | None = None,
        weight_decay: float | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class IPInsightsPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class IPInsightsModel(Model):
    def __init__(
        self, model_data: str | PipelineVariable, role: str | None = None, sagemaker_session: Session | None = None, **kwargs
    ) -> None: ...
