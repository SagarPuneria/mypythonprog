#!/usr/bin/env python3


class Point:
    """Object lifecycle and destructor"""

    def __init__(self, x: int = 1, y: int = 2):
        self.x = x
        self.y = y
        print(f"Point created: ({self.x}, {self.y})")

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt2
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the obejcts
del pt1
print(id(pt2), id(pt3))  # prints the ids of the obejcts
del pt2
print(id(pt3))  # prints the ids of the obejcts
del pt3
