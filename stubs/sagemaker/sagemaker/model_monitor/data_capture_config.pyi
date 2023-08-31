from _typeshed import Incomplete

class DataCaptureConfig:
    API_MAPPING: Incomplete
    enable_capture: Incomplete
    sampling_percentage: Incomplete
    destination_s3_uri: Incomplete
    kms_key_id: Incomplete
    capture_options: Incomplete
    csv_content_types: Incomplete
    json_content_types: Incomplete
    def __init__(
        self,
        enable_capture,
        sampling_percentage: int = 20,
        destination_s3_uri: Incomplete | None = None,
        kms_key_id: Incomplete | None = None,
        capture_options: Incomplete | None = None,
        csv_content_types: Incomplete | None = None,
        json_content_types: Incomplete | None = None,
        sagemaker_session: Incomplete | None = None,
    ) -> None: ...
