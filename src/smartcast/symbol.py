import dataclasses
from sys import prefix
from .mic_util import create_uuid
from .iter import sequence_q

@dataclasses
class Symbol:
    name: str

def unique(prefix = ""):
    if sequence_q(prefix):
        return map(unique, prefix)
    return Symbol(create_uuid(prefix))