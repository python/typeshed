from _typeshed import Incomplete

from braintree.error_result import ErrorResult as ErrorResult
from braintree.successful_result import SuccessfulResult as SuccessfulResult
from braintree.transaction import Transaction as Transaction

class TestingGateway:
    gateway: Incomplete
    config: Incomplete
    def __init__(self, gateway) -> None: ...
    def make_past_due(self, subscription_id, number_of_days_past_due: int = 1) -> None: ...
    def escrow_transaction(self, transaction_id) -> None: ...
    def settle_transaction(self, transaction_id): ...
    def settlement_confirm_transaction(self, transaction_id): ...
    def settlement_decline_transaction(self, transaction_id): ...
    def settlement_pending_transaction(self, transaction_id): ...
    def create_3ds_verification(self, merchant_account_id, params): ...
