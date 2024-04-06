from _typeshed import Incomplete

from braintree.resource import Resource

class PaymentMethod(Resource):
    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def find(payment_method_token): ...
    @staticmethod
    def update(payment_method_token, params): ...
    @staticmethod
    def delete(payment_method_token, options: Incomplete | None = None): ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def signature(type): ...
    @staticmethod
    def update_signature(): ...
    @staticmethod
    def delete_signature(): ...
