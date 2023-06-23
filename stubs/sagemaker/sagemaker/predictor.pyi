from typing import Optional

from sagemaker.base_predictor import Predictor, PredictorBase as PredictorBase, RealTimePredictor as RealTimePredictor
from sagemaker.session import Session

def retrieve_default(
    endpoint_name: str,
    sagemaker_session: Optional[Session] = None,
    region: Optional[str] = None,
    model_id: Optional[str] = None,
    model_version: Optional[str] = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> Predictor: ...
