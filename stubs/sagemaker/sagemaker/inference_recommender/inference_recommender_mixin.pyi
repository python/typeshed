from _typeshed import Incomplete
from typing import Dict, List, Optional

from sagemaker.parameter import CategoricalParameter

INFERENCE_RECOMMENDER_FRAMEWORK_MAPPING: Incomplete
LOGGER: Incomplete

class Phase:
    to_json: Incomplete
    def __init__(self, duration_in_seconds: int, initial_number_of_users: int, spawn_rate: int) -> None: ...

class ModelLatencyThreshold:
    to_json: Incomplete
    def __init__(self, percentile: str, value_in_milliseconds: int) -> None: ...

class InferenceRecommenderMixin:
    inference_recommender_job_results: Incomplete
    inference_recommendations: Incomplete
    def right_size(
        self,
        sample_payload_url: str | None = None,
        supported_content_types: list[str] | None = None,
        supported_instance_types: list[str] | None = None,
        job_name: str | None = None,
        framework: str | None = None,
        job_duration_in_seconds: int | None = None,
        hyperparameter_ranges: list[dict[str, CategoricalParameter]] | None = None,
        phases: list[Phase] | None = None,
        traffic_type: str | None = None,
        max_invocations: int | None = None,
        model_latency_thresholds: list[ModelLatencyThreshold] | None = None,
        max_tests: int | None = None,
        max_parallel_tests: int | None = None,
        log_level: str | None = "Verbose",
    ): ...
