import enum
from _typeshed import Incomplete

from sagemaker import Session

TRAINING_JOB_ARN_ENV: str
PROCESSING_JOB_CONFIG_PATH: str
TRANSFORM_JOB_ARN_ENV: str
MAX_RETRY_ATTEMPTS: int
logger: Incomplete

class _EnvironmentType(enum.Enum):
    SageMakerTrainingJob: int
    SageMakerProcessingJob: int
    SageMakerTransformJob: int

class _RunEnvironment:
    environment_type: Incomplete
    source_arn: Incomplete
    def __init__(self, environment_type: _EnvironmentType, source_arn: str) -> None: ...
    @classmethod
    def load(
        cls,
        training_job_arn_env: str = "TRAINING_JOB_ARN",
        processing_job_config_path: str = "/opt/ml/config/processingjobconfig.json",
        transform_job_arn_env: str = "TRANSFORM_JOB_ARN",
    ): ...
    def get_trial_component(self, sagemaker_session: Session): ...
