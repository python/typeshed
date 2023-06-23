import abc
from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

CLASS_NAMES: Incomplete
TFS_CLASSES: Incomplete

class TensorFlowServingConstructorRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class TensorFlowServingImportFromRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class TensorFlowServingImportRenamer(Modifier, metaclass=abc.ABCMeta):
    def check_and_modify_node(self, node): ...
