from _typeshed import Incomplete

from braintree.exchange_rate_quote import ExchangeRateQuote as ExchangeRateQuote
from braintree.montary_amount import MontaryAmount as MontaryAmount

class ExchangeRateQuotePayload:
    quotes: Incomplete
    def __init__(self, data) -> None: ...
    def get_quotes(self): ...
