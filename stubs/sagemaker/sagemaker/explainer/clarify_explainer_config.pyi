from _typeshed import Incomplete
from typing import List, Optional

class ClarifyTextConfig:
    language: Incomplete
    granularity: Incomplete
    def __init__(self, language: str, granularity: str) -> None: ...

class ClarifyShapBaselineConfig:
    mime_type: Incomplete
    shap_baseline: Incomplete
    shap_baseline_uri: Incomplete
    def __init__(
        self, mime_type: Optional[str] = "text/csv", shap_baseline: Optional[str] = None, shap_baseline_uri: Optional[str] = None
    ) -> None: ...

class ClarifyShapConfig:
    number_of_samples: Incomplete
    seed: Incomplete
    shap_baseline_config: Incomplete
    text_config: Incomplete
    use_logit: Incomplete
    def __init__(
        self,
        shap_baseline_config: ClarifyShapBaselineConfig,
        number_of_samples: Optional[int] = None,
        seed: Optional[int] = None,
        use_logit: Optional[bool] = False,
        text_config: Optional[ClarifyTextConfig] = None,
    ) -> None: ...

class ClarifyInferenceConfig:
    feature_headers: Incomplete
    feature_types: Incomplete
    features_attribute: Incomplete
    probability_index: Incomplete
    probability_attribute: Incomplete
    label_index: Incomplete
    label_attribute: Incomplete
    label_headers: Incomplete
    max_payload_in_mb: Incomplete
    max_record_count: Incomplete
    content_template: Incomplete
    def __init__(
        self,
        feature_headers: Optional[List[str]] = None,
        feature_types: Optional[List[str]] = None,
        features_attribute: Optional[str] = None,
        probability_index: Optional[int] = None,
        probability_attribute: Optional[str] = None,
        label_index: Optional[int] = None,
        label_attribute: Optional[str] = None,
        label_headers: Optional[List[str]] = None,
        max_payload_in_mb: Optional[int] = 6,
        max_record_count: Optional[int] = None,
        content_template: Optional[str] = None,
    ) -> None: ...

class ClarifyExplainerConfig:
    enable_explanations: Incomplete
    shap_config: Incomplete
    inference_config: Incomplete
    def __init__(
        self,
        shap_config: ClarifyShapConfig,
        enable_explanations: Optional[str] = None,
        inference_config: Optional[ClarifyInferenceConfig] = None,
    ) -> None: ...
