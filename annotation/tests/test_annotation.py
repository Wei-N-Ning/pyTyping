from annotation import primitives
from annotation import classes
from annotation import functions
from annotation import containers
import unittest


class TestAnnotation(unittest.TestCase):
    def test_classes(self):
        my_obj = classes.MyClass()

    def test_functions(self):
        self.assertFalse(functions.send_email([''], '', [], []))
