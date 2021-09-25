from dataclasses import MISSING
from .pattern import Blank

from smartcast.symbol import Symbol
from .symbols import NULL

def Function(body, params:List(Symbol()) = NULL, attrs: Blank() = NULL):
    pass

def List(body):
    return body

def Range(imin= 1, imax = NULL, di = 1):
    assert imax is not NULL
    return List(range(imin, imax + 1, di))


def Table(expr, rangespec):
    exprfor 

def Array(f, n, r = 1):
    zip(f, 