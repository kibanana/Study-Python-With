# -*- coding: utf-8 -*- 

# 리스트는 어떤 자료형이든 넣을 수 있다

#  리스트 만들기
odd = [1,5,7,9,11] # 홀수 리스트

# 빈 리스트
a = []
a = list()

print(odd)
print(odd[0])
print(odd[0]+odd[1])
print(odd[-1])

test = [1,2,3,['a','b','c']]
# 인덱싱
print(test[0])
print(test[3])
print(test[3][0])
print(test[-1][0])

# 슬라이싱
print(test[1:3])
print(test[1:])
print(test[3][2:])

# 리스트 더하기(연결하기)
print(odd + test)

# 리스트 반복하기
print(odd * 2)

print(str(test[0]) + "hi")
# print(test[0] + "hi") # error