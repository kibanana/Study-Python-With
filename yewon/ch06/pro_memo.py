# -*- coding: utf-8 -*- 

import sys

# option -o: 한 줄 -> 바로 다음 실행옵션이 저장할 값이다.
# option -m: 여러 줄 -> while문으로 저장할 값을 입력받는다.
# option -a: 추가적으로 기입 -> 바로 다음 실행옵션 -o 또는 -m
# option -v: 파일 내용 보기 -> 출력
# 빈 파일은 생성하지 않는다.

# ex) python pro_memo.py -w -o "The person has their own time. My time is now. I will make it like that"
# ex) python pro_memo.py -w -m
# ex) python pro_memo.py -v

option = sys.argv[1:]
data = ""

if "-o" in option:
    data = option[option.index("-o") + 1] # one line 옵션 바로 다음 값 
elif "-m" in option:
  while True:
    temp = input()
    if temp == ":wq!":
      break
    else:
      data += temp + "\n"

mode = ""

if "-a" in option: # append mode
  mode = "a"
elif "-v" in option: # view mode
  mode = "r"
elif "-a" not in option: # write mode
  mode = "w"

with open("memo.txt", mode) as f:
  if mode == "a" or mode == "w":
    f.write(data)
  else:
    reading = f.read()
    print(reading)
  f.close()