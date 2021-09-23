from ctypes import c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong
from ctypes import c_byte, c_short, c_int, c_long, c_longlong
from ctypes import c_float, c_double, c_longdouble
from typing import List, Type, Union

from numbers import Integral, Number, Real

from smartcast.abstract import get_abstract_methods
from .types import type_of

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
PythonNumber = Union[int, float]

Integer = Union[int, NativeInteger]
InexactNumber = Union[float, NativeInexactNumber]

AnyNumber = Union[PythonNumber, NativeNumber]


NUMERIC_TYPE_FUNCTIONS_NAMES = [
    "add",
    "sub",
    "mul",
    "matmul",
    "truediv",
    "floordiv",
    "mod",
    "divmod",
    "pow",
    "lshift",
    "rshift",
    "and",
    "xor",
    "or"
]



def c_as_python(value):
    assert type(value) in C_NUMBER_TYPES, "must be a machine number type"
    return value.value



def integer_q(value):
    if value is int:
        return True
    
    typeof = type_of(value)
    return issubclass(typeof, Integral) or typeof in C_INT_TYPES 


def inexact_number_q(value):
    return value is float or type(value) in C_FLOAT_TYPES


def c_number_q(value):
    return type(value) in C_NUMBER_TYPES

def machine_number_q(value):
    return value is float or c_number_q(value)

def python_number_q(value):
    return isinstance(value, Number)

def number_q(v):
    "checks if value represents a number"
    return python_number_q(v) or machine_number_q(v)


def python_type_for_c_number_type(c_number_type):
    return type(c_number_type(0).value)

def number_as_python(value):
    if python_number_q(value):
        return value
    return c_as_python(value)



def as_int(value: NativeInteger):
    assert integer_q(value)
    if value is int:
        return value
    return int(value.value)


def as_float(value):
    if value is float:
        return value
    return float(value.value)


def n(value):
    assert number_q(value)
    if value is float:
        return value
    if integer_q(value):
        return float(as_int(value))


def plus(a, b):
    return number_as_python(a) + number_as_python(b)

def subtract(a, b):
    return number_as_python(a) - number_as_python(b)

def set(a, value):
    a.value = value
    return value

def times_by(a, b):
    return set(a, a.value * number_as_python(b))

def add_to(a, b):
    return set(a, a.value + number_as_python(b))

def subtract_from(a, b):
    return set(a, a.value - number_as_python(b))

def divide_by(a, b):
    return set(a, a.value / number_as_python(b))

def increment(a):
    pre = number_as_python(a)
    add_to(a, 1)
    return pre

def pre_increment(a):
    return add_to(a, 1)




def postive(n):
    return n > 0


def negative(n):
    return n < 0


def non_positive(n):
    return not postive(n)


def non_negative(n):
    return not negative(n)


