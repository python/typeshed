from .xml_base import XmlBase

class CliGeneralInformation(XmlBase):
    REPORTID_TAG: str
    REVIEWED_BY_TAG: str
    COMPONENT_NAME_TAG: str
    COMMUNITY_TAG: str
    COMPONENT_VERSION_TAG: str
    COMPONENT_HASH_TAG: str
    COMPONENT_RELEAESE_DATE_TAG: str
    LINK_COMPONENT_MGNT_TAG: str
    LINK_SCAN_TOOL_TAG: str
    COMPONENT_ID_ELEMENT_TAG: str
    COMPONENT_TYPE_TAG: str
    COMPONENT_ID_TAG: str
    report_id: str
    reviewed_by: str
    component_name: str
    community: str
    component_version: str
    component_hash: str
    component_release_date: str
    link_component_management: str
    link_scan_tool: str
    component_id: str
    component_id_type: str
    def __init__(self) -> None: ...
