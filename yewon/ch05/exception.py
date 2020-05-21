try:
  a = 63 / 0
except ZeroDivisionError as err:
  print(err, end=" ")
  print("라는 에러가 발생했다! 주의하자!")

try:
  b = [1, 2, 3]
  c = b[4]
except IndexError:
  print("IndexError가 발생했다!")

try:
  d = 36 / 0
except:
  print("어떤 에러가 발생했다! 근데 뭔 에러인지 정확히는 모른다!")

try:
  print("A")
  print("B")
  print("C")
except:
  print("에러가 발생했다!")
else:
  print("에러가 발생하지 않았다!")
finally:
  print("에러가 발생했든 안 발생했든 실행되는 문장이다! 졸리다!")

try:
  f = open('a.txt', 'r')
except FileNotFoundError as err:
  print(err)
else:
  data = f.readline() # 한줄만
  print(data)
finally:
  f.close()

try:
  f = open('b.txt', 'r')
except FileNotFoundError:
  pass
else:
  data = f.readline() # 한줄만
  print(data)
finally:
  f.close()

# 오류 일부러 발생시키기
class Bird:
  def fly(self): # '꼭 메서드 오버라이딩 해야 한다.'는 것을 나타낸다.
    raise NotImplementedError # 꼭 작성해야하는 부분이 구현되지 않았을 때 일부러 오류를 발생시키기 위해 사용한다.

# class Eagle(Bird):
#   pass # 아무것도 안함
# eagle = Eagle()
# eagle.fly()

class Sparrow(Bird):
  def fly(self):
    print("참새 난다!")
sparrow = Sparrow()
sparrow.fly()