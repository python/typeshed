from _typeshed import Incomplete

from sagemaker.cli.compatibility.v2.modifiers.modifier import Modifier

GET_IMAGE_URI_NAME: str
GET_IMAGE_URI_NAMESPACES: Incomplete

class ImageURIRetrieveRefactor(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...

class ImageURIRetrieveImportFromRenamer(Modifier):
    def node_should_be_modified(self, node): ...
    def modify_node(self, node): ...
