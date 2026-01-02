from types import TracebackType
from typing_extensions import Self

from auth0.rest import RestClientOptions

# ignore: Relative import climbs too many namespaces
from .._asyncified.management.actions import _ActionsAsync  # type: ignore[misc]
from .._asyncified.management.attack_protection import _AttackProtectionAsync  # type: ignore[misc]
from .._asyncified.management.blacklists import _BlacklistsAsync  # type: ignore[misc]
from .._asyncified.management.branding import _BrandingAsync  # type: ignore[misc]
from .._asyncified.management.client_credentials import _ClientCredentialsAsync  # type: ignore[misc]
from .._asyncified.management.client_grants import _ClientGrantsAsync  # type: ignore[misc]
from .._asyncified.management.clients import _ClientsAsync  # type: ignore[misc]
from .._asyncified.management.connections import _ConnectionsAsync  # type: ignore[misc]
from .._asyncified.management.custom_domains import _CustomDomainsAsync  # type: ignore[misc]
from .._asyncified.management.device_credentials import _DeviceCredentialsAsync  # type: ignore[misc]
from .._asyncified.management.email_templates import _EmailTemplatesAsync  # type: ignore[misc]
from .._asyncified.management.emails import _EmailsAsync  # type: ignore[misc]
from .._asyncified.management.grants import _GrantsAsync  # type: ignore[misc]
from .._asyncified.management.guardian import _GuardianAsync  # type: ignore[misc]
from .._asyncified.management.hooks import _HooksAsync  # type: ignore[misc]
from .._asyncified.management.jobs import _JobsAsync  # type: ignore[misc]
from .._asyncified.management.log_streams import _LogStreamsAsync  # type: ignore[misc]
from .._asyncified.management.logs import _LogsAsync  # type: ignore[misc]
from .._asyncified.management.organizations import _OrganizationsAsync  # type: ignore[misc]
from .._asyncified.management.prompts import _PromptsAsync  # type: ignore[misc]
from .._asyncified.management.resource_servers import _ResourceServersAsync  # type: ignore[misc]
from .._asyncified.management.roles import _RolesAsync  # type: ignore[misc]
from .._asyncified.management.rules import _RulesAsync  # type: ignore[misc]
from .._asyncified.management.rules_configs import _RulesConfigsAsync  # type: ignore[misc]
from .._asyncified.management.stats import _StatsAsync  # type: ignore[misc]
from .._asyncified.management.tenants import _TenantsAsync  # type: ignore[misc]
from .._asyncified.management.tickets import _TicketsAsync  # type: ignore[misc]
from .._asyncified.management.user_blocks import _UserBlocksAsync  # type: ignore[misc]
from .._asyncified.management.users import _UsersAsync  # type: ignore[misc]
from .._asyncified.management.users_by_email import _UsersByEmailAsync  # type: ignore[misc]

class AsyncAuth0:
    def __init__(self, domain: str, token: str, rest_options: RestClientOptions | None = None) -> None: ...
    def set_session(self, session) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

    # Same as Auth0, but async
    actions: _ActionsAsync
    attack_protection: _AttackProtectionAsync
    blacklists: _BlacklistsAsync
    branding: _BrandingAsync
    client_credentials: _ClientCredentialsAsync
    client_grants: _ClientGrantsAsync
    clients: _ClientsAsync
    connections: _ConnectionsAsync
    custom_domains: _CustomDomainsAsync
    device_credentials: _DeviceCredentialsAsync
    email_templates: _EmailTemplatesAsync
    emails: _EmailsAsync
    grants: _GrantsAsync
    guardian: _GuardianAsync
    hooks: _HooksAsync
    jobs: _JobsAsync
    log_streams: _LogStreamsAsync
    logs: _LogsAsync
    organizations: _OrganizationsAsync
    prompts: _PromptsAsync
    resource_servers: _ResourceServersAsync
    roles: _RolesAsync
    rules_configs: _RulesConfigsAsync
    rules: _RulesAsync
    stats: _StatsAsync
    tenants: _TenantsAsync
    tickets: _TicketsAsync
    user_blocks: _UserBlocksAsync
    users_by_email: _UsersByEmailAsync
    users: _UsersAsync
