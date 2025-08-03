class Person:
    """Class with constructor (__init__)"""

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


p1 = Person("John", 36)

print("p1.name:" + p1.name)
print("p1.age:" + str(p1.age))

print("p1.name:", Person("John", 36).name)
print("p1.age:", Person("John", 36).age)
