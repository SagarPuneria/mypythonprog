#!/usr/bin/python
'''
Set is a collection which is unordered and unindexed(i.e., assignment to particular index is not possible).
 No duplicate members. In Python sets are written with curly brackets.
'''
thisset = {"apple", "banana", "cherry", 123, 123}
#thisset[0] = "wow" #TypeError: 'set' object does not support item assignment
print thisset #set(['cherry', 123, 'banana', 'apple'])