from typing import Dict, List, Optional, Union

from sagemaker.network import NetworkConfig
from sagemaker.processing import FrameworkProcessor
from sagemaker.pytorch.estimator import PyTorch
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class PyTorchProcessor(FrameworkProcessor):
    estimator_cls = PyTorch
    def __init__(
        self,
        framework_version: str,
        role: Optional[Union[str, PipelineVariable]] = None,
        instance_count: Union[int, PipelineVariable] = None,
        instance_type: Union[str, PipelineVariable] = None,
        py_version: str = "py3",
        image_uri: Optional[Union[str, PipelineVariable]] = None,
        command: Optional[List[str]] = None,
        volume_size_in_gb: Union[int, PipelineVariable] = 30,
        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
        code_location: Optional[str] = None,
        max_runtime_in_seconds: Optional[Union[int, PipelineVariable]] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
        network_config: Optional[NetworkConfig] = None,
    ) -> None: ...
