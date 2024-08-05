from __future__ import annotations

import typing

import grpc
from grpc_reflection.v1alpha.reflection import enable_server_reflection

server = typing.cast(grpc.Server, None)
enable_server_reflection(["foo"], server, None)
