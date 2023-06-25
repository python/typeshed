from _typeshed import Incomplete

from sagemaker import Model, Predictor, Session
from sagemaker.workflow.entities import PipelineVariable

framework_name: str

class SparkMLPredictor(Predictor):
    def __init__(self, endpoint_name, sagemaker_session: Incomplete | None = None, serializer=..., **kwargs) -> None: ...

class SparkMLModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        spark_version: str = "3.3",
        sagemaker_session: Session | None = None,
        **kwargs,
    ) -> None: ...
