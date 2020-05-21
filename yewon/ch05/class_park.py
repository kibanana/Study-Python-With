class HousePark:
  def __init__(self, firstname):
    self.lastname = "박"
    self.firstname = firstname
  def fullname(self):
    return self.lastname + self.firstname
  def travel(self, destination):
    return "%s -> %s" % (self.fullname(), destination)
  def __add__(self, other):
    return "%s, %s이 동거하기 시작했습니다." % (self.fullname(), other.fullname())
  def __sub__(self, other):
    return "%s, %s이 동거를 그만뒀습니다." % (self.fullname(), other.fullname())
  def __mul__(self, other):
    return "%s, %s이 힘을 합해서 재산을 불렸습니다." % (self.fullname(), other.fullname())
  def __truediv__(self, other):
    return "%s, %s이 재산을 분할했습니다." % (self.fullname(), other.fullname())

park = HousePark("유연")
print(park.fullname())
print(park.travel("전라도"))

class HouseKim(HousePark):
  def __init__(self, firstname):
    self.lastname = "김"
    self.firstname = firstname

kim = HouseKim("연")
print(kim.fullname())
print(kim.travel("전라도"))

print(park + kim)
print(park * kim)

print(park - kim)
print(park / kim)