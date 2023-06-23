from _typeshed import Incomplete
from typing import Optional

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
        model_statistics: Optional[MetricsSource] = None,
        model_constraints: Optional[MetricsSource] = None,
        model_data_statistics: Optional[MetricsSource] = None,
        model_data_constraints: Optional[MetricsSource] = None,
        bias_config_file: Optional[FileSource] = None,
        bias_pre_training_constraints: Optional[MetricsSource] = None,
        bias_post_training_constraints: Optional[MetricsSource] = None,
        explainability_constraints: Optional[MetricsSource] = None,
        explainability_config_file: Optional[FileSource] = None,
    ) -> None: ...
