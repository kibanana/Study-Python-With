# -*- coding: utf-8 -*- 

import re

# 문자 클래스 []
# 문자와 매치

# re.sub은 무조건 매개변수를 세 개 전달해야 한다. 아니면 무조건 에러다.
# re.sub(pattern, repl, string)

example1 = re.compile("[abc]") # a, b, c 매치
print(re.sub(example1, "z", "aaabbbccc"))
print(re.sub(example1, "before", "aaabbbccc"))
print(re.sub(example1, "dude", "aaabbbccc"))

example2 = re.compile("[A-Z]") # 대문자 매치
print(re.sub(example2, "Yewon", "Apple"))
print(re.sub(example2, "김예원", "Kim"))

example3 = re.compile("[1-5]") # 1-5 숫자 매치
print(re.sub(example3, "kyw017763", "63"))

example4 = re.compile("[^0-9]") # 숫자 아닌 것 -> 문자 매치
print(re.sub(example4, "a", "KimKimKim"))


print("=" * 50)


exampled = re.compile("[\d]")
exampleD = re.compile("[\D]")
examples = re.compile("[\s]")
exampleS = re.compile("[\S]")
examplew = re.compile("[\w]")
exampleW = re.compile("[\W]")

# \d : 숫자와 매치
print(re.sub(exampled, "12345", "abcde63"))
print(re.sub(exampled, "abcde", "abcde63"))

# \D : 숫자가 아닌 것과 매치
print(re.sub(exampleD, "12345", "1a2b"))
print(re.sub(exampleD, "", "1a2b"))

# \s : whitespace(= 이스케이프 시퀀스)와 매치
print(re.sub(examples, "*nextline*", "abcde\n"))
print(re.sub(examples, "*tab*", "abcde\t"))

# \S : whitespace(= 이스케이프 시퀀스)와 매치
print(re.sub(exampleS, "*nextline*", "abcde\n"))
print(re.sub(exampleS, "*tab*", "abcde\t"))

# \w : 문자 + 숫자와 매치 [a-zA-Z0-9]
print(re.sub(examplew, "", "?"))
print(re.sub(examplew, "", "a1b2c3?"))

# \W : 문자 + 숫자가 아닌 문자와 매치 [^a-zA-Z0-9]
print(re.sub(exampleW, "", "?"))
print(re.sub(exampleW, "", "a1b2c3?"))


print("=" * 50)


# 반복

# .(dot)
# \n를 제외한 모든 문자와 매치된다
example5 = re.compile("a.b")
example6 = re.compile("a...b")

print(re.sub(example5, "", "acb"))
print(re.sub(example5, "", "adb"))
print(re.sub(example5, "", "ab"))

# * 0 ~
example7 = re.compile("ca*t")
print(re.sub(example7, "", "cat"))
print(re.sub(example7, "", "caaat"))

# + 1 ~
example8 = re.compile("ca+t")
print(re.sub(example8, "", "cat"))
print(re.sub(example8, "", "caaat"))

# {}
example9 = re.compile("ap{,9}e") # ~9
example10 = re.compile("ap{9,}e") # 9~
example11 = re.compile("ap{1,3}e") # 1~3
example12 = re.compile("ap{2}e") # 2

print(re.sub(example9, "", "apple"))
print(re.sub(example9, "", "appppppppppppple"))

print(re.sub(example10, "", "apple"))
print(re.sub(example10, "", "appllllllllllllle"))

print(re.sub(example11, "", "apple"))
print(re.sub(example11, "", "appleeeeeeeeeeeeee"))

print(re.sub(example12, "", "apple"))
print(re.sub(example12, "", "appppppppppple"))

# ? 0~1
example13 = re.compile("app?e")
print(re.sub(example13, "" "apple"))
print(re.sub(example13, "" "appe"))
