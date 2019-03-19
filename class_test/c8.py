#!/usr/bin/python
class Parent:        # define parent class
   'define parent class'
   parentAttr = 100
   def __init__(self):
      self.name = "Parent"
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

   def displayParentEmployee(self):
      print "Name : ", self.name

class Child(Parent): # define child class
   'define child class'
   def __init__(self):
      self.name = "Child"
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

   def displayChildEmployee(self):
      print "Name : ", self.name

c = Child()          # instance of child
print "isinstance(c,Child):"+str(isinstance(c,Child))
print "isinstance(c,Parent):"+str(isinstance(c,Parent))
print "issubclass(Child,Parent):"+str(issubclass(Child,Parent))
print "issubclass(Parent,Child):"+str(issubclass(Parent,Child))
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.displayChildEmployee()
#c.displayParentEmployee() # AttributeError: Child instance has no attribute 'name'
p = Parent()
p.displayParentEmployee()

print "Child.__doc__:", Child.__doc__
print "Child.__name__:", Child.__name__
print "Child.__module__:", Child.__module__
print "Child.__bases__:", Child.__bases__
print "Child.__dict__:", Child.__dict__