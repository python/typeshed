from braintree.resource import Resource as Resource
from braintree.transaction import Transaction as Transaction

class LocalPaymentCompleted(Resource):
    transaction: Transaction
    def __init__(self, gateway, attributes) -> None: ...
