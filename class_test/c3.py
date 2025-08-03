class Person:
    """Class with constructor (__init__) and method"""

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def myfunc(self) -> None:
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()
Person("John", 36).myfunc()
