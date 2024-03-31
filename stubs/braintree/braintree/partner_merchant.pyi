from _typeshed import Incomplete

from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource

class PartnerMerchant(Resource):
    partner_merchant_id: Incomplete
    private_key: Incomplete
    public_key: Incomplete
    merchant_public_id: Incomplete
    client_side_encryption_key: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
