from typing import Iterator, Union, Optional, List, TypeVar, Callable, Iterable


# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)


# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2


# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f

# see this example also:
T_ = TypeVar('T_')
R_ = TypeVar('R_')
Value = Optional[T_]


# how to define callable's type hint:
# https://stackoverflow.com/questions/37835179/how-can-i-specify-the-function-type-in-my-type-hints
def maybe(x: Value, f: Callable[[Value], R_], defa: R_) -> R_:
    return defa if x is None else f(x)


# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


# You can of course split a function annotation over multiple lines
def send_email(address: Union[str, List[str]],
               sender: str,
               cc: Optional[List[str]],
               bcc: Optional[List[str]],
               subject='',
               body: Optional[List[str]] = None) -> bool:
    return False


# An argument can be declared positional-only by giving it a name
# starting with two underscores:
def quux(__x: int) -> None:
    pass


quux(3)  # Fine
# quux(__x=3)  # Error
