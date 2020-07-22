# dedicate this example to how to use typing.NamedTuple
# - how to define recursive type (Node -> Node ...)
# - How to assign default value to params

# sources:
# default param:
# https://stackoverflow.com/questions/11351032/namedtuple-and-default-values-for-optional-keyword-arguments

# recursive type:
# https://stackoverflow.com/questions/53845024/defining-a-recursive-type-hint-in-python

# what is forward reference:
# https://www.python.org/dev/peps/pep-0484/#forward-references

from typing import NamedTuple, Any
import unittest

class Node(NamedTuple):
    v: Any = None
    num_left: int = 0
    l: NamedTuple('Node') = None
    r: NamedTuple('Node') = None
    count: int = 1

class TestNode(unittest.TestCase):
    def test_default_value(self):
        self.assertEqual(1, Node().count)
        self.assertEqual(None, Node())
        self.assertEqual(10, Node(10).v)

if __name__ == '__main__':
    unittest.main()
