from typing import Any

from ... import DEREF_NEVER as DEREF_NEVER, SUBTREE as SUBTREE
from ...core.exceptions import LDAPExtensionError as LDAPExtensionError
from ...protocol.microsoft import (
    dir_sync_control as dir_sync_control,
    extended_dn_control as extended_dn_control,
    show_deleted_control as show_deleted_control,
)
from ...utils.dn import safe_dn as safe_dn

class DirSync:
    connection: Any
    base: Any
    filter: Any
    attributes: Any
    cookie: Any
    object_security: Any
    ancestors_first: Any
    public_data_only: Any
    incremental_values: Any
    max_length: Any
    hex_guid: Any
    more_results: bool
    def __init__(
        self,
        connection,
        sync_base,
        sync_filter,
        attributes,
        cookie,
        object_security,
        ancestors_first,
        public_data_only,
        incremental_values,
        max_length,
        hex_guid,
    ) -> None: ...
    def loop(self): ...
