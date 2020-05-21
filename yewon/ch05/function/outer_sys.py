import sys

temp = sys.argv
print(temp)
print(temp[1:])

if "exit" in temp:
  print("스크립트를 강제 종료합니다")
  sys.exit()