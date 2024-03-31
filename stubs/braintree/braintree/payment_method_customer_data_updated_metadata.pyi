from _typeshed import Incomplete

from braintree.enriched_customer_data import EnrichedCustomerData as EnrichedCustomerData
from braintree.payment_method_parser import parse_payment_method as parse_payment_method
from braintree.resource import Resource as Resource

class PaymentMethodCustomerDataUpdatedMetadata(Resource):
    payment_method: Incomplete
    enriched_customer_data: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
