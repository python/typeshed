from typing import Any, Optional

RELATIVE_REG: Any

def date_is_relative(translation: Any): ...

class _ExactLanguageSearch:
    loader: Any = ...
    language: Any = ...
    def __init__(self, loader: Any) -> None: ...
    def get_current_language(self, shortname: Any) -> None: ...
    def search(self, shortname: Any, text: Any, settings: Any): ...
    @staticmethod
    def set_relative_base(substring: Any, already_parsed: Any): ...
    def choose_best_split(self, possible_parsed_splits: Any, possible_substrings_splits: Any): ...
    def split_by(self, item: Any, original: Any, splitter: Any): ...
    def split_if_not_parsed(self, item: Any, original: Any): ...
    def parse_item(self, parser: Any, item: Any, translated_item: Any, parsed: Any, need_relative_base: Any): ...
    def parse_found_objects(self, parser: Any, to_parse: Any, original: Any, translated: Any, settings: Any): ...
    def search_parse(self, shortname: Any, text: Any, settings: Any): ...

class DateSearchWithDetection:
    loader: Any = ...
    available_language_map: Any = ...
    search: Any = ...
    def __init__(self) -> None: ...
    language_detector: Any = ...
    def detect_language(self, text: Any, languages: Any): ...
    def search_dates(self, text: Any, languages: Optional[Any] = ..., settings: Optional[Any] = ...): ...
