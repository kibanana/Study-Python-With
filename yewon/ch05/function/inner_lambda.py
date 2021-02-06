# -*- coding: utf-8 -*- 

# lambda는 def와 동일한 역할을 한다.
# def를 사용하지 않아도 될 정도로 간단하거나 def를 쓸 수 없는 곳에 주로 쓴다.
# lambda arg1, arg2, ... : 표현식

sum = lambda a, b: a+b
print(sum(15, 30)) # 45

myList = []
myList.append(lambda a, b: a+b)
myList.append(lambda a, b: a-b)
myList.append(lambda a, b: a*b)
myList.append(lambda a, b: a//b)

print(myList[0](5, 10)) # 15
print(myList[1](10, 5)) # 5
print(myList[2](5, 10)) # 50
print(myList[3](10, 5)) # 2