# Automatically generated by pb2py
from .. import protobuf as p


class ECDHSessionKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 62
    FIELDS = {
        1: ('session_key', p.BytesType, 0),
    }

    def __init__(
        self,
        session_key: bytes = None
    ) -> None:
        self.session_key = session_key
