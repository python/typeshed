import threading
from _typeshed import Incomplete

class Producer(threading.Thread):
    bootstrap_servers: Incomplete
    topic: Incomplete
    stop_event: Incomplete
    big_msg: Incomplete
    def __init__(self, bootstrap_servers, topic, stop_event, msg_size) -> None: ...
    sent: int
    def run(self) -> None: ...

class Consumer(threading.Thread):
    bootstrap_servers: Incomplete
    topic: Incomplete
    stop_event: Incomplete
    msg_size: Incomplete
    def __init__(self, bootstrap_servers, topic, stop_event, msg_size) -> None: ...
    valid: int
    invalid: int
    def run(self) -> None: ...

def get_args_parser(): ...
def main(args) -> None: ...
