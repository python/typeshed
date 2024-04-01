from _typeshed import Incomplete

from braintree.resource import Resource as Resource
from braintree.venmo_profile_data import VenmoProfileData as VenmoProfileData

class EnrichedCustomerData(Resource):
    profile_data: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
