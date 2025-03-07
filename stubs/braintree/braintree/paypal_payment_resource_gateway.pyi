from braintree.resource import Resource
from braintree.paypal_payment_resource import PayPalPaymentResource
from braintree.payment_method_nonce import PaymentMethodNonce
from braintree.util.xml_util import XmlUtil
from braintree.error_result import ErrorResult
from braintree.successful_result import SuccessfulResult
from braintree.exceptions.unexpected_error import UnexpectedError
from braintree.braintree_gateway import BraintreeGateway
from _typeshed import Incomplete
from braintree.configuration import Configuration

class PayPalPaymentResourceGateway:
    config: Configuration
    gateway: BraintreeGateway
    def __init__(self, gateway: BraintreeGateway) -> None: ...
    def update(self, params) -> SuccessfulResult | ErrorResult: ...
