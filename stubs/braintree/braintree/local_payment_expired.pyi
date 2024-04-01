from braintree.resource import Resource as Resource

class LocalPaymentExpired(Resource):
    def __init__(self, gateway, attributes) -> None: ...
