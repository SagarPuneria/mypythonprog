#!/usr/bin/python


class Employee:
    """Class attributes and built-in functions.
    Common base class for all employees"""

    empCount = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total Employee: {Employee.empCount}")
        # print("Total Employee %d" % Employee.empCount)

    def displayAge(self):
        if hasattr(self, "age"):
            print("Employee Age:", self.age)
        else:
            print("Employee Age: Not set")

    def displayEmployee(self):
        # print("Name : ", self.name, ", Salary: ", self.salary)
        print(f"Name: {self.name}, Salary: {self.salary}")
        # print("Name : %s, Salary: %d" % (self.name, self.salary))


# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCount()

print(
    # "'age' attribute exists:", hasattr(emp1, "age")
    f"'age' attribute exists: {hasattr(emp1, 'age')}"
)  # Returns true if 'age' attribute exists

if not hasattr(emp1, "age"):
    setattr(emp1, "age", 8)  # Set attribute 'age' at 8

if hasattr(emp1, "age"):
    print("getattr value:", getattr(emp1, "age"))  # Returns value of 'age' attribute

emp1.displayAge()

# When if condition inside displayAge is commented out,
# Then AttributeError: 'Employee' object has no attribute 'age'
emp2.displayAge()

if hasattr(emp1, "age"):  # Returns true if 'age' attribute exists
    print("deleting age attribute")
    delattr(emp1, "age")  # Delete attribute 'age'

print(
    # "'age' attribute exists:", hasattr(emp1, "age")
    f"'age' attribute exists: {hasattr(emp1, 'age')}"
)  # Returns true if 'age' attribute exists

print(Employee.__doc__)
