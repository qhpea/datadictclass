
import dataclasses
import typing
import enum
import smartcast


class Ez(enum.Enum):
    MAX = enum.auto()
    MIN = enum.auto()


@dataclasses.dataclass
class Yay:
    wow: bool = True

def horray():
    return {10: Yay(wow = False)}
@dataclasses.dataclass
class Hey:
    req: bool
    pain: Ez = Ez.MAX
    nice: typing.Dict[int, Yay] = dataclasses.field(default_factory=horray)
    maybe: typing.Optional[bool] = None


def test_cast():
    value = [Hey(True)]
    normal = smartcast.normal(value)
    revalue = smartcast.cast(normal, typing.List[Hey])
    for a, b in zip(value, revalue):
        assert a == b

def test_2():
    value = Hey(True, maybe=True,pain=Ez.MIN, nice = {})
    normal = smartcast.normal(value)
    revalue = smartcast.cast(normal, Hey)
    assert value == revalue