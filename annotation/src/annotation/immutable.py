from typing import NamedTuple, Text


# inspired by functional python programming P/122
# the argument of imperative style and FP style when using
# python's class;
# however I want to show that immutability is not compromised if
# using the inheriting-NamedTuple approach, where behavior (the
# encapsulation) still comes close to the data
class Contract(NamedTuple):
    who: Text
    where: Text

    def __call__(self):
        return f'{self.who} at {self.where}'
