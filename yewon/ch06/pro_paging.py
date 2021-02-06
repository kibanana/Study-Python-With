# -*- coding: utf-8 -*- 

def getTotalPage(n, perPage = 1):
  # 나머지가 0이면 + 1 하면 안된다.
  if n % perPage == 0:
    return n // perPage
  else:
    return n // perPage + 1

print(getTotalPage(100, 10))
print(getTotalPage(100))
print(getTotalPage(100, 3))