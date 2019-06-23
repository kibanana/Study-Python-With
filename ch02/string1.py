str1 = "Hello"
str2 = 'World'
str3 = """Hello World"""
str4 = '''Hello World!'''

print(str1)
print(str2)
print(str3)
print(str4)

# 문자열에 작은따옴표 포함 시 큰따옴표로 둘러야 함
print("Yewon's sleep")
# print('Yewon's sleep')

# 문자열에 작은따옴표 포함 시 큰따옴표로 둘러야 함
print('She said "Good job"')
# print("She said "Good job"")

# 백슬래시 이용
print('She\'brother said \"I\'m sleepy\"')


# 여러 줄인 문자열 변수에 대입
print("a\nb\nc\n")
print("""
a
b
c
""")
print('''
d
f
g
''')


# 문자열 연산

# concat
first = "Kim"
second = "Yewon"


print(first + " " + second)

# multiple
print('=' * 30)
print('Middle of Program')
print('=' * 30)