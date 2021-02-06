# -*- coding: utf-8 -*- 

import tempfile
# 파일을 임시로 만들어서 사용한다.

print(tempfile.mktemp()) # 중복되지 않는 임시 파일의 이름을 무작위로 만든다.
print(tempfile.mkdtemp())
print(tempfile.mkstemp())

with tempfile.TemporaryFile() as f: # 기본적으로 wb 모드
  f.close() # f.close() 하는 순간 임시 파일 객체는 사라진다.