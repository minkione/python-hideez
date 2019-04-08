# Automatically generated by pb2py
from .. import protobuf as p


class FirmwareRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 8
    FIELDS = {
        1: ('offset', p.UVarintType, 0),
        2: ('length', p.UVarintType, 0),
    }

    def __init__(
        self,
        offset: int = None,
        length: int = None
    ) -> None:
        self.offset = offset
        self.length = length
