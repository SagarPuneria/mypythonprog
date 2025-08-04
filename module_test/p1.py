#!/usr/bin/env python3
import sys, os

# Module importing and path manipulation

# support and support2 are custom modules
# support is a nested module structure
# support2 is a simple module with function

# import support # ModuleNotFoundError: No module named 'support'
import support2

# Now you can call defined function that module as follows
support2.print_func("Zara 2")

print("======================")
print("1 sys.path:", sys.path)

currentPath = os.path.dirname(os.path.realpath(__file__))
print("======================")
print("currentPath:", currentPath)

sys.path.insert(0, os.path.join(currentPath, "spt"))
# sys.path.insert(0, os.path.join(currentPath , '\\spt'))
print("======================")
print("2 sys.path:", sys.path)

print("======================")
# Import module support
import support

# Now you can call defined function that module as follows
support.print_func("Zara")
