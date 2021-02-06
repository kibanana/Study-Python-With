# -*- coding: utf-8 -*- 

# all()
# iterable(반복 가능한) 자료형을 인수로 받는다. -> 리스트, 튜플, 문자열, 딕셔너리, 집합
# 모두 참이면 True, 아니면 False 리턴
print(all([1, 2, 3]))
print(all([0, 1, 2])) # 0
print(all([None, True, True])) # None
print(all([False, True, True])) # False
print(all([None, False, True])) # None, False

# any()
# 하나라도 참이면 True, 아니면 False 리턴
print(any([1, 2, 3])) # 1, 2, 3
print(any([0, 1, 2])) # 1, 2
print(any([None, True, True])) # True
print(any([False, True, True])) # True
print(any([None, False, 1])) # 1