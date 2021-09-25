from typing import Callable, TypeVar, Any

from smartcast.symbols import NULL


def identiy(x):
    return x

def null_coalesce(*values):
    for v in values:
        if v is not None:
            return v
    return None

_TI = TypeVar("_TI")
_TO = TypeVar("_TO")

# def composition(f1:Callable[[_TI], Any], *funcs: Callable, fn: Callable[[Any], _TO]) -> Callable[[_TI], _TO]:
#     functions = [f1] + funcs + [fn]
#     def fun(value: _TI):
#         x = value
#         for f in functions:
#             x = f(x)
#         return x
#     return fun


def If(condition, true, false = None, default = Exception):
    if condition == True:
        return true
    if condition == False:
        return false
    if isinstance(default, Exception):
        raise default
    return default
    

def composition(f1:Callable[[_TI], Any], functions: Callable) -> Callable[[_TI], _TO]:
    def fun(value: _TI):
        x = f1(value)
        for f in functions:
            x = f(x)
        return x
    return fun


def logical_not(value):
    assert value is bool, "logical not only works on bool"
    return not value

def construct(f, *args):
    return f(*args)

def apply(function, expr: list, levelspec = None):
    if levelspec is None or levelspec == [0]:
        return function(*expr)
    if levelspec is int:
        return apply(function, expr, {1, levelspec})

