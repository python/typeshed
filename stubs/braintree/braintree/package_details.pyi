from typing import ClassVar

from braintree.attribute_getter import AttributeGetter as AttributeGetter

class PackageDetails(AttributeGetter):
    detail_list: ClassVar[list[str]]
    def __init__(self, attributes) -> None: ...
