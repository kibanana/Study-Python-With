# 사용자 입출력
x = input()
print(x)

number = input('숫자를 입력하세요:')
if number.isdecimal():
	print('숫자다!')
else:
	print('숫자 아니다!')

print("나" "배고파" "졸려") # "(문자열)"은 + 연산과 동일하다
print("나", "배고파", "졸려") # 문자열 띄어쓰기
for i in range(10):
	print(i, end=' ') # 한 줄에 결과 출력


# 파일 입출력

# 1. 파일 생성
f = open('new_file.txt', 'w') # 파일 열기 모드 : r, w, a
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 사라진다.
# 파일 생성 시 절대경로나 상대경로를 사용할 수 있다.
f.close() # 열려 있는 파일 객체를 닫는다. 원래 파이썬이 열려 있는 파일 객체를 자동으로 닫기때문에 생략해도 되지만,
# 생략해도 되지만, 쓰기 모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문에 명시적으로 해주는 게 좋다.

# 2. 파일 쓰기 모드로 열어서 Write
f = open('new_file.txt', 'w')
for i in range(1, 11):
	data = "%d번째 줄이다.\n" % i
	f.write(data)
f.close()

# 3. 프로그램 외부에 저장된 파일 읽기
# 1) readline() 함수 이용
f = open('new_file.txt', 'r')
while True:
	line = f.readline() # 더이상 읽을 라인이 없으면 None
	if not line: break
	print(line)
f.close()

# 2) readlines() 함수 이용
f = open('new_file.txt', 'r')
lines = f.readlines()
for line in lines:
	print(line)
f.close()

# 3) read() 함수 이용
f = open('new_file.txt', 'r')
data = f.read()
print(data)
f.close()

# 4. 파일에 새로운 내용 Append - Wirte 모드는 이미 존재하는 파일의 경우 그 파일의 내용이 모두 사라진다.
f = open('new_file.txt', 'a')
for i in range(11, 20):
	data = "%d번째 줄이다.\n" % i 
	f.write(data)
f.close()

# 5. with문
with open('new_file.txt', 'w') as f:
	f.write('Life is too short, you need python')