#!/usr/bin/env python3
"""
Tuple is a collection which is ordered and unchangeable/unindexed(i.e., assignment to particular index
 is not possible). Allows duplicate members. In Python tuples are written with round brackets.
"""

"""
from typing import Literal

tup1: tuple[Literal[12], Literal[12], float, Literal["wow"]] = (12, 12, 34.56, "wow")
tup2: tuple[Literal["abc"], Literal["xyz"], Literal[123]] = ("abc", "xyz", 123)
# So let's create a new tuple as follows
tup3: tuple[
    Literal[12],
    Literal[12],
    float,
    Literal["wow"],
    Literal["abc"],
    Literal["xyz"],
    Literal[123],
] = (
    tup1 + tup2
)
"""


tup1 = (12, 12, 34.56, "wow")
tup2 = ("abc", "xyz", 123)

# Following action is not valid for tuples
# tup1[0] = 100  # TypeError: 'tuple' object does not support item assignment

tup3 = tup1 + tup2
print(tup3)  # (12, 12, 34.56, 'wow', 'abc', 'xyz', 123)
