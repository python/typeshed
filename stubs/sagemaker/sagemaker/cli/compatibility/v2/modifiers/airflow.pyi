from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers import renamed_params
from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

FUNCTION_NAMES: Incomplete
NAMESPACES: Incomplete
FUNCTIONS: Incomplete

class ModelConfigArgModifier(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class ModelConfigImageURIRenamer(renamed_params.ParamRenamer):
    @property
    def calls_to_modify(self): ...
    @property
    def old_param_name(self): ...
    @property
    def new_param_name(self): ...
