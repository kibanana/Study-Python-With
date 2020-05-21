class SimpleCalculator:
  def __init__(self):
    self.sum = 0
  def add(self, num):
    self.sum += num

class Calculator(SimpleCalculator): # 다중상속 가능
  def say(self):
    print(self.sum)

if __name__ == "__main__":
  test = Calculator()
  test.add(500)
  test.say()

  print(type(test))