# -*- coding: utf-8 -*- 

import sys
from copy import copy

print(type(3)) # 상수값이 아닌, 정수형 객체
print(type('hello')) # 상수값이 아닌, 문자열형 객체

a = 63
b = 63
print(a is b) # a,b가 동일한 객체를 가리키는지 판단한다 -> Reference Count = 2
print(a is 63)

print(sys.getrefcount(63)) # 입력한 자료형에 대한 참조 개수
c = 63
print(sys.getrefcount(63))

s1, s2 = ('javascript', 'typescript')
(s3, s4) = 'python', 'snake';

print(s1, s2, s3, s4)

[s5, s6] = ['java', 'kotlin']
print(s5, s6)

s7 = s8 = s9 = 63
print(s7, s8, s9)

s6, s7 = s7, s6
print(s6, s7)

# 값을 메모리에서 지운다 = Reference Count를 줄인다
# 가비지 컬렉션 동작은 파이썬이 자동으로 하므로 사람이 신경쓸 필요는 없다
print(sys.getrefcount(63))
del(s6, s8, s9)
print(sys.getrefcount(63))

# 아래와 같은 방식으로 리스트를 복사하려고 하면 동일한 리스트를 가리키게 되므로
# 하나의 값을 변경해도 두 값이 모두 변경된다
list1 = ['a', 'b', 'c']
list2 = list1
list2[0] = 'y'
print(list1, list2)
print(list1 is list2)

list3 = ['d', 'e', 'f']
list4 = list3[:]
list5 = copy(list4)
list3[0] = 'x';
list4[0] = 'y';
list5[0] = 'z';
print(list3)
print(list4)
print(list5)
print(list3 is list4)
print(list4 is list5)
print(list3 is list5)