from typing import Any, Optional

RELATIVE_REG: Any

def date_is_relative(translation): ...

class _ExactLanguageSearch:
    loader: Any = ...
    language: Any = ...
    def __init__(self, loader) -> None: ...
    def get_current_language(self, shortname) -> None: ...
    def search(self, shortname, text, settings): ...
    @staticmethod
    def set_relative_base(substring, already_parsed): ...
    def choose_best_split(self, possible_parsed_splits, possible_substrings_splits): ...
    def split_by(self, item, original, splitter): ...
    def split_if_not_parsed(self, item, original): ...
    def parse_item(self, parser, item, translated_item, parsed, need_relative_base): ...
    def parse_found_objects(self, parser, to_parse, original, translated, settings): ...
    def search_parse(self, shortname, text, settings): ...

class DateSearchWithDetection:
    loader: Any = ...
    available_language_map: Any = ...
    search: Any = ...
    def __init__(self) -> None: ...
    language_detector: Any = ...
    def detect_language(self, text, languages): ...
    def search_dates(self, text, languages: Any | None = ..., settings: Any | None = ...): ...
