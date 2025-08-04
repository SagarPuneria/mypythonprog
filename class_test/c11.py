#!/usr/bin/env python3

from typing import Self  # Import Self for type hinting


class MyNumbers:
    """Iterator protocol"""

    def __init__(self):
        print("Inside __init__")
        self.a = 1

    def __iter__(self) -> Self:
        print("Inside __iter__")
        self.a = 1
        return self

    def __next__(self) -> int:
        print("Inside __next__")
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
