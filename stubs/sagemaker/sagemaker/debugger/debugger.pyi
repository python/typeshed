from _typeshed import Incomplete
from abc import ABC

from sagemaker.workflow.entities import PipelineVariable

framework_name: str
DEBUGGER_FLAG: str

def get_rule_container_image_uri(region): ...
def get_default_profiler_rule(): ...

class RuleBase(ABC):
    name: Incomplete
    image_uri: Incomplete
    instance_type: Incomplete
    container_local_output_path: Incomplete
    s3_output_path: Incomplete
    volume_size_in_gb: Incomplete
    rule_parameters: Incomplete
    def __init__(
        self, name, image_uri, instance_type, container_local_output_path, s3_output_path, volume_size_in_gb, rule_parameters
    ) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class Rule(RuleBase):
    collection_configs: Incomplete
    actions: Incomplete
    def __init__(
        self,
        name,
        image_uri,
        instance_type,
        container_local_output_path,
        s3_output_path,
        volume_size_in_gb,
        rule_parameters,
        collections_to_save,
        actions: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def sagemaker(
        cls,
        base_config,
        name: Incomplete | None = None,
        container_local_output_path: Incomplete | None = None,
        s3_output_path: Incomplete | None = None,
        other_trials_s3_input_paths: Incomplete | None = None,
        rule_parameters: Incomplete | None = None,
        collections_to_save: Incomplete | None = None,
        actions: Incomplete | None = None,
    ): ...
    @classmethod
    def custom(
        cls,
        name: str,
        image_uri: str | PipelineVariable,
        instance_type: str | PipelineVariable,
        volume_size_in_gb: int | PipelineVariable,
        source: str | None = None,
        rule_to_invoke: str | PipelineVariable | None = None,
        container_local_output_path: str | PipelineVariable | None = None,
        s3_output_path: str | PipelineVariable | None = None,
        other_trials_s3_input_paths: list[str | PipelineVariable] | None = None,
        rule_parameters: dict[str, str | PipelineVariable] | None = None,
        collections_to_save: list[CollectionConfig] | None = None,
        actions: Incomplete | None = None,
    ): ...
    def prepare_actions(self, training_job_name) -> None: ...
    def to_debugger_rule_config_dict(self): ...

class ProfilerRule(RuleBase):
    @classmethod
    def sagemaker(
        cls,
        base_config,
        name: Incomplete | None = None,
        container_local_output_path: Incomplete | None = None,
        s3_output_path: Incomplete | None = None,
    ): ...
    @classmethod
    def custom(
        cls,
        name,
        image_uri,
        instance_type,
        volume_size_in_gb,
        source: Incomplete | None = None,
        rule_to_invoke: Incomplete | None = None,
        container_local_output_path: Incomplete | None = None,
        s3_output_path: Incomplete | None = None,
        rule_parameters: Incomplete | None = None,
    ): ...
    def to_profiler_rule_config_dict(self): ...

class DebuggerHookConfig:
    s3_output_path: Incomplete
    container_local_output_path: Incomplete
    hook_parameters: Incomplete
    collection_configs: Incomplete
    def __init__(
        self,
        s3_output_path: str | PipelineVariable | None = None,
        container_local_output_path: str | PipelineVariable | None = None,
        hook_parameters: dict[str, str | PipelineVariable] | None = None,
        collection_configs: list[CollectionConfig] | None = None,
    ) -> None: ...

class TensorBoardOutputConfig:
    s3_output_path: Incomplete
    container_local_output_path: Incomplete
    def __init__(
        self, s3_output_path: str | PipelineVariable, container_local_output_path: str | PipelineVariable | None = None
    ) -> None: ...

class CollectionConfig:
    name: Incomplete
    parameters: Incomplete
    def __init__(self, name: str | PipelineVariable, parameters: dict[str, str | PipelineVariable] | None = None) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
