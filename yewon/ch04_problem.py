# 1
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)

# 2 : sample.txt 파일에 줄마다 있는 숫자값을 모두 읽어서 총합과 평균값을 구한 후 result.txt 파일에 작성
f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
	score = int(line)
	total += score

average = total / len(lines)

f = open('result.txt', 'w')
f.write(str(average)) # 숫자값은 바로 파일에 쓸 수 없다.
f.close()