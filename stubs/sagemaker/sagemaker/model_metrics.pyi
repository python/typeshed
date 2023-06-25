from _typeshed import Incomplete

from sagemaker.workflow.entities import PipelineVariable

class ModelMetrics:
    model_statistics: Incomplete
    model_constraints: Incomplete
    model_data_statistics: Incomplete
    model_data_constraints: Incomplete
    bias: Incomplete
    bias_pre_training: Incomplete
    bias_post_training: Incomplete
    explainability: Incomplete
    def __init__(
        self,
        model_statistics: MetricsSource | None = None,
        model_constraints: MetricsSource | None = None,
        model_data_statistics: MetricsSource | None = None,
        model_data_constraints: MetricsSource | None = None,
        bias: MetricsSource | None = None,
        explainability: MetricsSource | None = None,
        bias_pre_training: MetricsSource | None = None,
        bias_post_training: MetricsSource | None = None,
    ) -> None: ...

class MetricsSource:
    content_type: Incomplete
    s3_uri: Incomplete
    content_digest: Incomplete
    def __init__(
        self,
        content_type: str | PipelineVariable,
        s3_uri: str | PipelineVariable,
        content_digest: str | PipelineVariable | None = None,
    ) -> None: ...

class FileSource:
    content_type: Incomplete
    s3_uri: Incomplete
    content_digest: Incomplete
    def __init__(
        self,
        s3_uri: str | PipelineVariable,
        content_digest: str | PipelineVariable | None = None,
        content_type: str | PipelineVariable | None = None,
    ) -> None: ...
