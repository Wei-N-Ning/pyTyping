from annotation import primitives
from annotation import classes
from annotation import functions
from annotation import containers
from annotation import aliases_references
from annotation import immutable
import unittest
import dataclasses


class TestAnnotation(unittest.TestCase):
    def test_classes(self):
        classes.MyClass()

    def test_functions(self):
        self.assertFalse(functions.send_email([''], '', [], []))

    def test_containers(self):
        containers.demo()

    def test_immutable(self):
        ct = immutable.Contract('doom', 'e1m1')
        self.assertEqual('doom at e1m1', ct())

    def test_dataclass(self):
        dc = classes.InventoryItem('a', 1.0, 1)
        self.assertEqual(dataclasses.astuple(dc), ('a', 1.0, 1))
