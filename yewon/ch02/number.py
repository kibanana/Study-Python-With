# -*- coding: utf-8 -*- 

a = -123

b = 123.456

c = 4.24E10

d = 0o75
# 당연히 8부터는 오류남

e = 0xA7
# 당연히 16부터는 오류남

f1 = 1+2j
f2 = 1+2J
# j도 쓰고 J도 씀
f1.real # 복소수의 실수부분
f1.imag # 복소수의 허수부분
f1.conjugate() # 복소수의 켤레복소수
abs(f1) # 복소수의 절댓값

# 사칙연산

g = 3 / 4
print(g)
# python v2에서는 0으로 나올 것

h = 2**3
print(h)
# 2의 3제곱

i = 5%3
print(i)
# 나머지 연산자

j = 3 // 4
print(j)
# 나눗셈 후 소수점 아랫자리 버림