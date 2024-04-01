from _typeshed import Incomplete

from braintree.resource import Resource as Resource
from braintree.transaction import Transaction as Transaction

class LocalPaymentFunded(Resource):
    transaction: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
