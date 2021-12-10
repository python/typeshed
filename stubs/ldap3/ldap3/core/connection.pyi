from typing import Any

SASL_AVAILABLE_MECHANISMS: Any
CLIENT_STRATEGIES: Any

class Connection:
    connection_lock: Any
    last_error: str
    strategy_type: Any
    user: Any
    password: Any
    authentication: Any
    version: Any
    auto_referrals: Any
    request: Any
    response: Any
    result: Any
    bound: bool
    listening: bool
    closed: bool
    auto_bind: Any
    sasl_mechanism: Any
    sasl_credentials: Any
    socket: Any
    tls_started: bool
    sasl_in_progress: bool
    read_only: Any
    lazy: Any
    pool_name: Any
    pool_size: Any
    cred_store: Any
    pool_lifetime: Any
    pool_keepalive: Any
    starting_tls: bool
    check_names: Any
    raise_exceptions: Any
    auto_range: Any
    extend: Any
    fast_decoder: Any
    receive_timeout: Any
    empty_attributes: Any
    use_referral_cache: Any
    auto_escape: Any
    auto_encode: Any
    source_address: Any
    source_port_list: Any
    server_pool: Any
    server: Any
    strategy: Any
    send: Any
    open: Any
    get_response: Any
    post_send_single_response: Any
    post_send_search: Any
    def __init__(
        self,
        server,
        user: Any | None = ...,
        password: Any | None = ...,
        auto_bind=...,
        version: int = ...,
        authentication: Any | None = ...,
        client_strategy=...,
        auto_referrals: bool = ...,
        auto_range: bool = ...,
        sasl_mechanism: Any | None = ...,
        sasl_credentials: Any | None = ...,
        check_names: bool = ...,
        collect_usage: bool = ...,
        read_only: bool = ...,
        lazy: bool = ...,
        raise_exceptions: bool = ...,
        pool_name: Any | None = ...,
        pool_size: Any | None = ...,
        pool_lifetime: Any | None = ...,
        cred_store: Any | None = ...,
        fast_decoder: bool = ...,
        receive_timeout: Any | None = ...,
        return_empty_attributes: bool = ...,
        use_referral_cache: bool = ...,
        auto_escape: bool = ...,
        auto_encode: bool = ...,
        pool_keepalive: Any | None = ...,
        source_address: Any | None = ...,
        source_port: Any | None = ...,
        source_port_list: Any | None = ...,
    ) -> None: ...
    def repr_with_sensitive_data_stripped(self): ...
    @property
    def stream(self): ...
    @stream.setter
    def stream(self, value) -> None: ...
    @property
    def usage(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def bind(self, read_server_info: bool = ..., controls: Any | None = ...): ...
    def rebind(
        self,
        user: Any | None = ...,
        password: Any | None = ...,
        authentication: Any | None = ...,
        sasl_mechanism: Any | None = ...,
        sasl_credentials: Any | None = ...,
        read_server_info: bool = ...,
        controls: Any | None = ...,
    ): ...
    def unbind(self, controls: Any | None = ...): ...
    def search(
        self,
        search_base,
        search_filter,
        search_scope=...,
        dereference_aliases=...,
        attributes: Any | None = ...,
        size_limit: int = ...,
        time_limit: int = ...,
        types_only: bool = ...,
        get_operational_attributes: bool = ...,
        controls: Any | None = ...,
        paged_size: Any | None = ...,
        paged_criticality: bool = ...,
        paged_cookie: Any | None = ...,
        auto_escape: Any | None = ...,
    ): ...
    def compare(self, dn, attribute, value, controls: Any | None = ...): ...
    def add(self, dn, object_class: Any | None = ..., attributes: Any | None = ..., controls: Any | None = ...): ...
    def delete(self, dn, controls: Any | None = ...): ...
    def modify(self, dn, changes, controls: Any | None = ...): ...
    def modify_dn(
        self, dn, relative_dn, delete_old_dn: bool = ..., new_superior: Any | None = ..., controls: Any | None = ...
    ): ...
    def abandon(self, message_id, controls: Any | None = ...): ...
    def extended(
        self, request_name, request_value: Any | None = ..., controls: Any | None = ..., no_encode: Any | None = ...
    ): ...
    def start_tls(self, read_server_info: bool = ...): ...
    def do_sasl_bind(self, controls): ...
    def do_ntlm_bind(self, controls): ...
    def refresh_server_info(self) -> None: ...
    def response_to_ldif(
        self,
        search_result: Any | None = ...,
        all_base64: bool = ...,
        line_separator: Any | None = ...,
        sort_order: Any | None = ...,
        stream: Any | None = ...,
    ): ...
    def response_to_json(
        self,
        raw: bool = ...,
        search_result: Any | None = ...,
        indent: int = ...,
        sort: bool = ...,
        stream: Any | None = ...,
        checked_attributes: bool = ...,
        include_empty: bool = ...,
    ): ...
    def response_to_file(self, target, raw: bool = ..., indent: int = ..., sort: bool = ...) -> None: ...
    @property
    def entries(self): ...
