from cv2.cv2 import GMat, GOpaqueT, gapi_streaming_queue_capacity

SYNC_POLICY_DONT_SYNC: int
SYNC_POLICY_DROP: int
sync_policy_dont_sync: int
sync_policy_drop: int

queue_capacity = gapi_streaming_queue_capacity

def desync(g: GMat) -> GMat: ...
def seqNo(arg1: GMat) -> GOpaqueT: ...
def seq_id(arg1: GMat) -> GOpaqueT: ...
def size(src: GMat) -> GOpaqueT: ...
def timestamp(arg1: GMat) -> GOpaqueT: ...
