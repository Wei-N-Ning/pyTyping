# source: mypy cheatsheet
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

from dataclasses import dataclass


class MyClass:
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100

    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self) -> None:
        self.a = 1

    # For instance methods, omit type for "self"
    def my_method(self, num: int, str1: str) -> str:
        return num * str1


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    # __init__ is automatically added to the class

    # Note that this method is automatically added to the class: 
    # #it is not directly specified in the InventoryItem definition 

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
