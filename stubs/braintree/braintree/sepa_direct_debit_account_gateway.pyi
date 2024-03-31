from _typeshed import Incomplete

from braintree.error_result import ErrorResult as ErrorResult
from braintree.exceptions.not_found_error import NotFoundError as NotFoundError
from braintree.resource import Resource as Resource
from braintree.sepa_direct_debit_account import SepaDirectDebitAccount as SepaDirectDebitAccount
from braintree.successful_result import SuccessfulResult as SuccessfulResult

class SepaDirectDebitAccountGateway:
    gateway: Incomplete
    config: Incomplete
    def __init__(self, gateway) -> None: ...
    def find(self, sepa_direct_debit_account_token): ...
    def delete(self, sepa_direct_debit_account_token): ...
