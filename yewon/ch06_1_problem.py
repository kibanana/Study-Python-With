def compress_str(s):
  result = ""
  curr = ""
  cnt = 0
  for i in s:
    if curr != i:
      if curr != "":
        result += curr + str(cnt)
      curr = i
      cnt = 1
    else:
      cnt += 1
  result += curr + str(cnt) # 마지막 것이 출력 안되므로

str_input = "aaabbcccccca"
print(compress_str(str_input))
