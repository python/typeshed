from _typeshed import Incomplete

from dateparser.search.detection import BaseLanguageDetector

class FullTextLanguageDetector(BaseLanguageDetector):
    languages: Incomplete
    language_unique_chars: Incomplete
    language_chars: Incomplete
    def __init__(self, languages) -> None: ...
    def get_unique_characters(self, settings) -> None: ...
    def character_check(self, date_string, settings) -> None: ...
