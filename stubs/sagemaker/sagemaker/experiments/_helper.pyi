from _typeshed import Incomplete

logger: Incomplete

class _ArtifactUploader:
    sagemaker_session: Incomplete
    trial_component_name: Incomplete
    artifact_bucket: Incomplete
    artifact_prefix: Incomplete
    def __init__(
        self,
        trial_component_name,
        sagemaker_session,
        artifact_bucket: Incomplete | None = None,
        artifact_prefix="trial-component-artifacts",
    ) -> None: ...
    def upload_artifact(self, file_path): ...
    def upload_object_artifact(self, artifact_name, artifact_object, file_extension: Incomplete | None = None): ...

class _LineageArtifactManager:
    name: Incomplete
    source_uri: Incomplete
    etag: Incomplete
    source_arn: Incomplete
    dest_arn: Incomplete
    artifact_arn: Incomplete
    artifact_type: Incomplete
    def __init__(
        self,
        name,
        source_uri,
        etag,
        source_arn: Incomplete | None = None,
        dest_arn: Incomplete | None = None,
        artifact_type="Tracker",
    ) -> None: ...
    def create_artifact(self, sagemaker_session) -> None: ...
    def add_association(self, sagemaker_session) -> None: ...

class _LineageArtifactTracker:
    trial_component_arn: Incomplete
    sagemaker_session: Incomplete
    artifacts: Incomplete
    def __init__(self, trial_component_arn, sagemaker_session) -> None: ...
    def add_input_artifact(self, name, source_uri, etag, artifact_type) -> None: ...
    def add_output_artifact(self, name, source_uri, etag, artifact_type) -> None: ...
    def save(self) -> None: ...
