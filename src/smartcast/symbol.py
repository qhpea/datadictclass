import dataclasses
from sys import prefix

from .global_rule import rule
from .mic_util import create_uuid
from .iter import sequence_q

@dataclasses
class Symbol:
    name: str

@rule
def unique(prefix = ""):
    if sequence_q(prefix):
        return map(unique, prefix)
    return Symbol(create_uuid(prefix))

@rule
def symbol_q(value):
    return isinstance(value, Symbol)