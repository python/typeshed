from sagemaker import Session
from sagemaker.experiments._environment import _RunEnvironment

def resolve_artifact_name(file_path): ...
def guess_media_type(file_path): ...
def verify_length_of_true_and_predicted(true_labels, predicted_attrs, predicted_attrs_name) -> None: ...
def validate_invoked_inside_run_context(func): ...
def is_already_exist_error(error): ...
def get_tc_and_exp_config_from_job_env(environment: _RunEnvironment, sagemaker_session: Session) -> dict: ...
def verify_load_input_names(run_name: str | None = None, experiment_name: str | None = None): ...
def is_run_trial_component(trial_component_name: str, sagemaker_session: Session) -> bool: ...
