#!/usr/bin/env python3
"""
List is a collection which is ordered and changeable/indexed.
 Allows duplicate members. In Python lists are written with square brackets.
"""
from typing import Any

# List operations
list1: list[Any] = ["physics", "chemistry", 1997, 2000, 2000]
print(list1)  # ['physics', 'chemistry', 1997, 2000, 2000]
del list1[2]
print("After deleting value at index 2")
print(list1)  # ['physics', 'chemistry', 2000, 2000]
list1[0] = "biology"  # Change existing item
print(list1)  # ['biology', 'chemistry', 2000, 2000]
list1.append("math")  # Add new item
print(list1)  # ['biology', 'chemistry', 2000, 2000, 'math']
