from _typeshed import Incomplete

from braintree.payment_method_parser import parse_payment_method as parse_payment_method
from braintree.resource import Resource as Resource

class RevokedPaymentMethodMetadata(Resource):
    revoked_payment_method: Incomplete
    customer_id: Incomplete
    token: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
