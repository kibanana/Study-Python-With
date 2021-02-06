# -*- coding: utf-8 -*- 

# filter(함수, 반복 가능한iterable 자료형)

a = [i for i in range(15)]

print(a)
print(type(a))

def more_than_five(number_list):
  result = []
  for i in number_list:
    if i > 5:
      result.append(i)
  return result

def more_than_five_filter(i):
  if i > 5:
    return i

print(more_than_five(a))
print(list(filter(more_than_five_filter, a)))
print(list(filter(lambda i: i > 5, a)))