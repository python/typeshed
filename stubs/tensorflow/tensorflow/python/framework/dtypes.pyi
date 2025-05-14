import dataclasses

@dataclasses.dataclass(frozen=True)
class HandleData:
    shape_inference = None
    alias_id: int | None = None
