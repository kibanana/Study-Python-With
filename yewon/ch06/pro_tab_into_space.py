import sys

# python pro_tab_into_space.py example.txt exampleResult.txt

option = sys.argv[1:]
src = option[0]
dst = option[1]

data = ""

with open(src) as f:
  temp = f.read() # \t 탭은 어쩐지 감지가 안돼서 "00"로 대체
  data = temp.replace("00", " " * 4)
  f.close()
  
with open(dst, "w") as f:
  f.write(data)
  f.close()