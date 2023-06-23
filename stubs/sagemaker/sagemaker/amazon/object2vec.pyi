from typing import Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class Object2Vec(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    MINI_BATCH_SIZE: int
    enc_dim: hp
    mini_batch_size: hp
    epochs: hp
    early_stopping_patience: hp
    early_stopping_tolerance: hp
    dropout: hp
    weight_decay: hp
    bucket_width: hp
    num_classes: hp
    mlp_layers: hp
    mlp_dim: hp
    mlp_activation: hp
    output_layer: hp
    optimizer: hp
    learning_rate: hp
    negative_sampling_rate: hp
    comparator_list: hp
    tied_token_embedding_weight: hp
    token_embedding_storage_type: hp
    enc0_network: hp
    enc1_network: hp
    enc0_cnn_filter_width: hp
    enc1_cnn_filter_width: hp
    enc0_max_seq_len: hp
    enc1_max_seq_len: hp
    enc0_token_embedding_dim: hp
    enc1_token_embedding_dim: hp
    enc0_vocab_size: hp
    enc1_vocab_size: hp
    enc0_layers: hp
    enc1_layers: hp
    enc0_freeze_pretrained_embedding: hp
    enc1_freeze_pretrained_embedding: hp
    def __init__(
        self,
        role: Optional[str | PipelineVariable] = None,
        instance_count: Optional[int | PipelineVariable] = None,
        instance_type: Optional[str | PipelineVariable] = None,
        epochs: Optional[int] = None,
        enc0_max_seq_len: Optional[int] = None,
        enc0_vocab_size: Optional[int] = None,
        enc_dim: Optional[int] = None,
        mini_batch_size: Optional[int] = None,
        early_stopping_patience: Optional[int] = None,
        early_stopping_tolerance: Optional[float] = None,
        dropout: Optional[float] = None,
        weight_decay: Optional[float] = None,
        bucket_width: Optional[int] = None,
        num_classes: Optional[int] = None,
        mlp_layers: Optional[int] = None,
        mlp_dim: Optional[int] = None,
        mlp_activation: Optional[str] = None,
        output_layer: Optional[str] = None,
        optimizer: Optional[str] = None,
        learning_rate: Optional[float] = None,
        negative_sampling_rate: Optional[int] = None,
        comparator_list: Optional[str] = None,
        tied_token_embedding_weight: Optional[bool] = None,
        token_embedding_storage_type: Optional[str] = None,
        enc0_network: Optional[str] = None,
        enc1_network: Optional[str] = None,
        enc0_cnn_filter_width: Optional[int] = None,
        enc1_cnn_filter_width: Optional[int] = None,
        enc1_max_seq_len: Optional[int] = None,
        enc0_token_embedding_dim: Optional[int] = None,
        enc1_token_embedding_dim: Optional[int] = None,
        enc1_vocab_size: Optional[int] = None,
        enc0_layers: Optional[int] = None,
        enc1_layers: Optional[int] = None,
        enc0_freeze_pretrained_embedding: Optional[bool] = None,
        enc1_freeze_pretrained_embedding: Optional[bool] = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class Object2VecModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        **kwargs,
    ) -> None: ...
