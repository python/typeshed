import enum
from _typeshed import Incomplete

logger: Incomplete
HEALTH_CHECK_TIMEOUT_LIMIT: int

class _LocalProcessingJob:
    container: Incomplete
    state: str
    start_time: Incomplete
    end_time: Incomplete
    processing_job_name: str
    processing_inputs: Incomplete
    processing_output_config: Incomplete
    environment: Incomplete
    def __init__(self, container) -> None: ...
    def start(self, processing_inputs, processing_output_config, environment, processing_job_name) -> None: ...
    def describe(self): ...

class _LocalTrainingJob:
    container: Incomplete
    model_artifacts: Incomplete
    state: str
    start_time: Incomplete
    end_time: Incomplete
    environment: Incomplete
    training_job_name: str
    def __init__(self, container) -> None: ...
    def start(self, input_data_config, output_data_config, hyperparameters, environment, job_name) -> None: ...
    def describe(self): ...

class _LocalTransformJob:
    local_session: Incomplete
    name: Incomplete
    model_name: Incomplete
    primary_container: Incomplete
    container: Incomplete
    start_time: Incomplete
    end_time: Incomplete
    batch_strategy: Incomplete
    transform_resources: Incomplete
    input_data: Incomplete
    output_data: Incomplete
    environment: Incomplete
    state: Incomplete
    def __init__(self, transform_job_name, model_name, local_session: Incomplete | None = None) -> None: ...
    def start(self, input_data, output_data, transform_resources, **kwargs) -> None: ...
    def describe(self): ...

class _LocalModel:
    model_name: Incomplete
    primary_container: Incomplete
    creation_time: Incomplete
    def __init__(self, model_name, primary_container) -> None: ...
    def describe(self): ...

class _LocalEndpointConfig:
    name: Incomplete
    production_variants: Incomplete
    tags: Incomplete
    creation_time: Incomplete
    def __init__(self, config_name, production_variants, tags: Incomplete | None = None) -> None: ...
    def describe(self): ...

class _LocalEndpoint:
    local_session: Incomplete
    name: Incomplete
    endpoint_config: Incomplete
    production_variant: Incomplete
    tags: Incomplete
    primary_container: Incomplete
    container: Incomplete
    create_time: Incomplete
    state: Incomplete
    def __init__(
        self, endpoint_name, endpoint_config_name, tags: Incomplete | None = None, local_session: Incomplete | None = None
    ) -> None: ...
    def serve(self) -> None: ...
    def stop(self) -> None: ...
    def describe(self): ...

class _LocalPipeline:
    local_session: Incomplete
    pipeline: Incomplete
    pipeline_description: Incomplete
    creation_time: Incomplete
    last_modified_time: Incomplete
    def __init__(
        self, pipeline, pipeline_description: Incomplete | None = None, local_session: Incomplete | None = None
    ) -> None: ...
    def describe(self): ...
    def start(self, **kwargs): ...

class _LocalPipelineExecution:
    pipeline: Incomplete
    pipeline_execution_name: Incomplete
    pipeline_execution_description: Incomplete
    pipeline_execution_display_name: Incomplete
    status: Incomplete
    failure_reason: Incomplete
    creation_time: Incomplete
    last_modified_time: Incomplete
    step_execution: Incomplete
    pipeline_dag: Incomplete
    pipeline_parameters: Incomplete
    def __init__(
        self,
        execution_id,
        pipeline,
        PipelineParameters: Incomplete | None = None,
        PipelineExecutionDescription: Incomplete | None = None,
        PipelineExecutionDisplayName: Incomplete | None = None,
    ) -> None: ...
    def describe(self): ...
    def list_steps(self): ...
    def update_execution_success(self) -> None: ...
    def update_execution_failure(self, step_name, failure_message) -> None: ...
    def update_step_properties(self, step_name, step_properties) -> None: ...
    def update_step_failure(self, step_name, failure_message) -> None: ...
    def mark_step_executing(self, step_name) -> None: ...

class _LocalPipelineExecutionStep:
    name: Incomplete
    type: Incomplete
    description: Incomplete
    display_name: Incomplete
    status: Incomplete
    failure_reason: Incomplete
    properties: Incomplete
    start_time: Incomplete
    end_time: Incomplete
    def __init__(
        self,
        name,
        step_type,
        description,
        display_name: Incomplete | None = None,
        start_time: Incomplete | None = None,
        end_time: Incomplete | None = None,
        status: Incomplete | None = None,
        properties: Incomplete | None = None,
        failure_reason: Incomplete | None = None,
    ) -> None: ...
    def update_step_properties(self, properties) -> None: ...
    def update_step_failure(self, failure_message) -> None: ...
    def mark_step_executing(self) -> None: ...
    def to_list_steps_response(self): ...

class _LocalExecutionStatus(enum.Enum):
    EXECUTING: str
    SUCCEEDED: str
    FAILED: str
