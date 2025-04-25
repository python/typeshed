from typing import Literal


class EOFType:
    def __bool__(self) -> Literal[False]:
        return False

    def __len__(self) -> Literal[0]:
        return 0

    def _repr(self) -> Literal["<grpc.aio.EOF>"]:
        return "<grpc.aio.EOF>"

    def __repr__(self) -> Literal["<grpc.aio.EOF>"]:
        return self._repr()

    def __str__(self) -> Literal["<grpc.aio.EOF>"]:
        return self._repr()
