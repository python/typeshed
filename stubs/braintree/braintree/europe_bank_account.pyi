from typing import Final

from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource

class EuropeBankAccount(Resource):
    class MandateType:
        Business: Final = "business"
        Consumer: Final = "consumer"

    @staticmethod
    def signature(): ...
