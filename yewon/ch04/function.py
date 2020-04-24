# 기초적인 내용 패스(함수의 기본 형태)

# 입력값 여러개 받는 함수
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result1 = sum_many(1,2,3)
result2 = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result1)
print(result2)

def sum_mul(x, y):
   return x+y, x*y # 함수의 결과값은 언제나 하나여서 이런 반환값의 타입은 튜플이다

sum_result, mul_result = sum_mul(3,4)
print(sum_result)
print(mul_result)

# 인수에 초기값 설정
# 초기값은 오른쪽에만 존재해야 한다. 중간에 끼면 인터프리터가 인수를 어디에 대입할지 모르게 된다
def say_myself(name, age, gender='female'):
  print('내 이름', name, '내 나이', age)
  if gender == 'female':
    print('여자입니다')
  else:
    print('남자입니다')

say_myself('김예원', '18')

# 함수 내에서 선언된 변수는 기본적으로, 함수 밖에서 사용할 수 없다.
# 만약 꼭 그 변수를 함수 밖에서 사용하고 싶다면 return 하거나 global로 선언(추천 X)하면 된다