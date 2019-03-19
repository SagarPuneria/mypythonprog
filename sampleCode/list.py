#!/usr/bin/python
'''
List is a collection which is ordered and changeable/indexed.
 Allows duplicate members. In Python lists are written with square brackets.
'''
list1 = ['physics', 'chemistry', 1997, 2000, 2000];
print list1 #['physics', 'chemistry', 1997, 2000, 2000]
del list1[2];
print "After deleting value at index 2"
print list1 #['physics', 'chemistry', 2000, 2000]