#!/usr/bin/env python3
"""
Set is a collection which is unordered and unindexed(i.e., assignment to particular index is not possible).
 No duplicate members. In Python sets are written with curly brackets.
"""
from typing import Any


thisset: set[Any] = {"apple", "banana", "cherry", 123, 123}
# thisset[0] = "wow"  # TypeError: 'set' object does not support item assignment
print(thisset)  # {123, 'apple', 'banana', 'cherry'}
