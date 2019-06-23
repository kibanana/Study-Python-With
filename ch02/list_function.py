test = [1,2,3,['a','b','c']]

# 값 하나 수정
test[2] = 56
print(test[2])
print(test)

# 범위 안의 값 수정
test[0:2] = ['d','e','f']
print(test)

# 리스트 요소 삭제

# []
test[3:] = []
print(test)

# del
del test[2]
print(test)

del test[1:]
print(test)

# append
test.append(['a', 'b', 'c'])
print(test)

# sort
test.append(9)
test.append(8)
test.append(7)
print(test)
# 리스트 안에 리스트가 있는 경우 sort에서 에러나는 듯

a = [10,9,8,7,6,5]
print(a)
a.sort()
print(a)

print()

# reverse
a.reverse()
print(a)

# index
print(a.index(8))
# 없으면 오류남

# insert
# 첫번째-위치, 두번째-값
a.insert(0, ['a', 'b', 'c'])
print(a)
a.insert(0, 63)
print(a)

# remove
a.remove(63)
print(a)

# pop
# 마지막것 return 후 삭제
print(a.pop())

# count
# 요소 수 세기
print(a.count(6))

# extend
# 리스트에 리스트 붙이기
b = [63,36]
a.extend(b)
print(b)
print(a)