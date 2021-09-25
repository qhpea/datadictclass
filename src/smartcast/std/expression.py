from dataclasses import dataclass
from abc import ABC, abstractmethod

class Expression(ABC):
    @property
    @abstractmethod
    def head(self) -> "Expression":
        raise NotImplementedError

    @property
    @abstractmethod
    def body(self) -> "Expression":
        raise NotImplementedError

def typed(cls):
    return dataclass(cls)

@typed
class Symbol(Expression):
    name: str