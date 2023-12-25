from _typeshed import Incomplete

from .xml_base import XmlBase

class CliFile(XmlBase):
    LICENSE_TAG: str
    COPYRIGHT_TAG: str
    EXPORTRESTRICTIONS_TAG: str
    OBLIGATION_TAG: str
    TAGS_TAG: str
    GENERAL_INFORMATION_TAG: str
    ASSESSMENT_SUMMARY_TAG: str
    EXTERNAL_IDS_TAG: str
    IRRELEVANT_FILES_TAG: str
    COMMENT_TAG: str
    filename: str
    component: str
    creator: str
    date: str
    baseDoc: str
    toolUsed: str
    componentId: str
    includesAcknowledgements: bool
    componentSha1: str
    version: str
    general_information: Incomplete
    assessment_summary: Incomplete
    licenses: Incomplete
    copyrights: Incomplete
    obligations: Incomplete
    tags: Incomplete
    export_restrictions: Incomplete
    external_ids: Incomplete
    irrelevant_files: Incomplete
    comment: str
    def __init__(self) -> None: ...
    def read_from_file(self, filename: str) -> None: ...
    def write_to_file(self, filename: str) -> None: ...
