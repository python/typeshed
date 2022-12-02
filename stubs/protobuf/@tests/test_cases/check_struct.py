from __future__ import annotations

from google.protobuf.struct_pb2 import ListValue, Struct

list_value = ListValue()

lst = list(list_value)  # ensure ListValue's __len__ + __getitem__ make it iterable

list_value[0] = 42.42
list_value[0] = "42"
list_value[0] = None
list_value[0] = True
list_value[0] = [42.42, "42", None, True, [42.42, "42", None, True], {"42": 42}]
list_value[0] = ListValue()
list_value[0] = Struct()

list_element = list_value[0]
