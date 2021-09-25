from typing import Type

from smartcast.symbols import NUMBER
from .symbol import symbol_q, Symbol
from .expression_typed import TypedExpression

String = TypedExpression("String")
Number = TypedExpression(NUMBER)
TypedExpression = 