from dataclasses import field, make_dataclass

from .expression import Expression
from .symbol import symbol_q, Symbol


def TypedExpression(name, **params):
    symbol = name if symbol_q(name) else Symbol(name)

    fields = [(name, typeof, field(default=None)) for name, typeof in params.items()]
    fields = [("head", type(symbol), field(default=symbol, init=False))] + fields
    cls = make_dataclass(name, fields=fields, bases=(Expression,))

    cls.SYMBOL = symbol

    # def __init__(self, *args, **kwargs):
    #     super(self).__init__(symbol, *args, **kwargs)
    # cls.__init__ = __init__
    return cls
