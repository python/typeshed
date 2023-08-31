from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

ESTIMATORS: Incomplete
PARAMS: Incomplete

class TrainPrefixRemover(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...
