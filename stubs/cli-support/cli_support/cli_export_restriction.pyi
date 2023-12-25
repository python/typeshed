from .cli_file_item_base import CliFileItemBase

class CliExportRestriction(CliFileItemBase):
    CONTENT_TAG: str
    COMMENT_TAG: str
    export_restriction_text: str
    export_restriction_comment: str
    def __init__(self) -> None: ...
