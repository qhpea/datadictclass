
import dataclasses
import typing
import enum
import smartcast

class Ez(enum.Enum):
    MAX = enum.auto()
    PAIN = enum.auto()


@dataclasses.dataclass
class Hey:
    fun: str = "some"
    no: bool = True
    pain: Ez = Ez.MAX


def test_cast():
    smartcast.cast(smartcast.normal([Hey()]), typing.List[Hey])
