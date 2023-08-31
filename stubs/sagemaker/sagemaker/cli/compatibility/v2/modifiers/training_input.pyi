from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

S3_INPUT_NAME: str
S3_INPUT_NAMESPACES: Incomplete

class TrainingInputConstructorRefactor(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class TrainingInputImportFromRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class ShuffleConfigModuleRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class ShuffleConfigImportFromRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...
