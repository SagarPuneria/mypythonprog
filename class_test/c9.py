#!/usr/bin/env python3
class Vector:
    """Operator overloading"""

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"Vector: ({self.a}, {self.b})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
print("v1 =>", v1)
v2 = Vector(5, -2)
print("v2 =>", v2)
v3 = v1 + v2
print("v3 =>", v3)
