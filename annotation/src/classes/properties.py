# this is an example showing how to define object property methods
# source: https://www.python-course.eu/python3_properties.php

# 1. use @property to define the getter method
#    the property is named after the method
# 2. use <property>.setter to define the setter method

import weakref

class Node:
    def __init__(self, v):
        self.val = v
        self._prev = None
        self.next = None

    @property
    def prev(self):
        return self._prev() if self._prev else None

    @prev.setter
    def prev(self, other):
        if other is not None:
            self._prev = weakref.ref(other)
        else:
            self._prev = other

    def link_to(self, other):
        if self.next is not None:
            self.next.prev = self.prev
        self.next = other
        if other is not None:
            other.prev = self

    def unlink(self):
        if self.next is not None:
            self.next.prev = self.prev
        if self.prev is not None:
            self.prev.next = self.next
        self.next = None
        self.prev = None

    def find(self, val, reverse=False):
        ptr = self
        while ptr is not None:
            if ptr.val == val:
                return ptr
            if reverse:
                ptr = ptr.prev
            else:
                ptr = ptr.next
