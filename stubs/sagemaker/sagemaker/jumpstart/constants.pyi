from _typeshed import Incomplete
from typing import Dict, Set, Type

from sagemaker.base_deserializers import BaseDeserializer
from sagemaker.base_serializers import BaseSerializer
from sagemaker.jumpstart.enums import DeserializerType, MIMEType, SerializerType
from sagemaker.jumpstart.types import JumpStartLaunchedRegionInfo

JUMPSTART_LAUNCHED_REGIONS: Set[JumpStartLaunchedRegionInfo]
JUMPSTART_REGION_NAME_TO_LAUNCHED_REGION_DICT: Incomplete
JUMPSTART_REGION_NAME_SET: Incomplete
JUMPSTART_BUCKET_NAME_SET: Incomplete
JUMPSTART_DEFAULT_REGION_NAME: Incomplete
JUMPSTART_DEFAULT_MANIFEST_FILE_S3_KEY: str
INFERENCE_ENTRY_POINT_SCRIPT_NAME: str
TRAINING_ENTRY_POINT_SCRIPT_NAME: str
SUPPORTED_JUMPSTART_SCOPES: Incomplete
ENV_VARIABLE_JUMPSTART_CONTENT_BUCKET_OVERRIDE: str
ENV_VARIABLE_JUMPSTART_MODEL_ARTIFACT_BUCKET_OVERRIDE: str
ENV_VARIABLE_JUMPSTART_SCRIPT_ARTIFACT_BUCKET_OVERRIDE: str
ENV_VARIABLE_JUMPSTART_MANIFEST_LOCAL_ROOT_DIR_OVERRIDE: str
ENV_VARIABLE_JUMPSTART_SPECS_LOCAL_ROOT_DIR_OVERRIDE: str
JUMPSTART_RESOURCE_BASE_NAME: str
CONTENT_TYPE_TO_SERIALIZER_TYPE_MAP: Dict[MIMEType, SerializerType]
ACCEPT_TYPE_TO_DESERIALIZER_TYPE_MAP: Dict[MIMEType, DeserializerType]
SERIALIZER_TYPE_TO_CLASS_MAP: Dict[SerializerType, Type[BaseSerializer]]
DESERIALIZER_TYPE_TO_CLASS_MAP: Dict[DeserializerType, Type[BaseDeserializer]]
MODEL_ID_LIST_WEB_URL: str
