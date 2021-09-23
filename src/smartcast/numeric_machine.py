from ctypes import c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong
from ctypes import c_byte, c_short, c_int, c_long, c_longlong
from ctypes import c_float, c_double, c_longdouble
import numbers

from typing import Sequence, Union

from smartcast.abstract import get_abstract_methods
from .meta_foward import forward

C_UINT_TYPES = {c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong}
C_SINT_TYPES = {c_byte, c_short, c_int, c_long, c_longlong}
C_FLOAT_TYPES = {c_float, c_double, c_longdouble}
C_INT_TYPES = C_UINT_TYPES | C_SINT_TYPES
C_NUMBER_TYPES = C_INT_TYPES | C_FLOAT_TYPES
PYTHON_NUMBER_TYPES = {float, int}
NUMBER_TYPES = C_NUMBER_TYPES | C_NUMBER_TYPES

NativeIntegerSigned = Union[c_byte, c_short, c_int, c_long, c_longlong]
NativeIntegerUnsigned = Union[c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong]
NativeInteger = Union[NativeIntegerSigned, NativeIntegerUnsigned]
NativeInexactNumber = Union[float, c_float, c_double, c_longdouble]
NativeNumber = Union[NativeInexactNumber, NativeInteger]

def type_code(t) -> str:
    "get the array type code for a number"
    if t is float:
        return 'd'
    if t is int:
        raise TypeError("int is a varible sized big int and can't be put into an array")
        return 'q' # signed long long
    return t._type_




@forward
class MachineNumber(numbers.Real):
    def __init__(self, kind = c_double, value = 0) -> None:
        self._value = kind(value)
        super().__init__()

    @property
    def kind(self):
        return type(self._value)

    @property
    def value(self):
        return self._value.value

    def __float__(self) -> float:
        return float(self._value.value)

mn = MachineNumber(32, type = c_int)