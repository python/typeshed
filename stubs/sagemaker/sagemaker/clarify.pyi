import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from sagemaker.network import NetworkConfig
from sagemaker.processing import Processor
from sagemaker.session import Session

logger: Incomplete
ENDPOINT_NAME_PREFIX_PATTERN: str
ANALYSIS_CONFIG_SCHEMA_V1_0: Incomplete

class DatasetType(Enum):
    TEXTCSV: str
    JSONLINES: str
    JSON: str
    PARQUET: str
    IMAGE: str

class DataConfig:
    s3_data_input_path: Incomplete
    s3_output_path: Incomplete
    s3_analysis_config_output_path: Incomplete
    s3_data_distribution_type: str
    s3_compression_type: Incomplete
    label: Incomplete
    headers: Incomplete
    features: Incomplete
    facet_dataset_uri: Incomplete
    facet_headers: Incomplete
    predicted_label_dataset_uri: Incomplete
    predicted_label_headers: Incomplete
    predicted_label: Incomplete
    excluded_columns: Incomplete
    analysis_config: Incomplete
    def __init__(
        self,
        s3_data_input_path: str,
        s3_output_path: str,
        s3_analysis_config_output_path: Optional[str] = None,
        label: Optional[str] = None,
        headers: Optional[List[str]] = None,
        features: Optional[str] = None,
        dataset_type: str = "text/csv",
        s3_compression_type: str = "None",
        joinsource: Optional[str | int] = None,
        facet_dataset_uri: Optional[str] = None,
        facet_headers: Optional[List[str]] = None,
        predicted_label_dataset_uri: Optional[str] = None,
        predicted_label_headers: Optional[List[str]] = None,
        predicted_label: Optional[str | int] = None,
        excluded_columns: Optional[List[int, List[str]]] = None,
    ) -> None: ...
    def get_config(self): ...

class BiasConfig:
    analysis_config: Incomplete
    def __init__(
        self,
        label_values_or_threshold: int | float | str,
        facet_name: str | int | List[str, List[int]],
        facet_values_or_threshold: Optional[int | float | str] = None,
        group_name: Optional[str] = None,
    ) -> None: ...
    def get_config(self): ...

class ModelConfig:
    predictor_config: Incomplete
    def __init__(
        self,
        model_name: Optional[str] = None,
        instance_count: Optional[int] = None,
        instance_type: Optional[str] = None,
        accept_type: Optional[str] = None,
        content_type: Optional[str] = None,
        content_template: Optional[str] = None,
        record_template: Optional[str] = None,
        custom_attributes: Optional[str] = None,
        accelerator_type: Optional[str] = None,
        endpoint_name_prefix: Optional[str] = None,
        target_model: Optional[str] = None,
        endpoint_name: Optional[str] = None,
    ) -> None: ...
    def get_predictor_config(self): ...

class ModelPredictedLabelConfig:
    label: Incomplete
    probability: Incomplete
    probability_threshold: Incomplete
    label_headers: Incomplete
    predictor_config: Incomplete
    def __init__(
        self,
        label: Optional[str | int] = None,
        probability: Optional[str | int] = None,
        probability_threshold: Optional[float] = None,
        label_headers: Optional[List[str]] = None,
    ) -> None: ...
    def get_predictor_config(self): ...

class ExplainabilityConfig(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_explainability_config(self): ...

class PDPConfig(ExplainabilityConfig):
    pdp_config: Incomplete
    def __init__(self, features: Optional[List] = None, grid_resolution: int = 15, top_k_features: int = 10) -> None: ...
    def get_explainability_config(self): ...

class TextConfig:
    text_config: Incomplete
    def __init__(self, granularity: str, language: str) -> None: ...
    def get_text_config(self): ...

class ImageConfig:
    image_config: Incomplete
    def __init__(
        self,
        model_type: str,
        num_segments: Optional[int] = None,
        feature_extraction_method: Optional[str] = None,
        segment_compactness: Optional[float] = None,
        max_objects: Optional[int] = None,
        iou_threshold: Optional[float] = None,
        context: Optional[float] = None,
    ) -> None: ...
    def get_image_config(self): ...

class SHAPConfig(ExplainabilityConfig):
    shap_config: Incomplete
    def __init__(
        self,
        baseline: Optional[str | List | Dict] = None,
        num_samples: Optional[int] = None,
        agg_method: Optional[str] = None,
        use_logit: bool = False,
        save_local_shap_values: bool = True,
        seed: Optional[int] = None,
        num_clusters: Optional[int] = None,
        text_config: Optional[TextConfig] = None,
        image_config: Optional[ImageConfig] = None,
    ) -> None: ...
    def get_explainability_config(self): ...

class SageMakerClarifyProcessor(Processor):
    job_name_prefix: Incomplete
    skip_early_validation: Incomplete
    def __init__(
        self,
        role: Optional[str] = None,
        instance_count: int = None,
        instance_type: str = None,
        volume_size_in_gb: int = 30,
        volume_kms_key: Optional[str] = None,
        output_kms_key: Optional[str] = None,
        max_runtime_in_seconds: Optional[int] = None,
        sagemaker_session: Optional[Session] = None,
        env: Optional[Dict[str, str]] = None,
        tags: Optional[List[Dict[str, str]]] = None,
        network_config: Optional[NetworkConfig] = None,
        job_name_prefix: Optional[str] = None,
        version: Optional[str] = None,
        skip_early_validation: bool = False,
    ) -> None: ...
    def run(self, **_) -> None: ...
    def run_pre_training_bias(
        self,
        data_config: DataConfig,
        data_bias_config: BiasConfig,
        methods: str | List[str] = "all",
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        kms_key: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
    ): ...
    def run_post_training_bias(
        self,
        data_config: DataConfig,
        data_bias_config: BiasConfig,
        model_config: Optional[ModelConfig] = None,
        model_predicted_label_config: Optional[ModelPredictedLabelConfig] = None,
        methods: str | List[str] = "all",
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        kms_key: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
    ): ...
    def run_bias(
        self,
        data_config: DataConfig,
        bias_config: BiasConfig,
        model_config: Optional[ModelConfig] = None,
        model_predicted_label_config: Optional[ModelPredictedLabelConfig] = None,
        pre_training_methods: str | List[str] = "all",
        post_training_methods: str | List[str] = "all",
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        kms_key: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
    ): ...
    def run_explainability(
        self,
        data_config: DataConfig,
        model_config: ModelConfig,
        explainability_config: ExplainabilityConfig | List,
        model_scores: Optional[int | str | ModelPredictedLabelConfig] = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        kms_key: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
    ): ...
    def run_bias_and_explainability(
        self,
        data_config: DataConfig,
        model_config: ModelConfig,
        explainability_config: ExplainabilityConfig | List[ExplainabilityConfig],
        bias_config: BiasConfig,
        pre_training_methods: str | List[str] = "all",
        post_training_methods: str | List[str] = "all",
        model_predicted_label_config: ModelPredictedLabelConfig = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        experiment_config: Incomplete | None = None,
    ): ...

class _AnalysisConfigGenerator:
    @classmethod
    def bias_and_explainability(
        cls,
        data_config: DataConfig,
        model_config: ModelConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        explainability_config: ExplainabilityConfig | List[ExplainabilityConfig],
        bias_config: BiasConfig,
        pre_training_methods: str | List[str] = "all",
        post_training_methods: str | List[str] = "all",
    ): ...
    @classmethod
    def explainability(
        cls,
        data_config: DataConfig,
        model_config: ModelConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        explainability_config: ExplainabilityConfig | List[ExplainabilityConfig],
    ): ...
    @classmethod
    def bias_pre_training(cls, data_config: DataConfig, bias_config: BiasConfig, methods: str | List[str]): ...
    @classmethod
    def bias_post_training(
        cls,
        data_config: DataConfig,
        bias_config: BiasConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        methods: str | List[str],
        model_config: ModelConfig,
    ): ...
    @classmethod
    def bias(
        cls,
        data_config: DataConfig,
        bias_config: BiasConfig,
        model_config: ModelConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        pre_training_methods: str | List[str] = "all",
        post_training_methods: str | List[str] = "all",
    ): ...

class ProcessingOutputHandler:
    class S3UploadMode(Enum):
        CONTINUOUS: str
        ENDOFJOB: str
    @classmethod
    def get_s3_upload_mode(cls, analysis_config: Dict[str, Any]) -> str: ...
