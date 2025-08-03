class MyClass:
    """Basic class definition"""

    x = 5


print("MyClass:" + str(MyClass))
print("x:" + str(MyClass.x))
p1 = MyClass()
print("p1:" + str(p1))
print("p1.x:" + str(p1.x))
# Expected output:
# class_test % python3 c1.py
# MyClass:<class '__main__.MyClass'>
# x:5
# p1:<__main__.MyClass object at 0x100795890>
# p1.x:5
