from _typeshed import Incomplete

from braintree.bin_data import BinData as BinData
from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource
from braintree.three_d_secure_info import ThreeDSecureInfo as ThreeDSecureInfo

class PaymentMethodNonce(Resource):
    @staticmethod
    def create(payment_method_token, params={}): ...
    @staticmethod
    def find(payment_method_nonce): ...
    three_d_secure_info: ThreeDSecureInfo
    authentication_insight: Incomplete
    bin_data: BinData
    def __init__(self, gateway, attributes) -> None: ...
