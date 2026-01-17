import re
from collections.abc import Sequence

RE_DEFERRED: re.Pattern[str]

class ShowFieldBase:
    polymorphic_query_multiline_output: bool
    polymorphic_showfield_type: bool
    polymorphic_showfield_content: bool
    polymorphic_showfield_deferred: bool
    polymorphic_showfield_max_line_width: int | None
    polymorphic_showfield_max_field_width: int
    polymorphic_showfield_old_format: bool
    def _showfields_get_content(self, field_name: str, field_type: type = ...) -> str: ...
    def _showfields_add_regular_fields(self, parts: list[tuple[bool, str, str]]) -> None: ...
    def _showfields_add_dynamic_fields(
        self, field_list: Sequence[str], title: str, parts: list[tuple[bool, str, str]]
    ) -> None: ...

class ShowFieldType(ShowFieldBase):
    polymorphic_showfield_type: bool

class ShowFieldContent(ShowFieldBase):
    polymorphic_showfield_content: bool

class ShowFieldTypeAndContent(ShowFieldBase):
    polymorphic_showfield_type: bool
    polymorphic_showfield_content: bool
