def chkDuplicatedNumber(s):
  result = ""
  input_list = list(map(str, s.split()))
  for elem in input_list:
    chk_list = [True for i in range(10)]
    flag = True # 플래그가 없으면 for문 안에서 한 번, 밖에서 한 번 출력되는 경우가 생김
    for letter in elem:
      temp = int(letter)
      if chk_list[temp] is False:
        result += "false "
        flag = False
        break
      else:
        chk_list[temp] = False
    if flag is True:
      if True in chk_list:
        result +="false "
      if True not in chk_list:
        result +="true "
  return result

input_str = "0123456789 01234 01234567890 6789012345 012322456789"
print(chkDuplicatedNumber(input_str))
