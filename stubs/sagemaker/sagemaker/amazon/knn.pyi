from _typeshed import Incomplete
from typing import Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class KNN(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    k: hp
    sample_size: hp
    predictor_type: hp
    dimension_reduction_target: hp
    dimension_reduction_type: hp
    index_metric: hp
    index_type: hp
    faiss_index_ivf_nlists: hp
    faiss_index_pq_m: hp
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        k: int | None = None,
        sample_size: int | None = None,
        predictor_type: str | None = None,
        dimension_reduction_type: str | None = None,
        dimension_reduction_target: int | None = None,
        index_type: str | None = None,
        index_metric: str | None = None,
        faiss_index_ivf_nlists: str | None = None,
        faiss_index_pq_m: int | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class KNNPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class KNNModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        sagemaker_session: Session | None = None,
        **kwargs,
    ) -> None: ...
