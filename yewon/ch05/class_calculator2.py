# -*- coding: utf-8 -*- 

class Calculator:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def sum(self):
    return self.a + self.b
  def sub(self):
    return self.a - self.b
  def mul(self):
    return self.a * self.b
  def div(self):
    if self.b != 0:
      return self.a / self.b
    else:
      return 0

c = Calculator(6, 3)
print(c.sum())
print(c.sub())
print(c.mul())
print(c.div())