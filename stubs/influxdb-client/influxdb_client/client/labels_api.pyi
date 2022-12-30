from influxdb_client import Label

class LabelsApi:
    def __init__(self, influxdb_client) -> None: ...
    def create_label(self, name: str, org_id: str, properties: dict[str, str] = ...) -> Label: ...
    def update_label(self, label: Label): ...
    def delete_label(self, label: str | Label): ...
    def clone_label(self, cloned_name: str, label: Label) -> Label: ...
    def find_labels(self, **kwargs) -> list[Label]: ...
    def find_label_by_id(self, label_id: str): ...
    def find_label_by_org(self, org_id) -> list[Label]: ...
