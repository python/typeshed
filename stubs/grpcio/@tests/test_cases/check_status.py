from __future__ import annotations

from grpc import Status
from grpc_status import to_status

# XXX: to_status actually expects a "google.rpc.status.Status",
# but the stubs for that aren't present yet.
status: Status = to_status(None)
