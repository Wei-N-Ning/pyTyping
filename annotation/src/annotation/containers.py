from typing import Tuple, NamedTuple
from collections import namedtuple


# old way of defining a named tuple:
# Record = namedtuple('Record', ['id', 'name', 'value'])
# FP Python P/44:
class Record(NamedTuple):
    id: int
    name: str
    value: int


def demo() -> None:
    t1: Tuple[int, str] = (0, '')
    t2: Record = Record(1, 'idd', 12)
