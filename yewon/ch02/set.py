# -*- coding: utf-8 -*- 

# 중복을 허용하지 않고, 순서가 없다.
# (function 수가 좀 적어서 그냥 한 파일에 모두 연습함)

prac_set1 = set([1,2,4,2,3])
print(prac_set1)

prac_set2 = set('applepie')
print(prac_set2)

prac_set3 = set([1, 2, 3, 4, 5])
prac_set4 = set([5, 6, 7, 8, 9])

# 교집합
print(prac_set3 & prac_set4)
print(prac_set3.intersection(prac_set4))
print(list(prac_set3 & prac_set4))

print()

# 합집합
print(prac_set3 | prac_set4)
print(prac_set3.union(prac_set4))
print(list(prac_set3 | prac_set4))

print()

# 차집합
print(prac_set3 - prac_set4)
print(prac_set3.difference(prac_set4))
print(prac_set4.difference(prac_set3))
print(prac_set4.difference(prac_set4))
print(list(prac_set3 - prac_set4))

print()

# add, update, remove
prac_set3.add(63)
print(prac_set3)
prac_set3.update([63, 36, 33, 66]) # add이되 여러 값 add
print(prac_set3)
prac_set3.remove(63)
print(prac_set3)