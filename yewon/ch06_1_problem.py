str_input = "aaabbcccccca"

curr = ""
cnt = 0

for i in str_input:
  if curr != i:
    if curr != "":
      print(curr + str(cnt), end="")
    curr = i
    cnt = 1
  else:
    cnt += 1

print(curr + str(cnt), end="") # 마지막 것이 출력 안되므로