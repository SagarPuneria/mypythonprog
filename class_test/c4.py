from typing import Any


class Person:
    """Self parameter variations"""

    def __init__(mysillyobject: "Person", name: Any, age: Any) -> None:
        """(class) Person: "Person" is self parameter variations"""
        mysillyobject.name: Any = name
        mysillyobject.age: Any = age

    def myfunc(abc: "Person") -> None:
        """(class) Person: "Person" is self parameter variations"""
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
print(p1.age)
p1.age = 40
print(p1.age)
