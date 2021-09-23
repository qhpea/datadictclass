def is_type(value):
    return isinstance(value, type)

def type_of(value):
    "return type of value. if value is type returns value"
    return value if is_type(value) else type(value)

def instance_or_type_of(typeof, value):
    return isinstance(value, typeof) or ( is_type(value) and issubclass(value, typeof))

from numbers import Number

def number_q(value):
    return isinstance(value, Number)

def exception_q(value):
    return instance_or_type_of(value, BaseException )