import re

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
    def _showfields_add_annotated_fields(self, parts: list[tuple[bool, str, str]]) -> None: ...
    def _showfields_add_extra_select_fields(self, parts: list[tuple[bool, str, str]]) -> None: ...
    def _showfields_add_deferred_fields(self, parts: list[tuple[bool, str, str]]) -> None: ...

class ShowFieldType(ShowFieldBase):
    polymorphic_showfield_type: bool

class ShowFieldContent(ShowFieldBase):
    polymorphic_showfield_content: bool

class ShowFieldTypeAndContent(ShowFieldBase):
    polymorphic_showfield_type: bool
    polymorphic_showfield_content: bool
