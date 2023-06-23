import abc
from _typeshed import Incomplete

logger: Incomplete
METRICS_PERIOD_DEFAULT: int

class AnalyticsMetricsBase(metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    def export_csv(self, filename) -> None: ...
    def dataframe(self, force_refresh: bool = False): ...
    def clear_cache(self) -> None: ...

class HyperparameterTuningJobAnalytics(AnalyticsMetricsBase):
    def __init__(self, hyperparameter_tuning_job_name, sagemaker_session: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    def clear_cache(self) -> None: ...
    @property
    def tuning_ranges(self): ...
    def description(self, force_refresh: bool = False): ...
    def training_job_summaries(self, force_refresh: bool = False): ...

class TrainingJobAnalytics(AnalyticsMetricsBase):
    CLOUDWATCH_NAMESPACE: str
    def __init__(
        self,
        training_job_name,
        metric_names: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        start_time: Incomplete | None = None,
        end_time: Incomplete | None = None,
        period: Incomplete | None = None,
    ) -> None: ...
    @property
    def name(self): ...
    def clear_cache(self) -> None: ...

class ArtifactAnalytics(AnalyticsMetricsBase):
    def __init__(
        self,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        source_uri: Incomplete | None = None,
        artifact_type: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> None: ...

class ExperimentAnalytics(AnalyticsMetricsBase):
    MAX_TRIAL_COMPONENTS: int
    def __init__(
        self,
        experiment_name: Incomplete | None = None,
        search_expression: Incomplete | None = None,
        sort_by: Incomplete | None = None,
        sort_order: Incomplete | None = None,
        metric_names: Incomplete | None = None,
        parameter_names: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
        input_artifact_names: Incomplete | None = None,
        output_artifact_names: Incomplete | None = None,
    ) -> None: ...
    @property
    def name(self): ...
    def clear_cache(self) -> None: ...
