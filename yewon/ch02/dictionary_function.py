# -*- coding: utf-8 -*- 

d = {
    'birth': 20010630,
    'name': 'yw',
    'friends' : ['hj', 'jh', 'tm']
}

# keys
print(d.keys())
print(type(d.keys()))

for k in d.keys():
    print(k)

list_k = list(d.keys()) # d의 keys 객체를 리스트로 변환
print(list_k)
print(type(list_k))

# values
print(d.values())
print(type(d.values()))

for v in d.values():
    print(v)

list_v = list(d.values()) # d의 values 객체를 리스트로 변환
print(list_v)
print(type(list_v))

# items
# (key, item) 형태의 튜플 리스트 반환
print(d.items())
print(list(d.items()))
print(list(d.items())[0])

# get
print(d.get('birth'))
# 존재하지 않는 키로 가져올 때 
# None을 리턴
# d['notExist'] 는 키오류 발생
print(d.get('birth', 'notExist')) # get default 값 지정
print(d.get('friends', 'notExist'))
print(d.get('age', 'notExist'))

# in
# 키값으로 검색
# True, False 반환
print('name' in d)

# clear
print(d.clear()) # {}
print(d)