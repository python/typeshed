from _typeshed import Incomplete

class ClarifyTextConfig:
    language: Incomplete
    granularity: Incomplete
    def __init__(self, language: str, granularity: str) -> None: ...

class ClarifyShapBaselineConfig:
    mime_type: Incomplete
    shap_baseline: Incomplete
    shap_baseline_uri: Incomplete
    def __init__(
        self, mime_type: str | None = "text/csv", shap_baseline: str | None = None, shap_baseline_uri: str | None = None
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
        number_of_samples: int | None = None,
        seed: int | None = None,
        use_logit: bool | None = False,
        text_config: ClarifyTextConfig | None = None,
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
        feature_headers: list[str] | None = None,
        feature_types: list[str] | None = None,
        features_attribute: str | None = None,
        probability_index: int | None = None,
        probability_attribute: str | None = None,
        label_index: int | None = None,
        label_attribute: str | None = None,
        label_headers: list[str] | None = None,
        max_payload_in_mb: int | None = 6,
        max_record_count: int | None = None,
        content_template: str | None = None,
    ) -> None: ...

class ClarifyExplainerConfig:
    enable_explanations: Incomplete
    shap_config: Incomplete
    inference_config: Incomplete
    def __init__(
        self,
        shap_config: ClarifyShapConfig,
        enable_explanations: str | None = None,
        inference_config: ClarifyInferenceConfig | None = None,
    ) -> None: ...
