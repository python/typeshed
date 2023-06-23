from _typeshed import Incomplete
from typing import Optional, Union

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
        role: Optional[Union[str, PipelineVariable]] = None,
        instance_count: Optional[Union[int, PipelineVariable]] = None,
        instance_type: Optional[Union[str, PipelineVariable]] = None,
        k: Optional[int] = None,
        sample_size: Optional[int] = None,
        predictor_type: Optional[str] = None,
        dimension_reduction_type: Optional[str] = None,
        dimension_reduction_target: Optional[int] = None,
        index_type: Optional[str] = None,
        index_metric: Optional[str] = None,
        faiss_index_ivf_nlists: Optional[str] = None,
        faiss_index_pq_m: Optional[int] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class KNNPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., deserializer=...) -> None: ...

class KNNModel(Model):
    def __init__(
        self,
        model_data: Union[str, PipelineVariable],
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
