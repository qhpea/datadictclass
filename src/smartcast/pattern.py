

from typing import Optional
from .symbol import *
from .expression import *
from dataclasses import make_dataclass, field


def HeadType(name, **params):
    symbol = Symbol(name)

    fields = [(name, typeof, field(default=None, type = typeof)) for name, typeof in params.items()]
    fields.append("head", type(symbol), field(default=symbol, init=False))

    cls = make_dataclass(name, fields=fields, bases=(Expression,))


    cls.SYMBOL = symbol

    # def __init__(self, *args, **kwargs):
    #     super(self).__init__(symbol, *args, **kwargs)
    # cls.__init__ = __init__
    return cls


Blank = HeadType("Blank", head=Expression)
BlankSequence = HeadType("BlankSequance", head=Expression)
BlankNullSequance = HeadType("BlankNullSequence", head=Expression)
Pattern = HeadType("Pattern", sym=Symbol, obj=Expression)

Optional = HeadType("Optional", )


def match_q(form, expr: Expression) -> bool:
    p
