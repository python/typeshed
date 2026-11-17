from _typeshed import Incomplete

class TargetLookupItem:
    state: Incomplete
    target_box: Incomplete
    parse_again_functions: Incomplete
    page_maker_index: Incomplete
    cached_page_counter_values: Incomplete
    def __init__(self, state: str = "pending") -> None: ...

class CounterLookupItem:
    parse_again: Incomplete
    missing_counters: Incomplete
    missing_target_counters: Incomplete
    page_maker_index: Incomplete
    pending: bool
    cached_page_counter_values: Incomplete
    def __init__(self, parse_again, missing_counters, missing_target_counters) -> None: ...

def anchor_name_from_token(anchor_token): ...

class TargetCollector:
    target_lookup_items: Incomplete
    counter_lookup_items: Incomplete
    collecting: bool
    had_pending_targets: bool
    def __init__(self) -> None: ...
    def collect_anchor(self, anchor_name) -> None: ...
    def lookup_target(self, anchor_token, source_box, css_token, parse_again): ...
    def store_target(self, anchor_name, target_counter_values, target_box) -> None: ...
    def collect_missing_counters(
        self, parent_box, css_token, parse_again_function, missing_counters, missing_target_counters
    ) -> None: ...
    def check_pending_targets(self) -> None: ...
    def cache_target_page_counters(self, anchor_name, page_counter_values, page_maker_index, page_maker) -> None: ...
