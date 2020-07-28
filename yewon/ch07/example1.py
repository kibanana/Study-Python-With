# -*- coding: utf-8 -*- 

import re

# 주민등록번호 뒷자리를 *로 바꾸자
data = """
park 800905-1049118
kim 700905-1059119
"""

# 1) 정규표현식을 모를 때
result = []
for line in data.split("\n"):
  word_result = []
  for word in line.split():
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): # 이름인가 / 주민등록번호인가
      word = "%s-*******" % word[:6]
    word_result.append(word) # 이름 -> 변환된 주민등록번호 순서
  result.append(" ".join(word_result))
print("\n".join(result))

# 2) 정규표현식을 사용할 수 있을 때
reg = re.compile("(\d{6})[-]\d{7}")
print(reg.sub("\g<1>-*******", "", data))