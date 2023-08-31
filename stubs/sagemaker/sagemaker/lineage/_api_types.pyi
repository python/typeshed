from _typeshed import Incomplete

from sagemaker.apiutils import _base_types

class ArtifactSource(_base_types.ApiObject):
    source_uri: Incomplete
    source_types: Incomplete
    def __init__(self, source_uri: Incomplete | None = None, source_types: Incomplete | None = None, **kwargs) -> None: ...

class ArtifactSourceType(_base_types.ApiObject):
    source_id_type: Incomplete
    value: Incomplete
    def __init__(self, source_id_type: Incomplete | None = None, value: Incomplete | None = None, **kwargs) -> None: ...

class ActionSource(_base_types.ApiObject):
    source_uri: Incomplete
    source_type: Incomplete
    def __init__(self, source_uri: Incomplete | None = None, source_type: Incomplete | None = None, **kwargs) -> None: ...

class ContextSource(_base_types.ApiObject):
    source_uri: Incomplete
    source_type: Incomplete
    def __init__(self, source_uri: Incomplete | None = None, source_type: Incomplete | None = None, **kwargs) -> None: ...

class ArtifactSummary(_base_types.ApiObject):
    artifact_arn: Incomplete
    artifact_name: Incomplete
    source: Incomplete
    artifact_type: Incomplete
    creation_time: Incomplete
    last_modified_time: Incomplete

class ActionSummary(_base_types.ApiObject):
    action_arn: Incomplete
    action_name: Incomplete
    source: Incomplete
    action_type: Incomplete
    status: Incomplete
    creation_time: Incomplete
    last_modified_time: Incomplete

class ContextSummary(_base_types.ApiObject):
    context_arn: Incomplete
    context_name: Incomplete
    source: Incomplete
    context_type: Incomplete
    creation_time: Incomplete
    last_modified_time: Incomplete

class UserContext(_base_types.ApiObject):
    user_profile_arn: Incomplete
    user_profile_name: Incomplete
    domain_id: Incomplete
    def __init__(
        self,
        user_profile_arn: Incomplete | None = None,
        user_profile_name: Incomplete | None = None,
        domain_id: Incomplete | None = None,
        **kwargs,
    ) -> None: ...

class AssociationSummary(_base_types.ApiObject):
    source_arn: Incomplete
    source_name: Incomplete
    destination_arn: Incomplete
    destination_name: Incomplete
    source_type: Incomplete
    destination_type: Incomplete
    association_type: Incomplete
    creation_time: Incomplete
