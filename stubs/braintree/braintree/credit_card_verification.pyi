from _typeshed import Incomplete
from decimal import Decimal

from braintree.attribute_getter import AttributeGetter as AttributeGetter
from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource
from braintree.risk_data import RiskData as RiskData
from braintree.three_d_secure_info import ThreeDSecureInfo as ThreeDSecureInfo

class CreditCardVerification(AttributeGetter):
    class Status:
        Failed: str
        GatewayRejected: str
        ProcessorDeclined: str
        Verified: str

    amount: Decimal | None
    currency_iso_code: Incomplete
    processor_response_code: Incomplete
    processor_response_text: Incomplete
    network_response_code: Incomplete
    network_response_text: Incomplete
    risk_data: RiskData | None
    three_d_secure_info: ThreeDSecureInfo | None
    def __init__(self, gateway, attributes) -> None: ...
    @staticmethod
    def find(verification_id): ...
    @staticmethod
    def search(*query): ...
    @staticmethod
    def create(params): ...
    @staticmethod
    def create_signature(): ...
    def __eq__(self, other): ...
