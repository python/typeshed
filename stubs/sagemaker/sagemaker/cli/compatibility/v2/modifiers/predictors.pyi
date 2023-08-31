from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

BASE_PREDICTOR: str
PREDICTORS: Incomplete

class PredictorConstructorRefactor(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class PredictorImportFromRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...
