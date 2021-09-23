
from abc import ABCMeta
def get_abstract_methods(cls: type) -> frozenset:
    return getattr(cls, "__abstractmethods__", frozenset())
    #return cls.__abstractmethods__

import inspect
def get_methods(cls: type) -> frozenset:
    methods = inspect.getmembers(cls, predicate=inspect.ismethod)
    return frozenset((name for name, _ in methods))