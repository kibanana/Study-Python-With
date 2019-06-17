# 문자열 인덱싱, 슬라이싱
str = "Yewon is the best!"
print(str[0])
print(str[-1])
print(str[-3])
print(str[0:6])
print(str[-5:-1])
print(str[-5:]) # 끝까지 출력
print(str[:6]) # 처음부터 출력

# 슬라이싱 기법
str_slicing = "20010630"
str1 = str_slicing[:4]
str2 = str_slicing[4:]
print(str1)
print(str2)

# 문자열 수정
python = "Pithon"
# python[1] = 'y' # 에러 발생
python = python[:1] + "y" + python[2:]
print(python)

# 문자열 포매팅
str_fruit = "grape"
a = "I eat %s (fruit)" % str_fruit
print(a)

e1 = "sleepy"
e2 = "satisfied"
str_introduction = "I'm %s and %s" % (e1, e2)
print(str_introduction)

# 포맷 코드와 '%' 을 같은 문자열에 사용하려면 '%%'로 나타내야함

# 포맷 코드와 숫자 - 정렬, 공백, 소수점
str_num1 = "%8s is my birthday" % "0630"
str_num2 = "%-8s is my birthday" % "0630"
str_num3 = "%0.5f" % 5.1233456
str_num4 = "%10.5f" % 5.1233456 # 전체 10글자 중 소수점 아래 5글자
print(str_num1)
print(str_num2)
print(str_num3)


# 문자열 관련 함수들
str_name = "Kim Yewon Kim Yejin"

# count
print(str_name.count('Y'))

# find
print(str_name.find(' '))
print(str_name.find('a')) # -1

# index
# find 함수와 거의 비슷하지만, 찾는 문자열이 대상 문자열에 없다면
# 오류가 일어난다는 것이 다름

# join
a = ","
print(a.join('abcd'))
# abcd 각각의 사이에 , 를 삽입함
# a,b,c,d

# upper
print("hello".upper())

# lower
print("HI".lower())

str_strip = " good girl "
# lstrip
print("/" + str_strip.lstrip() + "/")

# rstrip
print("/" + str_strip.rstrip() + "/")

# strip
print("/" + str_strip.strip() + "/")

# replace
print("Yewon".replace("won", "jin"))

# split
str_split = "Good is evil and evil is good"
print(str_split.split())
print(str_split.split('o'))
# 기준이 된 기호는 반환된 배열에 존재하지 않음


# 고급 포매팅
# 1) 인덱스
print("I'm {0} now and I'm {1}".format("smiling", "good"))
# 2) 이름
print("I'm {face} now and I'm {feeling}".format(face="smiling", feeling="good"))
# 3) 인덱스, 이름 혼용

# 4) 정렬 (총 10글자)
print("{0:<10}".format("Hello")) # 왼쪽정렬
print("{0:>10}".format("Hello")) # 오른쪽정렬
print("{0:^10}".format("Hello")) # 중간정렬

# 5) 공백 채우기
print("{0:=<10}".format("Hello")) # 왼쪽정렬시 공백문자 대신 '=' 사용

# 6) 소수점 표현
print("{0:10.4f}".format(3.1234567)) # 왼쪽정렬시 공백문자 대신 '=' 사용

# 7) '{' 또는 '}' 문자 표현
print("{{ and }}".format())