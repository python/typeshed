from _typeshed import Incomplete

from braintree.apple_pay_options import ApplePayOptions as ApplePayOptions
from braintree.error_result import ErrorResult as ErrorResult
from braintree.exceptions.unexpected_error import UnexpectedError as UnexpectedError
from braintree.successful_result import SuccessfulResult as SuccessfulResult

class ApplePayGateway:
    gateway: Incomplete
    config: Incomplete
    def __init__(self, gateway) -> None: ...
    def register_domain(self, domain): ...
    def unregister_domain(self, domain): ...
    def registered_domains(self): ...
