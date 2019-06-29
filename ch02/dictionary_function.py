d = {
    'birth': 20010630,
    'name': 'yw',
    'friends' : ['hj', 'jh', 'tm']
}

# keys
print (d.keys())

for k in d.keys():
    print (k)

list_k = list(d.keys()) # d의 keys 객체를 리스트로 변환

# values
print (d.values())

for v in d.values():
    print (v)

list_v = list(d.values()) # d의 values 객체를 리스트로 변환

# items
print (d.items())

# clear
# print (d.clear()) # {}

# get
print(d.get('birth'))
# 존재하지 않는 키로 가져올 때 
# None을 리턴
# d['notExist'] 는 키오류 발생
print(d.get('notExist', 'birth')) # get default 값 지정

# in
# 키값으로 검색
# True, False 반환
print('name' in d)