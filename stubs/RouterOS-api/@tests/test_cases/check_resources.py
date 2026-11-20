from __future__ import annotations

from datetime import timedelta
from typing import Any
from typing_extensions import assert_type

from routeros_api import RouterOsApiPool
from routeros_api.api_structure import BooleanField, IntegerField, StringField, TimedeltaField
from routeros_api.resource import RouterOsResource

api = RouterOsApiPool("192.0.2.1").get_api()

assert_type(api.get_resource("/ip/address"), RouterOsResource[str, str])

# A structure of one field type carries that type into the resource.
flags = api.get_resource("/interface", structure={"disabled": BooleanField(), "running": BooleanField()})
assert_type(flags, RouterOsResource[bool, bool])
assert_type(flags.get(disabled=True)[0]["running"], bool)

# None is sent without a value as an argument, refused as a query, and decoded from "none".
timeouts = api.get_resource("/ip/hotspot/user", structure={"limit-uptime": TimedeltaField()})
timeouts.set(**{"limit-uptime": None})
timeouts.get(**{"limit-uptime": None})  # type: ignore
assert_type(timeouts.get()[0]["limit-uptime"], timedelta | None)

# A structure mixing field types gives a resource whose values' types aren't tracked.
mixed = api.get_resource("/ip/address", structure={"disabled": BooleanField(), "comment": StringField(), "mtu": IntegerField()})
assert_type(mixed, RouterOsResource[Any, Any])  # Any: the stub's type for a mixed structure
