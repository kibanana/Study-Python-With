from random import random, randint, choice, shuffle

# 0.0 ~ 1.0 실수 중 난수값
print(random())

# 1 ~ 10 정수 중 난수값
print(randint(1, 10))

# 1 ~ 55 정수 중 난수값
print(randint(1, 55))

data = [16, 17, 22, 23, 24, 25, 26, 27]
data2 = data[0:]
data3 = data[0:]

# 1)
def random_pop(data):
  number = randint(0, len(data)-1)
  return data.pop(number) # data 배열에서 무작위 값을 뽑고 삭제(pop)한다.

while data:
  print(random_pop(data))

print()

# 2)
def random_choice(data):
  number = choice(data)
  data.remove(number)
  return number

while data2:
  print(random_choice(data2))


for i in range(5):
  shuffle(data3)
  print(data3)