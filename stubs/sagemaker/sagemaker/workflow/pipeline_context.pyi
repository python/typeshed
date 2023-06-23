from _typeshed import Incomplete
from typing import Callable, Optional

from sagemaker.local import LocalSession
from sagemaker.session import Session

class _StepArguments:
    caller_name: Incomplete
    func: Incomplete
    func_args: Incomplete
    func_kwargs: Incomplete
    def __init__(self, caller_name: str = None, func: Callable = None, *func_args, **func_kwargs) -> None: ...

class _JobStepArguments(_StepArguments):
    args: Incomplete
    def __init__(self, caller_name: str, args: dict) -> None: ...

class _ModelStepArguments(_StepArguments):
    model: Incomplete
    create_model_package_request: Incomplete
    create_model_request: Incomplete
    need_runtime_repack: Incomplete
    runtime_repack_output_prefix: Incomplete
    def __init__(self, model) -> None: ...

class _PipelineConfig:
    pipeline_name: Incomplete
    step_name: Incomplete
    code_hash: Incomplete
    config_hash: Incomplete
    def __init__(self, pipeline_name, step_name, code_hash, config_hash) -> None: ...

class PipelineSession(Session):
    def __init__(
        self,
        boto_session: Incomplete | None = None,
        sagemaker_client: Incomplete | None = None,
        default_bucket: Incomplete | None = None,
        settings=...,
        sagemaker_config: dict = None,
        default_bucket_prefix: str = None,
    ) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, value: Optional[_StepArguments] = ...): ...
    def init_model_step_arguments(self, model) -> None: ...

class LocalPipelineSession(LocalSession, PipelineSession):
    def __init__(
        self,
        boto_session: Incomplete | None = None,
        default_bucket: Incomplete | None = None,
        s3_endpoint_url: Incomplete | None = None,
        disable_local_code: bool = False,
        default_bucket_prefix: Incomplete | None = None,
    ) -> None: ...

def runnable_by_pipeline(run_func): ...
def retrieve_caller_name(job_instance): ...
