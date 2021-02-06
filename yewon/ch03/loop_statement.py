# -*- coding: utf-8 -*- 

# while
i = 0
while i < 10:
  print(i)
  i += 1

j = 0
while j != 5:
  print('Hello')
  j = int(input()) # 5 입력할때까지

# for
# 1)
test_list = ['one', 'two', 'three']
for item in test_list:
  print(item)

# 2)
a = [(1, 2), (3, 4), (5, 6)]
for (before, after) in a:
  print(before + after)

# 3)
score = [90, 25, 67, 45, 80]
for s in range(len(score)):
  if score[s] >= 60:
    print("학생 %d 합격이다" % (s + 1))
  else:
    print("학생 %d 불합격이다" % (s + 1))

# 4) 구구단
for x in range(2, 10):
  for y in range(1, 10):
    print("{0} * {1} = {2}".format(x, y, x*y))
  print("=" * 30)

# 5) 리스트 내포
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

result2 = [num * 3 for num in a if num % 2 == 0]
print(result2)
