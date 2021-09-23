import array

from typing import Type
from .iter import sequence_q, take, first
from .number import type_code

All = Type("All")

def nest_while(transform, start, test, m = 1):
    out = [start]
    while test(*take(out, -m)):
        out.append(transform(*take(out, -m)))
    return out


def shape(value):
    return nest_while(first, value, sequence_q)
    
from array import array

class NumericArray:
    def __init__(self, value, item_type) -> None:
        self.shape = shape(value)
        self.items_type = item_type
        self.array = array(typecode= type_code(item_type), )