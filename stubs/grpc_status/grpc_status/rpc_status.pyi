import grpc
import typing


# XXX: don't yet know how to add a stub for google.rpc.status_pb2.Status
# without affecting other stuff; may need to make a stub-only package for
# google.rpc as well.


# Returns a google.rpc.status.Status message corresponding to a given grpc.Call.
def from_call(call: grpc.Call) -> typing.Any:
    ...


# Convert a google.rpc.status.Status message to grpc.Status.
def to_status(status: typing.Any) -> grpc.Status:
    ...
