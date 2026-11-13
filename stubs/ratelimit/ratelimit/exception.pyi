from _typeshed import FloatInt

class RateLimitException(Exception):
    period_remaining: FloatInt
    def __init__(self, message: str, period_remaining: FloatInt) -> None: ...
