from ssl import *

# for simplicity we trust that gevent's implementation matches the stdlib version exactly
# for the most part they just copy all the symbols anyways and re-implment the few that
# need to work differently. The only potentially problematic symbol is SSLSocket, since
# it derives from gevent's socket, rather than the stdlib one. SSLContext derives from
# the stdlib SSLContext. Since we already punted on socket, we don't need to change
# anything here either, until we decide that we can't punt on socket.
