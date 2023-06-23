from _typeshed import Incomplete
from typing import List, Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class RandomCutForest(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    MINI_BATCH_SIZE: int
    eval_metrics: hp
    num_trees: hp
    num_samples_per_tree: hp
    feature_dim: hp
    def __init__(
        self,
        role: Optional[str | PipelineVariable] = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        num_samples_per_tree: Optional[int] = None,
        num_trees: Optional[int] = None,
        eval_metrics: Optional[List] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class RandomCutForestPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class RandomCutForestModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
