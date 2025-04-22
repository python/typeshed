from typing import Literal

from braintree.resource import Resource

class UnknownPaymentMethod(Resource):
    def image_url(self) -> Literal["https://assets.braintreegateway.com/payment_method_logo/unknown.png"]: ...
