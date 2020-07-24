# -*- coding: utf-8 -*- 
import re
# re: regular expression의 약어
# re.compile()로 정규표현식을 컴파일하고 그 결과로 리턴되는 (컴파일된 패턴)객체를 이용하여 이후 작업을 수행한다.

# 1) 매치되면 match 객체 매치하지 않으면 None 리턴
# match(): 문자열의 처음(공백으로 분리될 때부터 처음이 아니게 됨) -> 아니면 None -> if & else
# search(): 문자열 전체

example1 = re.compile("[a-e]+") # a-e 값이 0~ 개
print(re.match(example1, "apple"))
print(re.match(example1, "birthday is good day"))
print(re.match(example1, "dog and cat is cute"))
print(re.match(example1, "good day is hard"))

print(re.search(example1, "apple"))
print(re.search(example1, "birthday is good day"))
print(re.search(example1, "dog and cat is cute"))
print(re.search(example1, "good day is hard"))

# 2) 
# findall(): 정규식과 매치되는 모든 문자열을 리스트로 리턴
print(re.findall(example1, "apple"))
print(re.findall(example1, "birthday is good day"))
print(re.findall(example1, "dog and cat is cute"))
print(re.findall(example1, "good day is hard"))

# finditer(): 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴 -> 각각의 요소는 match 객체
result1 = re.finditer(example1, "apple")
result2 = re.finditer(example1, "birthday is good day")
result3 = re.finditer(example1, "dog and cat is cute")
result4 = re.finditer(example1, "good day is hard")

# match 객체 -> match(), search(), finditer() 결과값으로 리턴된다.
# group(), start(), end(), span()
# match()의 결과값으로 반환된 match 객체의 .start() 값은 언제나 0이다.

for i in result1:
  print(i.group(), i.start(), i.end(), i.span())

for i in result2:
  print(i.group(), i.start(), i.end(), i.span())

for i in result3:
  print(i.group(), i.start(), i.end(), i.span())

for i in result4:
  print(i.group(), i.start(), i.end(), i.span())


# 컴파일 옵션 (re.compile의 두 번째 또는 세 번째 인자로 전달한다)

# DOTALL, S -> 모든 문자와 매치(특히 \n 포함) 
s1 = re.match("a.b", "a\nb", re.DOTALL)
s2 = re.match("a.b", "a\nb", re.S)
s3 = re.match("a.b", "a\nb")
print(s1.group(), s1.start(), s1.end(), s1.span())
print(s2.group(), s2.start(), s2.end(), s2.span())
print(s3.group(), s3.start(), s3.end(), s3.span())

# IGNORECASE, I -> 대소문자 관계없이 매치 -> [a-z] 정규표현식이 A-Z도 포함하게 된다
i1 = re.match("[a-z]", "python", re.IGNORECASE)
i2 = re.match("[a-z]", "Python", re.I)
i3 = re.match("[a-z]", "Python")
i4 = re.match("[a-z]", "123")
print(i1.group(), i1.start(), i1.end(), i1.span())
print(i2.group(), i2.start(), i2.end(), i2.span())
print(i3.group(), i3.start(), i3.end(), i3.span())
print(i4.group(), i4.start(), i4.end(), i4.span())

# MULTILINE, M -> 여러 줄과 매치 -> ^, $ 메타문자를 한 문자열의 처음이나 끝이 아니라 여러 줄의 입력 중 각 라인의 처음이나 끝으로 인식하게 한다
data = """
python is snake
python is programming language
python is what?
python is good
python is great
"""

m1 = re.findall("^python\s\w", data, re.MULTILINE) # python이라는 문자열로 시작해서 whitespace, 단어가 차례대로 온다.
m2 = re.findall("^python\s\w", data, re.M)
m3 = re.findall("^python\s\w", data)
print(m1)
print(m2)
print(m3)

# VERBOSE, X -> 정규식을 보기 편하게 만들거나 주석 등을 사용할 수 있는 verbose 모드
exampleX1 = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")
exampleX2 = re.compile(r"""
&[#] # Start of a numeric entity reference
(
  0[0-7]+ | [0-9]+ | x[0-9a-fA-F] # octal form, decimal form, hexadecimal form
)
;
""", re.VERBOSE)

# 백슬래시를 정규표현식 내에 넣고 싶으면 이스케이프 시퀀스와 헷갈리지 않도록 \\ 형태로 써야 한다. 또한 정규식 엔진으로 정규식을 컴파일하는 도중에 문제가 생길 수 있기 때문에
# \\\\ 처럼 백슬래시를 4개나 써서 단 하나의 백슬래시를 표현해야 한다.
# 이렇게 되면 너무 복잡하다. 따라서 컴파일해야하는 정규식이 Raw String임을 알려줄 수 있도록 r""를 사용한다.

p = re.compile(r'\\section')