import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

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
        s3_analysis_config_output_path: str | None = None,
        label: str | None = None,
        headers: list[str] | None = None,
        features: str | None = None,
        dataset_type: str = "text/csv",
        s3_compression_type: str = "None",
        joinsource: str | int | None = None,
        facet_dataset_uri: str | None = None,
        facet_headers: list[str] | None = None,
        predicted_label_dataset_uri: str | None = None,
        predicted_label_headers: list[str] | None = None,
        predicted_label: str | int | None = None,
        excluded_columns: list[int, list[str]] | None = None,
    ) -> None: ...
    def get_config(self): ...

class BiasConfig:
    analysis_config: Incomplete
    def __init__(
        self,
        label_values_or_threshold: int | float | str,
        facet_name: str | int | list[str, list[int]],
        facet_values_or_threshold: int | float | str | None = None,
        group_name: str | None = None,
    ) -> None: ...
    def get_config(self): ...

class ModelConfig:
    predictor_config: Incomplete
    def __init__(
        self,
        model_name: str | None = None,
        instance_count: int | None = None,
        instance_type: str | None = None,
        accept_type: str | None = None,
        content_type: str | None = None,
        content_template: str | None = None,
        record_template: str | None = None,
        custom_attributes: str | None = None,
        accelerator_type: str | None = None,
        endpoint_name_prefix: str | None = None,
        target_model: str | None = None,
        endpoint_name: str | None = None,
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
        label: str | int | None = None,
        probability: str | int | None = None,
        probability_threshold: float | None = None,
        label_headers: list[str] | None = None,
    ) -> None: ...
    def get_predictor_config(self): ...

class ExplainabilityConfig(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_explainability_config(self): ...

class PDPConfig(ExplainabilityConfig):
    pdp_config: Incomplete
    def __init__(self, features: list | None = None, grid_resolution: int = 15, top_k_features: int = 10) -> None: ...
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
        num_segments: int | None = None,
        feature_extraction_method: str | None = None,
        segment_compactness: float | None = None,
        max_objects: int | None = None,
        iou_threshold: float | None = None,
        context: float | None = None,
    ) -> None: ...
    def get_image_config(self): ...

class SHAPConfig(ExplainabilityConfig):
    shap_config: Incomplete
    def __init__(
        self,
        baseline: str | list | dict | None = None,
        num_samples: int | None = None,
        agg_method: str | None = None,
        use_logit: bool = False,
        save_local_shap_values: bool = True,
        seed: int | None = None,
        num_clusters: int | None = None,
        text_config: TextConfig | None = None,
        image_config: ImageConfig | None = None,
    ) -> None: ...
    def get_explainability_config(self): ...

class SageMakerClarifyProcessor(Processor):
    job_name_prefix: Incomplete
    skip_early_validation: Incomplete
    def __init__(
        self,
        role: str | None = None,
        instance_count: int | None = None,
        instance_type: str | None = None,
        volume_size_in_gb: int = 30,
        volume_kms_key: str | None = None,
        output_kms_key: str | None = None,
        max_runtime_in_seconds: int | None = None,
        sagemaker_session: Session | None = None,
        env: dict[str, str] | None = None,
        tags: list[dict[str, str]] | None = None,
        network_config: NetworkConfig | None = None,
        job_name_prefix: str | None = None,
        version: str | None = None,
        skip_early_validation: bool = False,
    ) -> None: ...
    def run(self, **_) -> None: ...
    def run_pre_training_bias(
        self,
        data_config: DataConfig,
        data_bias_config: BiasConfig,
        methods: str | list[str] = "all",
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        kms_key: str | None = None,
        experiment_config: dict[str, str] | None = None,
    ): ...
    def run_post_training_bias(
        self,
        data_config: DataConfig,
        data_bias_config: BiasConfig,
        model_config: ModelConfig | None = None,
        model_predicted_label_config: ModelPredictedLabelConfig | None = None,
        methods: str | list[str] = "all",
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        kms_key: str | None = None,
        experiment_config: dict[str, str] | None = None,
    ): ...
    def run_bias(
        self,
        data_config: DataConfig,
        bias_config: BiasConfig,
        model_config: ModelConfig | None = None,
        model_predicted_label_config: ModelPredictedLabelConfig | None = None,
        pre_training_methods: str | list[str] = "all",
        post_training_methods: str | list[str] = "all",
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        kms_key: str | None = None,
        experiment_config: dict[str, str] | None = None,
    ): ...
    def run_explainability(
        self,
        data_config: DataConfig,
        model_config: ModelConfig,
        explainability_config: ExplainabilityConfig | list,
        model_scores: int | str | ModelPredictedLabelConfig | None = None,
        wait: bool = True,
        logs: bool = True,
        job_name: str | None = None,
        kms_key: str | None = None,
        experiment_config: dict[str, str] | None = None,
    ): ...
    def run_bias_and_explainability(
        self,
        data_config: DataConfig,
        model_config: ModelConfig,
        explainability_config: ExplainabilityConfig | list[ExplainabilityConfig],
        bias_config: BiasConfig,
        pre_training_methods: str | list[str] = "all",
        post_training_methods: str | list[str] = "all",
        model_predicted_label_config: ModelPredictedLabelConfig | None = None,
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
        explainability_config: ExplainabilityConfig | list[ExplainabilityConfig],
        bias_config: BiasConfig,
        pre_training_methods: str | list[str] = "all",
        post_training_methods: str | list[str] = "all",
    ): ...
    @classmethod
    def explainability(
        cls,
        data_config: DataConfig,
        model_config: ModelConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        explainability_config: ExplainabilityConfig | list[ExplainabilityConfig],
    ): ...
    @classmethod
    def bias_pre_training(cls, data_config: DataConfig, bias_config: BiasConfig, methods: str | list[str]): ...
    @classmethod
    def bias_post_training(
        cls,
        data_config: DataConfig,
        bias_config: BiasConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        methods: str | list[str],
        model_config: ModelConfig,
    ): ...
    @classmethod
    def bias(
        cls,
        data_config: DataConfig,
        bias_config: BiasConfig,
        model_config: ModelConfig,
        model_predicted_label_config: ModelPredictedLabelConfig,
        pre_training_methods: str | list[str] = "all",
        post_training_methods: str | list[str] = "all",
    ): ...

class ProcessingOutputHandler:
    class S3UploadMode(Enum):
        CONTINUOUS: str
        ENDOFJOB: str
    @classmethod
    def get_s3_upload_mode(cls, analysis_config: dict[str, Any]) -> str: ...
