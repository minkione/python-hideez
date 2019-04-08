# Automatically generated by pb2py
from .. import protobuf as p
from .HDNodePathType import HDNodePathType
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None


class MultisigRedeemScriptType(p.MessageType):
    FIELDS = {
        1: ('pubkeys', HDNodePathType, p.FLAG_REPEATED),
        2: ('signatures', p.BytesType, p.FLAG_REPEATED),
        3: ('m', p.UVarintType, 0),
    }

    def __init__(
        self,
        pubkeys: List[HDNodePathType] = None,
        signatures: List[bytes] = None,
        m: int = None
    ) -> None:
        self.pubkeys = pubkeys if pubkeys is not None else []
        self.signatures = signatures if signatures is not None else []
        self.m = m
