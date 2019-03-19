import sys, os
currentPath = os.path.dirname(os.path.realpath(__file__))
print currentPath
print sys.path
print sys.path.insert(0, os.path.join(currentPath , '..'))
print sys.path
print sys.path.insert(0, os.path.join(currentPath , '..\\backup'))
print sys.path
print currentPath
def sample(a,b="venki"):
        print a
        print b
        c = str(a) + b
        print c
        print __name__ 
        print __file__ 

sample(10)
