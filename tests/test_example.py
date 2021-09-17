from smartcast import normal, cast
from typing import List, Optional, Union
import json
from dataclasses import dataclass
from enum import Enum, auto


class Option(Enum):
    A = auto()
    B = auto()


@dataclass
class Config:
    value: Option


def test_simple():
    value = Config(Option.A)
    nobj = normal(value)
    jstr = json.dumps(nobj)
    jobj = json.loads(jstr)
    revalue = cast(jobj, Config)
    assert value == revalue
