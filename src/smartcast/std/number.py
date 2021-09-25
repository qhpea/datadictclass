from ctypes import Union
from .expression import Expression, typed
import typing
import numbers

@typed
class Number(Expression):
    value: Union[float, int, complex] = 0

@typed
def Plus(a: Number, b: Number):
    return Number(a.value + b.value)

import math

@typed
def Sqrt(z: Number) -> Number:
    return Number(math.sqrt(z.value))

@typed
def Abs(z: Number) -> Number:
    abs()