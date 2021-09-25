

from typing import Optional
from .symbol import *
from .expression import *
from dataclasses import make_dataclass, field


from .expression_typed import TypedExpression

Blank = TypedExpression("Blank", head=Expression)
BlankSequence = TypedExpression("BlankSequance", head=Expression)
BlankNullSequance = TypedExpression("BlankNullSequence", head=Expression)
Pattern = TypedExpression("Pattern", sym=Symbol, obj=Expression)

Missing("Missing", reason = String)

Optional = HeadType("Optional", )


def match_q(form, expr: Expression) -> bool:
    p
