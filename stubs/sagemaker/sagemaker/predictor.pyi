from typing import Optional

from sagemaker.base_predictor import Predictor, PredictorBase as PredictorBase, RealTimePredictor as RealTimePredictor
from sagemaker.session import Session

def retrieve_default(
    endpoint_name: str,
    sagemaker_session: Session | None = None,
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> Predictor: ...
