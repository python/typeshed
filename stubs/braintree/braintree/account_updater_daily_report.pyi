from _typeshed import Incomplete

from braintree.configuration import Configuration as Configuration
from braintree.resource import Resource as Resource

class AccountUpdaterDailyReport(Resource):
    report_url: Incomplete
    report_date: Incomplete
    def __init__(self, gateway, attributes) -> None: ...
