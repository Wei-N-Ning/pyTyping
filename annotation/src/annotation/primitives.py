from typing import List, Text
Vector = List[float]


def greeting(name: str) -> str:
    return 'Hello ' + name


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])

# prefer Text to str
t: Text = "iddqd"
