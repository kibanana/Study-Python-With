from time import time, localtime, asctime, ctime, strftime, strptime, sleep

# time
# UTC를 이용하여 현재 시간을 실수 형태로 리턴한다.
# 1970년 1월 1일 0시 0분 0처 기준으로 지난 시간을 초 단위로 리턴한다.
print(time())

# localtime
# 초로 표현된 일시를 연도,월,일,시,분,초 형태로 바꿔준다.
print(localtime(time()))

# asctime
# 연도,월,일,시,분,초 형태로 표현된 일시를 날짜와 시간을 알아보기 쉬운 형태로 리턴한다.
# -> 반환된 튜플 형태의 값을 인수로 받는다.
print(asctime(localtime(time())))

# ctime
# asctime(localtime(time())) == ctime()
# asctime과 다른 점은 ctime은 언제나 현재 시간만 리턴한다는 점이다.
print(ctime())

# strftime
print(strftime("%x %X", localtime(time())))
print(strftime("%c", localtime(time())))
print(strftime("%Y-%m-%d", localtime(time())))

# strptime

# sleep
# 주로 루프 안에서 실행시켜서 일정한 시간 간격을 두고 루프를 실행할 수 있도록 한다.
for i in range(10):
  print(i)
  sleep(1)