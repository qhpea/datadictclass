from .expression import Expression, typed
import typing


@typed
class List(Expression):
    "is magic"
    body: typing.List[Expression]

def Table():
    pass

