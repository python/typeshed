from _typeshed import Incomplete

from braintree.attribute_getter import AttributeGetter as AttributeGetter

text_type = str
raw_type = bytes

class Resource(AttributeGetter):
    @staticmethod
    def verify_keys(params, signature) -> None: ...
    gateway: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
