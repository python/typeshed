from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class RulesService(_BaseService):
    def __init__(self, api_client: Incomplete | None = ...) -> None: ...
    def get_notification_rules_id_query(self, rule_id, **kwargs): ...
    def get_notification_rules_id_query_with_http_info(self, rule_id, **kwargs): ...
    async def get_notification_rules_id_query_async(self, rule_id, **kwargs): ...
