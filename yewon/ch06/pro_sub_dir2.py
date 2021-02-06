# -*- coding: utf-8 -*- 

import os

# os.walk() 함수 사용
# 시작 디렉터리부터 그 하위의 모든 디렉터리를 차례대로 방문

def search(dirname):
  try:
    for (path, dir, files) in os.walk(dirname): # 디렉터리 순회
      for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".txt":
          print("%s%s" % (path, filename))
  except PermissionError: # 권한이 없는 디렉터리에 접근해도 프로그램이 원활히 계속되도록 한다.
    pass

os.chdir("../")
search(os.getcwd())