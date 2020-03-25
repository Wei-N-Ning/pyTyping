from annotation import primitives
from annotation import classes
from annotation import functions
from annotation import containers
from annotation import aliases

import unittest


class TestAnnotation(unittest.TestCase):
    def test_classes(self):
        classes.MyClass()

    def test_functions(self):
        self.assertFalse(functions.send_email([''], '', [], []))

    def test_containers(self):
        containers.demo()
