from braintree.attribute_getter import AttributeGetter as AttributeGetter
from braintree.configuration import Configuration as Configuration
from braintree.us_bank_account import UsBankAccount

class UsBankAccountVerification(AttributeGetter):
    class Status:
        Failed: str
        GatewayRejected: str
        ProcessorDeclined: str
        Unrecognized: str
        Verified: str
        Pending: str

    class VerificationMethod:
        NetworkCheck: str
        IndependentCheck: str
        TokenizedCheck: str
        MicroTransfers: str

    class VerificationAddOns:
        CustomerVerification: str

    us_bank_account: UsBankAccount | None
    def __init__(self, gateway, attributes) -> None: ...
    @staticmethod
    def confirm_micro_transfer_amounts(verification_id, amounts): ...
    @staticmethod
    def find(verification_id): ...
    @staticmethod
    def search(*query): ...
    def __eq__(self, other): ...
