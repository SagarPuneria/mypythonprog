"""
Basic Python script with path manipulation

Python learning series % python3.11 -m venv .venv
% cd mypythonprog
mypythonprog % ../.venv/bin/python3 -m pylint sample.py
((.venv) )mypythonprog % source ../.venv/bin/activate && python -m pylint sample.py
((.venv) )mypythonprog % deactivate
mypythonprog % ../.venv/bin/python3 sample.py
mypythonprog % python3 sample.py
"""

import os
import sys
from typing import Any

currentPath = os.path.dirname(os.path.realpath(__file__))
print("currentPath:", currentPath)
print("sys.path before:", sys.path)
sys.path.insert(0, os.path.join(currentPath, ".."))
print("sys.path after inserting ..:", sys.path)
sys.path.insert(0, os.path.join(currentPath, "../backup"))
print("sys.path after inserting ../backup:", sys.path)
print("currentPath:", currentPath)


# def sample(a,b="venki"):
def sample(a: Any, b: str = "venki") -> None:
    """Add docstring here only"""
    print("a:", a)
    print("b:", b)
    c = str(a) + b
    print("c:", c)
    print("__name__:", __name__)
    print("__file__:", __file__)


sample(10)
