# source:
# functional python programming P/70
# the type variable T_ created with TypeVar function is used
# to clarify precisely how ....
# ** Otherwise I run into Any to Any problem!
# see iter_pairs:
# the return type IterTT must refer to the same type as the input
# IterT

from typing import TypeVar, Iterable, Tuple, Any
import itertools

T_ = TypeVar('T_')
TT = Tuple[T_, T_]
IterTT = Iterable[TT]
IterT = Iterable[T_]


def iter_pairs(it: IterT) -> IterTT:
    first, second = itertools.tee(it, 2)
    try:
        next(second)
    except StopIteration:
        return iter(tuple())
    return zip(first, second)
