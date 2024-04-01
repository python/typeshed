from typing import ClassVar

from braintree.attribute_getter import AttributeGetter as AttributeGetter
from braintree.merchant_account.address_details import AddressDetails as AddressDetails

class IndividualDetails(AttributeGetter):
    detail_list: ClassVar[list[str]]
    address_details: AddressDetails
    def __init__(self, attributes) -> None: ...
