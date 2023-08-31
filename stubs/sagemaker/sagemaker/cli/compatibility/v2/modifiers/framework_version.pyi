from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

FRAMEWORK_ARG: str
IMAGE_ARG: str
PY_ARG: str
FRAMEWORK_DEFAULTS: Incomplete
FRAMEWORK_CLASSES: Incomplete
ESTIMATORS: Incomplete
MODELS: Incomplete

class FrameworkVersionEnforcer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...
