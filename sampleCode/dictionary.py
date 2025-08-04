#!/usr/bin/env python3
"""
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
 In Python dictionaries are written with curly brackets, and they have keys and values.
"""
from typing import Any

# Dictionary operations
thisdict: dict[str, Any] = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
thisdict["brand"] = "Ferrai"
print(thisdict)  # {'brand': 'Ferrai', 'model': 'Mustang', 'year': 1964}
