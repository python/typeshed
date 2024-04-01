from braintree.ach_mandate import AchMandate as AchMandate
from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource
from braintree.us_bank_account_verification import UsBankAccountVerification as UsBankAccountVerification

class UsBankAccount(Resource):
    @staticmethod
    def find(token): ...
    @staticmethod
    def sale(token, transactionRequest): ...
    @staticmethod
    def signature(): ...
    ach_mandate: AchMandate | None
    verifications: list[UsBankAccountVerification]
    def __init__(self, gateway, attributes) -> None: ...
