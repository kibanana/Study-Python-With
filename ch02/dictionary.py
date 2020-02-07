# 다른 형태로는 연관배열, 해시
# key : value 관계로 구성 => 순차적이지 않음

d = {
    'birth': 20010630,
    'name': 'yw',
    'friends' : ['hj', 'jh', 'tm']
}

# 추가
d['age'] = 19
# 문자열 key를 이용해서 추가 시 ''로 key 감싸줌

d[2] = 15;
d[5] = ['a','b','c']

print(d)


# 삭제
del d['age']

print(d)


# 사용방법
print(d['name'])
print(d[5])

# 중복되는 키로 정한 값 중 무엇이 저장될지 모름 => 중복된 키 사용 X
# 리스트는 변할 수 있는 값이기에 key로 사용할 수 없음