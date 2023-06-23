from typing import Dict

from sagemaker.dataset_definition.inputs import AthenaDatasetDefinition, RedshiftDatasetDefinition

def generate_data_ingestion_flow_from_s3_input(
    input_name: str,
    s3_uri: str,
    s3_content_type: str = "csv",
    s3_has_header: bool = False,
    operator_version: str = "0.1",
    schema: Dict = None,
): ...
def generate_data_ingestion_flow_from_athena_dataset_definition(
    input_name: str, athena_dataset_definition: AthenaDatasetDefinition, operator_version: str = "0.1", schema: Dict = None
): ...
def generate_data_ingestion_flow_from_redshift_dataset_definition(
    input_name: str, redshift_dataset_definition: RedshiftDatasetDefinition, operator_version: str = "0.1", schema: Dict = None
): ...
