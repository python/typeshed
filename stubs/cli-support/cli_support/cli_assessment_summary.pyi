from .xml_base import XmlBase

class CliAssessmentSummary(XmlBase):
    GENERAL_ASSESSMENT_TAG: str
    CRITICAL_FILES_TAG: str
    DEPENDENCY_NOTES_TAG: str
    EXPORT_RESTRICTIONS_TAG: str
    USAGE_RESTRICTIONS_TAG: str
    ADDITIONAL_NOTES_TAG: str
    general_assessment: str
    critical_files_found: str
    dependency_notes: str
    export_restrictions_found: str
    usage_restrictions_found: str
    additional_notes: str
    def __init__(self) -> None: ...
