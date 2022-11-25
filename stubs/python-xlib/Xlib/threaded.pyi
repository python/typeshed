# We change the allocate_lock function in Xlib.support.lock to
# return a basic Python lock, instead of the default dummy lock
from Xlib.support import lock as lock
