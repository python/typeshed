from typing import Any, Final

from braintree.attribute_getter import AttributeGetter as AttributeGetter
from braintree.configuration import Configuration as Configuration

class UsBankAccountVerification(AttributeGetter):
    class Status:
        Failed: Final = "failed"
        GatewayRejected: Final = "gateway_rejected"
        ProcessorDeclined: Final = "processor_declined"
        Unrecognized: Final = "unrecognized"
        Verified: Final = "verified"
        Pending: Final = "pending"

    # NEXT_MAJOR_VERSION this can be an enum! they were added as of python 3.4 and we support 3.5+
    class VerificationMethod:
        NetworkCheck: Final = "network_check"
        IndependentCheck: Final = "independent_check"
        TokenizedCheck: Final = "tokenized_check"
        MicroTransfers: Final = "micro_transfers"

    class VerificationAddOns:
        CustomerVerification: Final = "customer_verification"

    us_bank_account: Any
    def __init__(self, gateway, attributes) -> None: ...
    @staticmethod
    def confirm_micro_transfer_amounts(verification_id, amounts): ...
    @staticmethod
    def find(verification_id): ...
    @staticmethod
    def search(*query): ...
    def __eq__(self, other): ...
