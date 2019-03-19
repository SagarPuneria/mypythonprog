#!/usr/bin/python
'''
Tuple is a collection which is ordered and unchangeable/unindexed(i.e., assignment to particular index
 is not possible). Allows duplicate members. In Python tuples are written with round brackets.
'''
tup1 = (12, 12, 34.56, 'wow');
tup2 = ('abc', 'xyz', 123);

# Following action is not valid for tuples
# tup1[0] = 100; #TypeError: 'tuple' object does not support item assignment

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3; #(12, 12, 34.56, 'wow', 'abc', 'xyz', 123)