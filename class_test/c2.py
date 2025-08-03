class Person:
    """Class with constructor (__init__)"""

    def __init__(self, name: str, age: int, city: str = "Hyderabad") -> None:
        """city is an optional parameter with a default value"""
        print("$$$$Initializing Person object$$$$")
        self.name: str = name
        self.age: int = age
        self.city: str = city


# Efficient way, calling class Person one time
p1 = Person("John", 36)
print("p1.name:" + p1.name)
print("p1.age:" + str(p1.age))
print("p1.city:" + p1.city)

# Inefficient way, calling class Person multiple times
print("p1.name:", Person("John", 36).name)
print("p1.age:", Person("John", 36).age)
print("p1.city:", Person("John", 36, "Bangalore").city)
