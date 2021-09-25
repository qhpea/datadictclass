

from dataclasses import field
from typing import List, Type
from .symbol import *
from .fun import identiy

from .symbols import *


LevelSpec = Type("LevelSpec")

import dataclasses

class Expression:
    head = NULL

    @property
    def body(self):
        return dataclasses.astuple(self)

    @property
    def length(self):
        return len(self.body) 
    
    def __repr__(self) -> str:
        return f"{self.head}[{self.body}]"

def head(expr: Expression):
    return expr.head

@dataclasses
class ListExpression(Expression):
    head = LIST
    body: List[Expression] = {}

Expression.SYMBOL = None

def level(expr, levelspec: LevelSpec, f = identiy):
    pass

def depth(expr, heads = False):
    pass


def flatten(iterable: Expression, n = 1) -> Expression:
    for v in iterable:
        if False:
            pass

def head(expr):
    return expr.head

def position(expr, value, levelspec = NULL, n = INFINITY):
    pass


def operate(p, expr):
    new_head = p(head(expr))
    return Expression(head = )
    (body(expr))