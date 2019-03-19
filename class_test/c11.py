#!/usr/bin/python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def nxt(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)
print(nxt(myiter))
print(nxt(myiter))
print(nxt(myiter))
print(nxt(myiter))
print(nxt(myiter))