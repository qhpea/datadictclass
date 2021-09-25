from typing import Callable, Type, TypeVar
from .global_rule import rule

_T = TypeVar("_T")

@rule
def equal_to(y: _T) -> Callable[[_T], bool]:
    return y.__eq__

@rule
def greater_equal_than(y: _T) -> Callable[[_T], bool]:
    return y.__ge__
