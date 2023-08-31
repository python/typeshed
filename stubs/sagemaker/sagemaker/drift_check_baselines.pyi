from _typeshed import Incomplete

from sagemaker.model_metrics import FileSource, MetricsSource

class DriftCheckBaselines:
    model_statistics: Incomplete
    model_constraints: Incomplete
    model_data_statistics: Incomplete
    model_data_constraints: Incomplete
    bias_config_file: Incomplete
    bias_pre_training_constraints: Incomplete
    bias_post_training_constraints: Incomplete
    explainability_constraints: Incomplete
    explainability_config_file: Incomplete
    def __init__(
        self,
        model_statistics: MetricsSource | None = None,
        model_constraints: MetricsSource | None = None,
        model_data_statistics: MetricsSource | None = None,
        model_data_constraints: MetricsSource | None = None,
        bias_config_file: FileSource | None = None,
        bias_pre_training_constraints: MetricsSource | None = None,
        bias_post_training_constraints: MetricsSource | None = None,
        explainability_constraints: MetricsSource | None = None,
        explainability_config_file: FileSource | None = None,
    ) -> None: ...
