from typing import Dict, List, Optional

from sagemaker import Session
from sagemaker.network import NetworkConfig
from sagemaker.processing import ScriptProcessor
from sagemaker.workflow.entities import PipelineVariable

class SKLearnProcessor(ScriptProcessor):
    def __init__(
        self,
        framework_version: str,
        role: Optional[str | PipelineVariable] = None,
        instance_count: int | PipelineVariable = None,
        instance_type: str | PipelineVariable = None,
        command: Optional[List[str]] = None,
        volume_size_in_gb: int | PipelineVariable = 30,
        volume_kms_key: Optional[str | PipelineVariable] = None,
        output_kms_key: Optional[str | PipelineVariable] = None,
        max_runtime_in_seconds: Optional[int | PipelineVariable] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        env: Optional[Dict[str, str | PipelineVariable]] = None,
        tags: Optional[List[Dict[str, str | PipelineVariable]]] = None,
        network_config: Optional[NetworkConfig] = None,
    ) -> None: ...
