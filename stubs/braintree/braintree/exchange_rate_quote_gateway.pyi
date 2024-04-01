from _typeshed import Incomplete

from braintree.error_result import ErrorResult as ErrorResult
from braintree.exchange_rate_quote_payload import ExchangeRateQuotePayload as ExchangeRateQuotePayload
from braintree.successful_result import SuccessfulResult as SuccessfulResult

class ExchangeRateQuoteGateway:
    gateway: Incomplete
    config: Incomplete
    graphql_client: Incomplete
    def __init__(self, gateway, graphql_client: Incomplete | None = None) -> None: ...
    exchange_rate_quote_payload: Incomplete
    def generate(self, request): ...
