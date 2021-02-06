# -*- coding: utf-8 -*- 

import os

# 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해준다.

# os.environ
# 환경변수 정보

# print(os.environ)

# os.chdir
# 현재 디렉터리의 위치 변경
os.chdir("../")

# os.getcwd
# 현재 디렉터리 위치 리턴
print(os.getcwd()) # 원래 ../function 인데 os.chdir로 바꿔서 ../ch05

# os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수 있다.

# print(os.system("dir")) # Windows 운영체제일 때
print(os.system("ls")) # MacOS 운영체제일 때

# os.popen()
# 시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일 객체로 리턴한다.
os.chdir("./function")
print(os.getcwd())
# f = os.popen("dir")
f = os.popen("ls")
data = f.read()
with open("popenResult.txt", "w") as f:
  f.write(data)
  f.close()

# os.mkdir(), os.rmdir()
# 디렉터리를 생성 & 삭제(디렉터리가 비어있을 경우에만)한다.
os.mkdir("testDir")
f = os.popen("dir")
data = f.read()
with open("mkdirResult.txt", "w") as f:
  f.write(data)
  f.close()
os.rmdir("testDir")

# os.unlink()
# 파일을 지운다
# os.unlink("popenResult.txt")

# os.rename(src, dst)
os.rename("mkdirResult.txt", "mkdir.txt")