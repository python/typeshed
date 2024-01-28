from _typeshed import Incomplete

import tensorflow as tf
from tensorflow.keras.layers import Layer, _InputT, _OutputT

class Model(Layer[_InputT, _OutputT], tf.Module, Incomplete): ...
