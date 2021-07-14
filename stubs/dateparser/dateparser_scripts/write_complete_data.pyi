from typing import Any

from dateparser_scripts.order_languages import avoid_languages as avoid_languages
from dateparser_scripts.utils import combine_dicts as combine_dicts

cldr_date_directory: str
supplementary_directory: str
supplementary_date_directory: str
translation_data_directory: str
date_translation_directory: str
cldr_languages: Any
supplementary_languages: Any
all_languages: Any
RELATIVE_PATTERN: Any

def write_complete_data(in_memory: bool = ...): ...
