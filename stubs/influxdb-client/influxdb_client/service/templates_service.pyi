from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class TemplatesService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def apply_template(self, template_apply, **kwargs): ...
    def apply_template_with_http_info(self, template_apply, **kwargs): ...
    async def apply_template_async(self, template_apply, **kwargs): ...
    def create_stack(self, **kwargs): ...
    def create_stack_with_http_info(self, **kwargs): ...
    async def create_stack_async(self, **kwargs): ...
    def delete_stack(self, stack_id, org_id, **kwargs): ...
    def delete_stack_with_http_info(self, stack_id, org_id, **kwargs): ...
    async def delete_stack_async(self, stack_id, org_id, **kwargs): ...
    def export_template(self, **kwargs): ...
    def export_template_with_http_info(self, **kwargs): ...
    async def export_template_async(self, **kwargs): ...
    def list_stacks(self, org_id, **kwargs): ...
    def list_stacks_with_http_info(self, org_id, **kwargs): ...
    async def list_stacks_async(self, org_id, **kwargs): ...
    def read_stack(self, stack_id, **kwargs): ...
    def read_stack_with_http_info(self, stack_id, **kwargs): ...
    async def read_stack_async(self, stack_id, **kwargs): ...
    def uninstall_stack(self, stack_id, **kwargs): ...
    def uninstall_stack_with_http_info(self, stack_id, **kwargs): ...
    async def uninstall_stack_async(self, stack_id, **kwargs): ...
    def update_stack(self, stack_id, **kwargs): ...
    def update_stack_with_http_info(self, stack_id, **kwargs): ...
    async def update_stack_async(self, stack_id, **kwargs): ...
