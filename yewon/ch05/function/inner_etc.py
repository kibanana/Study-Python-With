# -*- coding: utf-8 -*- 

from copy import copy
from class_park import HousePark

# dir()
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
# print(dir(HousePark)) # lastname, firstname은 안보인다.
# print()
# hp = HousePark("ㅇㅇ")
# print(dir(HousePark)) # lastname, firstname은 안보인다.
# print()
# print(dir([1, 2, 3]))
# print()
# print(dir({ "a": 1 }))
# print()

# enumerate()
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아서 인덱스 값을 포함하는 enumerate 객체를 리턴
# for문 같은 데에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요하면 사용한다.
# enumerate 객체는 한 번 쓰면 끝인 것 같다.
temp = ['A', 'B', 'C']
temp2 = temp
result1 = enumerate(temp)
result2 = enumerate(temp)
print(result1) # <enumerate object at ~>
print(result2) # <enumerate object at ~>

for i, j in result1:
  print(i, j)
  # 0, A
  # 1, B
  # 2, C

for i in result2:
  print(i)
  # (0, 'A')
  # (1, 'B')
  # (2, 'C')

# id()
print(id(temp)) # temp와 temp2의 주소값은 같다
print(id(temp2)) # temp와 temp2의 주소값은 같다
print(id(result1))
print(id(result2))

# input()
# print(input("배고픈데 뭘 먹을까: "))

# isinstance(), issubclass()
# 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받아서 True 또는 False를 리턴
class A:
  def __init__(self):
    self.a = 'A'

class B:
  def __init__(self):
    self.b = 'B'

class BB(B):
  def __init__(self):
    self.bb = 'BB'

classA = A()
classB = B()
classBB = BB()

print(isinstance(classA, B)) # False, classA는 B의 객체가 아니기때문에
print(isinstance(classA, A)) # True, classA는 A의 객체이기때문에
print(isinstance(classB, B)) # True, classB는 B의 객체이기때문에
print(isinstance(classB, BB)) # False, classB는 BB의 객체가 아니기때문에

print(issubclass(A, B)) # False
print(issubclass(B, A)) # False
print(issubclass(B, BB)) # False
print(issubclass(BB, B)) # True -> (Subclass, Superclass) 순

# len()
print(len("Python is short")) # 15
print(len([1, 2, 3])) # 3
print(len((6, 3))) # 2

# list()
# 리스트 복사 용도로도 사용할 수 있다.
print(list("Python is short"))

# map()
# 함수와 반복가능한iterable 자료형을 입력으로 받아서 2를 1로 실행한 결과를 묶어서 리턴
# 1)
def double(number_list):
  result = []
  for num in number_list:
    result.append(num * 2)
  return result

print(double([5, 6, 7]))

# 2)
def double_simple(i): return i * 2
print(list(map(double_simple, [5, 6, 7])))

# 3)
print(list(map(lambda i: i*2, [5, 6, 7])))

# max(), min()
# 반복가능한iterable 자료형을 입력으로 받아서 최대값/최소값 리턴
a = [1, 2, 3]
print(max(a)) # 3
print(max("yewon")) # y
print(min(a)) # 1
print(min("yewon")) # e

# tuple()
# list()와 비슷하게 반복가능한iterable 자료형을 입력받아서 튜플 형태로 바꿔서 리턴
print(tuple("Python"))
print(tuple([5, 3, 1]))

# zip()
# 동일한 개수로 이루어진 자료형을 묶는다
print(list(zip([10, 20, 30], [300, 200, 100], [50, 100, 150])))
print(list(zip("ABC", "DEF", "GHI")))