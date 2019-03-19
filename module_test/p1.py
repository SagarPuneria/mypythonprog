#!/usr/bin/python
import sys, os
print sys.path
currentPath = os.path.dirname(os.path.realpath(__file__))
print currentPath

sys.path.insert(0, os.path.join(currentPath , 'spt'))
#sys.path.insert(0, os.path.join(currentPath , '\\spt'))
print sys.path
# Import module support
import support
# Now you can call defined function that module as follows
support.print_func("Zara")

import support2
# Now you can call defined function that module as follows
support2.print_func("Zara 2")
