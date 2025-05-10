import gevent
from gevent.resolver import cares

print(cares.ares_host_result(1, [1, 2, "asd"]))
