from _typeshed import Incomplete
from typing import Final

from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource
from braintree.successful_result import SuccessfulResult as SuccessfulResult

class DocumentUpload(Resource):
    class Kind:
        EvidenceDocument: Final = "evidence_document"

    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def create_signature(): ...
    def __init__(self, gateway, attributes) -> None: ...
