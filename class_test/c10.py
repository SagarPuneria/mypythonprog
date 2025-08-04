#!/usr/bin/env python3


class JustCounter:
    """Private attributes and name mangling"""

    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount) #AttributeError: JustCounter instance has no attribute '__secretCount'
print(counter._JustCounter__secretCount)
