from _typeshed import Incomplete
from typing import Optional, Union

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
        model_statistics: Optional["MetricsSource"] = None,
        model_constraints: Optional["MetricsSource"] = None,
        model_data_statistics: Optional["MetricsSource"] = None,
        model_data_constraints: Optional["MetricsSource"] = None,
        bias: Optional["MetricsSource"] = None,
        explainability: Optional["MetricsSource"] = None,
        bias_pre_training: Optional["MetricsSource"] = None,
        bias_post_training: Optional["MetricsSource"] = None,
    ) -> None: ...

class MetricsSource:
    content_type: Incomplete
    s3_uri: Incomplete
    content_digest: Incomplete
    def __init__(
        self,
        content_type: str | PipelineVariable,
        s3_uri: str | PipelineVariable,
        content_digest: Optional[str | PipelineVariable] = None,
    ) -> None: ...

class FileSource:
    content_type: Incomplete
    s3_uri: Incomplete
    content_digest: Incomplete
    def __init__(
        self,
        s3_uri: str | PipelineVariable,
        content_digest: Optional[str | PipelineVariable] = None,
        content_type: Optional[str | PipelineVariable] = None,
    ) -> None: ...
