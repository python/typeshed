from _typeshed import Incomplete

from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource

class SepaDirectDebitAccount(Resource):
    @staticmethod
    def find(sepa_direct_debit_account_token): ...
    @staticmethod
    def delete(sepa_direct_debit_account_token): ...
    subscriptions: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
