#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
      print "Total Employee %d" % Employee.empCount

   def displayAge(self):
      print "Employee Age %d" % self.age

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
print getattr(emp1, 'age')    # Returns value of 'age' attribute
emp1.displayAge()
print hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
delattr(emp1, 'age')    # Delete attribute 'age'
print hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
print Employee.__doc__